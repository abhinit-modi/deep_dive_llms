from langchain_core.runnables import Runnable
from langchain_core.callbacks import BaseCallbackHandler
from fastapi import FastAPI, Request, Depends
from sse_starlette.sse import EventSourceResponse
from langserve.serialization import WellKnownLCSerializer
from typing import List
from sqlalchemy.orm import Session

import schemas
from chains import simple_chain
# import crud, models, schemas
from database import SessionLocal, engine
# from callbacks import LogResponseCallback


# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def generate_stream(input_data: schemas.BaseModel, runnable: Runnable, callbacks: List[BaseCallbackHandler]=[]):
    for output in runnable.stream(input_data.dict(), config={"callbacks": callbacks}): 
        data = WellKnownLCSerializer().dumps(output).decode("utf-8")
        yield {'data': data, "event": "data"} 
    yield {"event": "end"}


@app.post("/simple/stream")
async def simple_stream(request: Request):
    data = await request.json()
    user_question = schemas.UserQuestion(**data['input'])
    return EventSourceResponse(generate_stream(user_question, simple_chain))


@app.post("/formatted/stream")
async def formatted_stream(request: Request):
    # TODO: use the formatted_chain to implement the "/formatted/stream" endpoint.
    raise NotImplemented


@app.post("/history/stream")
async def history_stream(request: Request, db: Session = Depends(get_db)):  
    # TODO: Let's implement the "/history/stream" endpoint. The endpoint should follow those steps:
    # - The endpoint receives the request
    # - The request is parsed into a user request
    # - The user request is used to pull the chat history of the user
    # - We add as part of the user history the current question by using add_message.
    # - We create an instance of HistoryInput by using format_chat_history.
    # - We use the history input within the history chain.
    raise NotImplemented


@app.post("/rag/stream")
async def rag_stream(request: Request, db: Session = Depends(get_db)):  
    # TODO: Let's implement the "/rag/stream" endpoint. The endpoint should follow those steps:
    # - The endpoint receives the request
    # - The request is parsed into a user request
    # - The user request is used to pull the chat history of the user
    # - We add as part of the user history the current question by using add_message.
    # - We create an instance of HistoryInput by using format_chat_history.
    # - We use the history input within the rag chain.
    raise NotImplemented


@app.post("/filtered_rag/stream")
async def filtered_rag_stream(request: Request, db: Session = Depends(get_db)):  
    # TODO: Let's implement the "/filtered_rag/stream" endpoint. The endpoint should follow those steps:
    # - The endpoint receives the request
    # - The request is parsed into a user request
    # - The user request is used to pull the chat history of the user
    # - We add as part of the user history the current question by using add_message.
    # - We create an instance of HistoryInput by using format_chat_history.
    # - We use the history input within the filtered rag chain.
    raise NotImplemented
    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", reload=True,  port=8000)