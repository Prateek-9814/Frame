from sqlalchemy import Column, String, Integer
from config import Base

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    no_tickets = Column(String)
