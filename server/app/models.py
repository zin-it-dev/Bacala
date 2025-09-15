import enum

from sqlalchemy import Column, String, Text, Float, Integer, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from .extensions import db
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
    name = Column(String(80), unique=True, nullable=False)
    
    books = relationship('Book', backref='category', lazy=True)
    
    def __str__(self):
        return self.name
    
    
book_author = db.Table(
    'book_author',
    Column('book_id', Integer, ForeignKey('book.id'), primary_key=True),
    Column('author_id', Integer, ForeignKey('author.id'), primary_key=True)
)
    

book_tag = db.Table('book_tag',
    Column('book_id', Integer, ForeignKey('book.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True)
)


class Tag(ModelMixin):
    name = Column(String(50), unique=True)

    def __repr__(self):
        return f'<Tag "{self.name}">' 
    
    
class Author(ModelMixin):
    name = Column(String(80), unique=True)
    
    def __str__(self):
        return self.name


class Book(ModelMixin):
    name = Column(String(120), unique=True)
    description = Column(Text)
    price = Column(Float, default=0.00)
    
    category_id = Column(Integer, ForeignKey(Category.id))
    authors = relationship(Author, secondary=book_author, backref='books')
    tags = relationship(Tag, secondary=book_tag, backref='books')
    
    def __str__(self):
        return self.name