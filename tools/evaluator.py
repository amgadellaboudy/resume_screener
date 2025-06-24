from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from tools.schemas import ResumeEvaluation
from typing import Dict

load_dotenv()
llm = ChatOpenAI(model="gpt-4o", temperature=0)

parser = PydanticOutputParser(pydantic_object=ResumeEvaluation)

# Create prompt template
prompt = ChatPromptTemplate.from_template(
    """
    You are an AI recruiter. Compare the resume below to the job description.

    Resume:
    {resume}

    Job Description:
    {jd}

    Your task:
    1. Rate match score from 1 to 10.
    2. List 2 strengths.
    3. List 2 weaknesses.

    Respond in JSON format as specified:
    {format_instructions}
    """
)


# Evaluate and parse
def score_resume_against_jd(resume_text: str, jd_text: str) -> Dict:
    formatted_prompt = prompt.format_prompt(
        resume=resume_text,
        jd=jd_text,
        format_instructions=parser.get_format_instructions()
    )
    response = llm.invoke(formatted_prompt.to_messages())
    return parser.parse(response.content).model_dump(mode='json')
