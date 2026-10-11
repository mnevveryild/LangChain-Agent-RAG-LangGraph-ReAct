from dotenv import load_dotenv
from langchain.chains.summarize.map_reduce_prompt import prompt_template

load_dotenv()
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4", temperature=0.3)

system_prompt = "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt),("user","{text}")
    ]
)

parser = StrOutputParser()
chain = prompt_template| model | parser


if __name__ == "__main__":
    print(chain.invoke({"language" : "italian", "text" : "i love you" }))