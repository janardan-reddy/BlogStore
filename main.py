from fastapi import FastAPI
from application.routers import blog_router

app = FastAPI()
app.include_router(blog_router.router)

@app.get('/')
def index():
    return {
        'status': 'success',
        'message': 'server is up and running'
    }