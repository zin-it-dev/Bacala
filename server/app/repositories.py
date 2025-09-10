from flask_sqlalchemy.model import Model

from .models import Category, User

class BaseRepository:
    def __init__(self, model: Model):
        self.model = model
        
    def get_all(self):
        return self.model.query.filter_by(active=True).all()
    
    def get_by_id(self, id):
        return self.model.query.filter_by(id=id).first()
    
    
class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)
    
    
class CategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(Category)