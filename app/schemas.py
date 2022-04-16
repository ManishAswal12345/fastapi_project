from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, conint

from app.database import Base


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    

class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True


class Post(PostBase):
    # Defines what fields to send in our response
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    class Config:
        # Allows Pydantic model to read orm mode as well(not only dict).
        orm_mode = True
        
        
class PostOut(BaseModel):
    Post: Post
    votes: int
    class Config:
        orm_mode = True
        

class UserCreate(BaseModel):
    email: EmailStr
    password: str
        

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
    
class TokenData(BaseModel):
    id: Optional[str] = None
    
    
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)