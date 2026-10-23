from fastapi import FastAPI

import models
from database import Base, engine
from routers import auth, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

app.include_router(auth.router)
app.include_router(tasks.router)


@app.get("/")
def root():
    return {"message": "welcome to the Task Manager API!"}
