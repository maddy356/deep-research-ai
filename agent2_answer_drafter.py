import os
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0.7)

prompt_template = PromptTemplate.from_template(
    "Based on the research below, write a detailed and clear response:\n\n{content}"
)

def draft_answer(research_content: str) -> str:
    """
    Takes in research content and returns a well-formed response using OpenAI's model.
    """
    prompt = prompt_template.format(content=research_content)
    return llm.predict(prompt)
if __name__ == "__main__":
    test_research = "Python is a programming language used for web development, data science, AI, and more."
    answer = draft_answer(test_research)
    print("\n--- Drafted Answer ---\n")
    print(answer)
