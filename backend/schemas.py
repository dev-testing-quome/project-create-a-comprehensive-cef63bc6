from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr = Field(..., regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    password: str = Field(..., min_length=8)
    is_instructor: Optional[bool] = False

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_instructor: bool
    created_at: datetime
    updated_at: datetime

class CourseCreate(BaseModel):
    title: str
    description: str

class CourseResponse(BaseModel):
    id: int
    title: str
    description: str
    instructor_id: int
    created_at: datetime
    updated_at: datetime

class ModuleCreate(BaseModel):
    title: str
    content: str

class ModuleResponse(BaseModel):
    id: int
    title: str
    content: str
    course_id: int
    created_at: datetime
    updated_at: datetime
