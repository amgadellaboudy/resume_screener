# app.py
import streamlit as st
import os
from tools.agent import evaluate_candidate

st.set_page_config(page_title="Resume Screener GPT")
st.title("📄 Resume Screener GPT")

st.markdown("Upload a resume PDF and paste the link to the job description.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
jd_url = st.text_input("Paste Job Description URL or Text")

if uploaded_file and jd_url:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    jd_path = "temp_jd.txt"
    if jd_url.startswith("http"):
        import requests
        jd_text = requests.get(jd_url).text
        with open(jd_path, "w", encoding="utf-8") as f:
            f.write(jd_text)
    else:
        with open(jd_path, "w", encoding="utf-8") as f:
            f.write(jd_url)

    with st.spinner("Evaluating candidate..."):
        results = evaluate_candidate("temp_resume.pdf", jd_path)

    st.subheader("Candidate Summary")
    st.write(results["summary"])

    st.subheader("Match Score")
    st.write(f"{results['score']} / 10")

    st.subheader("Strengths")
    st.markdown("\n".join(f"- {s}" for s in results["strengths"]))

    st.subheader("Weaknesses")
    st.markdown("\n".join(f"- {w}" for w in results["weaknesses"]))

    st.subheader("Outreach Email")
    st.code(results["email"], language="markdown")

    try:
        os.remove("temp_resume.pdf")
        os.remove("temp_jd.txt")
    except OSError as e:
        st.warning(f"Could not delete temp files: {e}")
