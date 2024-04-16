from typing import Optional
from pydantic import BaseModel,EmailStr, conint
from datetime import datetime

class PostBase(BaseModel):
    title:  str
    content:    str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserCreate(BaseModel):
    email_id: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email_id: str
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email_id: EmailStr
    password: str

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner:UserOut

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int]=None

class Vote(BaseModel):
    post_id: int 
    dir: conint(le=1)
