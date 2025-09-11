import enum

from sqlalchemy import Column, String, Text, Float, Integer, ForeignKey, Enum as SQLEnum 
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from .mixins import ModelMixin


class Role(enum.Enum):
    USER = 'User'
    ADMIN = 'Admin'


class User(ModelMixin, UserMixin):
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(255))
    role = Column(SQLEnum(Role), default=Role.USER)
    
    def __str__(self):
        return self.username
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Category(ModelMixin):
    name = Column(String(80), unique=True)
    
    books = relationship('Book', backref='category',lazy=True)
    
    def __str__(self):
        return self.name
    
    
class Author(ModelMixin):
    name = Column(String(80), unique=True)
    
    def __str__(self):
        return self.name
    

class Book(ModelMixin):
    name = Column(String(120), unique=True)
    description = Column(Text)
    price = Column(Float, default=0.00)
    
    category_id = Column(Integer, ForeignKey(Category.id))
    
    def __str__(self):
        return self.name