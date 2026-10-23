from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from models import Task, User
from schemas import TaskCreate, TaskResponse
from security import get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    task_in: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_task = Task(
        title=task_in.title,
        description=task_in.description,
        due_date=task_in.due_date,
        user_id=current_user.id,
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@router.get("", response_model=list[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    return (
        db.execute(select(Task).where(Task.user_id == current_user.id)).scalars().all()
    )
