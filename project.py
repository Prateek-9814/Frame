from typing import List
from fastapi import FastAPI, Depends
from promodel import User
import re
from count import *
from config import Base, engine, sessionmaker, SessionLocal
import models 
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Users).all()

@app.post("/")
async def create_user(user:User, db: Session= Depends(get_db)):
    x= Count_ticket()
    if (x != 0): 
        while(x>= user.no_tickets):
            user_model = models.Users()
            user_model.first_name= user.first_name
            user_model.last_name= user.last_name
            user_model.email= user.email
            user_model.no_tickets= user.no_tickets
            if (re.match("[a-zA-z0-9_\-\.]+@[a-zA-Z]+\.(com|edu|net|in)", user.email) and ("[a-zA-z]{2,}", user.first_name) and ("[a-zA-z]{2,}", user.last_name)):
                x = Count_ticket(user.no_tickets)
                print(x)
                db.add(user_model)
            else:
                return("Try again!")
            break
    db.commit()
    return {
        'remaining_tickets': x,
        'status': 201, 
        'transaction' : 'successful'
     }

# @app.delete("/{user_fisrt_name}")
# async def delete_user(user.first_name, db: Session=Depends(get_db)):
#     for user.first_name in db:
#         pass
