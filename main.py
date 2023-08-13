from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {
        'status': 'success',
        'message': 'server is up and running'
    }