from sqlalchemy.orm import Session
import models, schemas


def get_or_create_user(db: Session, username: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        user = models.User(username=username)
        db.add(user)
        db.commit()
        db.refresh(user)
    return user

def add_message(db: Session, message: schemas.MessageBase, username: str):
    # TODO:  Implement the add_message function. It should:
    # - get or create the user with the username
    # - create a models.Message instance
    # - pass the retrieved user to the message instance
    # - save the message instance to the database
    raise NotImplemented

def get_user_chat_history(db: Session, username: str):
    raise NotImplemented