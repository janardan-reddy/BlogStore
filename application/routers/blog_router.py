from fastapi import APIRouter,Depends,status
from application.schemas.requests.blog_request import BlogRequest
from application.schemas.responses.blog_response import BlogResponse
from sqlalchemy.orm import Session
from database.database import get_db
from typing import List
from service import blog_service

router= APIRouter(
    prefix= '/blog',
    tags= ['blog']
)

@router.get('', status_code= status.HTTP_200_OK, response_model= List[BlogResponse])
def getBlog(db:Session= Depends(get_db)):
    result= blog_service.getAllBlogs(db)
    return result

@router.get('/{id}', status_code= status.HTTP_200_OK, response_model= BlogResponse)
def getBlog(id: str, db:Session= Depends(get_db)):
    result= blog_service.getBlogById(id, db)
    return result

@router.post('/add', status_code= status.HTTP_201_CREATED, response_model= BlogResponse)
def addBlog(request: BlogRequest, db:Session= Depends(get_db)):
    result= blog_service.addBlog(request, db)
    return result

@router.put('/update/{id}', status_code= status.HTTP_200_OK)
def updateBlog(id: str, request: BlogRequest, db:Session= Depends(get_db)):
    result= blog_service.updateBlog(id, request, db)
    return result

@router.delete('/delete/{id}', status_code= status.HTTP_204_NO_CONTENT)
def deleteBlog(id: str, db:Session= Depends(get_db)):
    result= blog_service.deleteBlog(id, db)
    return result