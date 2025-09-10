from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView as BaseModelView
from flask_admin.form import SecureForm

from .models import User, Category, Book, Author
from .extensions import db


class ModelView(BaseModelView):
    column_list = ['active', 'date_created', 'date_updated']
    form_base_class = SecureForm
    column_filters = ['active']
    can_view_details = True
    can_export = True
    create_modal = True
    edit_modal = True


class UserModelView(ModelView):
    column_list = ['username'] + ModelView.column_list
    column_exclude_list = ['password']
    

class CategoryModelView(ModelView):
    column_list = ['name'] + ModelView.column_list

    
class AuthorModelView(ModelView):
    column_list = ['name'] + ModelView.column_list
    
    
class BookModelView(ModelView):
    column_list = ['name', 'category'] + ModelView.column_list
    
    
manager = Admin(name='Readify 🔖', template_mode='bootstrap4')

manager.add_view(UserModelView(User, db.session, category="Management"))
manager.add_view(CategoryModelView(Category, db.session, category="Management"))
manager.add_view(AuthorModelView(Author, db.session, category="Management"))
manager.add_view(BookModelView(Book, db.session, category="Management"))