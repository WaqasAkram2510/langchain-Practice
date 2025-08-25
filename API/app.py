from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama

load_dotenv("../.env") 

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')



app = FastAPI(
    title = "Langchain Server",
    version = "1.0",
    description = "This is a Langchain server using FastAPI"
)

add_routes(
    app,
    ChatOpenAI(),
    path = "/openai"
)

model = ChatOpenAI()
llm = Ollama(model = "llama2")

prompt1 = ChatPromptTemplate.from_template("Write me a essay about {Topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {Topic} with 50 words")


add_routes(
    app,
    prompt1|model,
    path = '/essay'
)

add_routes(
    app,
    prompt2|llm,
    path = '/poem'
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
