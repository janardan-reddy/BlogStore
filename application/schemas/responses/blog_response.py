from pydantic import BaseModel

class BlogResponse(BaseModel):
    id: str
    title: str
    