from dotenv import load_dotenv
load_dotenv()

from langchain.chains.summarize.map_reduce_prompt import prompt_template

from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from fastapi import FastAPI
from langserve import add_routes
model = ChatOpenAI(model="gpt-4", temperature=0.3)

system_prompt = "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt),("user","{text}")
    ]
)

parser = StrOutputParser()
chain = prompt_template| model | parser

app = FastAPI(
    title="LangChain API",
    version="1.0.0",
    description="translator APP",
)

add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)