from fastapi import FastAPI
from schemas import TaskRead, TaskCreate
from database import engine, Base, get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import HTTPException
import models
app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return{"message":"Its working Priya!"}
@app.post("/tasks/", response_model = TaskRead)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
      
    db_task = models.Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    return db_task

@app.get("/tasks/",response_model=list[TaskRead])
def read_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()

@app.get("/tasks/{task_id}", response_model=TaskRead)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code = 404, detail = "data not found")
    return task

@app.put("/tasks/{task_id}",response_model = TaskRead)
def update_task(task_id:int, task : TaskCreate, db:Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id==task_id).first()
    if not db_task:
        raise HTTPException(status_code = 404, detail = "data not found")
    db_task.title = task.title
    db_task.description = task.description
    db.commit()
    db.refresh(db_task)
    return db_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id:int, db:Session=Depends(get_db)):
    db_task =  db.query(models.Task).filter(models.Task.id==task_id).first()
    if not db_task:
        return HTTPException(status_code = 404, detail= "data not found")
    
    db.delete(db_task)
    db.commit()
 
    return {"message": " task deleted Successfully"}