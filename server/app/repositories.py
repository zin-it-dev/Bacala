from flask_sqlalchemy.model import Model

from .models import Category, User, Book

class BaseRepository:
    def __init__(self, model: Model):
        self.model = model
        
    def get_all(self):
        return self.model.query.filter_by(active=True).all()
    
    def get_by_id(self, id):
        return self.model.query.filter_by(id=id).first()
    
    def is_exists(self, **kwargs):
        return self.model.query.filter_by(**kwargs).first() is not None
    
    def create(self, **kwargs):
        instance = self.model(**kwargs)
        instance.save()
    
    
class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)
        
    def create_user(self, username, email, password, **kwargs):
        user = self.model(username=username, email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def check_login(self, email, password):
        user = self.model.query.filter_by(email=email).first()
        return user if user and user.check_password(password=password) else None
    
    
class CategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(Category)
        
        
class BookRepository(BaseRepository):
    def __init__(self):
        super().__init__(Book)
        
    def get_all(self, page=1, page_size=None):
        queries = self.model.query.filter(self.model.active.__eq__(True))
        
        paginator = queries.paginate(page=page, per_page=page_size)
        
        return dict(
            results=paginator.items,
            count=paginator.total,
            page_size=paginator.per_page,
        )