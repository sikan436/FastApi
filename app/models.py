from app.database import Base 
from sqlalchemy import TIMESTAMP, Column, ForeignKey,Integer,String,Boolean, text
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ ="posts"

    id= Column(Integer,primary_key=True,nullable=False)
    title= Column(String,nullable=False)
    content= Column(String,nullable=False)
    published=Column(Boolean,server_default="True",nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))
    owner_id=Column(Integer, ForeignKey("users.id",ondelete="cascade"),nullable=False)
    owner=relationship("User")

class User(Base):
    __tablename__="users"
    email_id=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    id= Column(Integer,primary_key=True,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))

class Vote(Base):
    __tablename__="votes"
    post_id=Column(Integer,ForeignKey("posts.id",ondelete="cascade"),nullable=False,primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id",ondelete="cascade"),nullable=False,primary_key=True)


