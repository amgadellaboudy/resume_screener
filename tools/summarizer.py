from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from tools.schemas import CandidateSummary
from dotenv import load_dotenv

load_dotenv()
parser = PydanticOutputParser(pydantic_object=CandidateSummary)

prompt = ChatPromptTemplate.from_template(
    """
    Summarize the following resume.

    Resume:
    {resume_text}

    {format_instructions}
    """
)

llm = ChatOpenAI(model="gpt-4o", temperature=0)


def summarize_resume(resume_text: str) -> CandidateSummary:
    formatted_prompt = prompt.format_prompt(
        resume_text=resume_text,
        format_instructions=parser.get_format_instructions()
    )
    output = llm.invoke(formatted_prompt.to_messages())
    return parser.parse(output.content)
