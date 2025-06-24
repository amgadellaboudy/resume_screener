from tools.utils import load_text_or_pdf
from tools.summarizer import summarize_resume
from tools.evaluator import score_resume_against_jd
from tools.email_writer import generate_outreach_email


def evaluate_candidate(resume_path: str, jd_path: str):
    resume_text = load_text_or_pdf(resume_path)
    jd_text = load_text_or_pdf(jd_path)

    summary = summarize_resume(resume_text)
    eval_results = score_resume_against_jd(resume_text, jd_text)
    email = generate_outreach_email(summary, jd_text)

    return {
        "summary": summary.summary,
        "score": eval_results["score"],
        "strengths": eval_results["strengths"],
        "weaknesses": eval_results["weaknesses"],
        "email": email
    }