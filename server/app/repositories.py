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
        
    def create_user(self, username, email, password, **kwargs):
        user = User(username=username, email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def check_login(self, email, password):
        user = User.query.filter(User.email.__eq__(email)).first()
        return user if user and user.check_password(password=password) else None
    
    
class CategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(Category)