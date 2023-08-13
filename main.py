from fastapi import FastAPI
from application.routers import blog_router
from database import models
from database.database import engine

app = FastAPI()
app.include_router(blog_router.router)
models.Base.metadata.create_all(engine)


@app.get('/')
def index():
    return {
        'status': 'success',
        'message': 'server is up and running'
    }