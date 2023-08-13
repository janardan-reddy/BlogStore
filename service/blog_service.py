from application.schemas.requests.blog_request import BlogRequest
from sqlalchemy.orm import Session
from database import models
from database import blog_database

def getAllBlogs(db:Session):
    result= blog_database.getAllBlogs(db)
    return result

def getBlogById(id: str, db:Session):
    result= blog_database.getBlogById(id, db)
    return result

def addBlog(request: BlogRequest, db:Session):
    new_blog= models.DBBlog(
        **request
    )
    result= blog_database.addBlog(new_blog, db)
    return result

def updateBlog(id: str, request: BlogRequest, db:Session):
    new_blog= models.DBBlog(
        **request
    )
    result= blog_database.updateBlog(id, new_blog, db)
    return result

def deleteBlog(id: str, db:Session):
    result= blog_database.deleteBlog(id, db)
    return result