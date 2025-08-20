from pydantic.v1 import BaseModel


class UserQuestion(BaseModel):
    question: str

# TODO: create a HistoryInput data model with a chat_history and question attributes.
class HistoryInput(BaseModel):
    pass

# TODO: let's create a UserRequest data model with a question and username attribute. 
# This will be used to parse the input request.
class UserRequest(BaseModel):
    username: str

# TODO: implement MessageBase as a schema mapping from the database model to the 
# FastAPI data model. Basically MessageBase should have the same attributes as models.Message
class MessageBase(BaseModel):
    pass
