from database.database import Base
from sqlalchemy import Column, Integer, String

class DBBlog(Base):
    __tablename__= 'blog'
    id= Column(Integer, primary_key= True, index= True)
    author= Column(String)
    title= Column(String)
    description= Column(String)
    category= Column(String)