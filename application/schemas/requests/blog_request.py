from pydantic import BaseModel

class BlogRequest(BaseModel):
    title: str
    description: str
    author: str
    category: str