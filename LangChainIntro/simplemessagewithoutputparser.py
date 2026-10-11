from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4", temperature=0.3)

messages = [
    SystemMessage(content="translate the following from English to Spanish"),
    HumanMessage(content="hi"),
]

parser = StrOutputParser()
chain = model | parser


if __name__ == "__main__":
    print(chain.invoke(messages))