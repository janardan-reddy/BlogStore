from database.models import DBBlog
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

def getAllBlogs(db:Session):
    result= db.query(DBBlog).all()
    return result

def getBlogById(id: str, db:Session):
    result= db.query(DBBlog).filter(DBBlog.id == id).first()
    if result != None:
        return result
    else:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "requested blog doesn't exist"
        )

def addBlog(request: DBBlog, db:Session):
    db.add(request)
    db.commit()
    db.refresh(request)
    return request

def updateBlog(id:str, request: DBBlog, db:Session):
    result= getBlogById(id, db)
    result.update(request)
    db.commit()
    result= getBlogById(id, db)
    return result

def deleteBlog(id: str, db:Session):
    result= getBlogById(id, db)
    result.delete()
    db.commit()

