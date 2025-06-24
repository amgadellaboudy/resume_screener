from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model="gpt-4o", temperature=0.7)


def generate_outreach_email(summary_obj, jd_text):
    prompt = ChatPromptTemplate.from_template(
        """
        Write a short outreach email to this candidate.

        Candidate Summary:
        {summary}

        Job Description:
        {jd}

        Keep it friendly and personalized.
        """
    )
    formatted = prompt.format_prompt(summary=summary_obj.summary, jd=jd_text)
    return llm.invoke(formatted.to_messages()).content.strip()
