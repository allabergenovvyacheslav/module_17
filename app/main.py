from fastapi import FastAPI
from routers import task, user

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})


@app.get('/')
async def wellcome():
    return {"message": "Welcome to Taskmanager"}

об
app.include_router(task.router)
app.include_router(user.router)