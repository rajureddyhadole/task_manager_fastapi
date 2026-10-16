from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr = Field(max_length=100)


class UserIn(UserBase):
    password: str = Field(min_length=6, max_length=255)


class UserResponse(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class TaskBase(BaseModel):
    title: str = Field(min_length=5, max_length=200)
    description: str | None = Field(
        default=None,
        max_length=400,
        description="detailed notes about this task",
    )
    due_date: datetime | None = None


class TaskCreate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)
