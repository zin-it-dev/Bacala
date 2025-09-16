import os.path as op

from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView as BaseModelView
from flask_admin.form import SecureForm
from flask_admin.actions import action
from flask_admin.contrib.fileadmin import FileAdmin
from flask_login import current_user, logout_user
from flask import redirect, url_for
from werkzeug.security import generate_password_hash

from .models import User, Category, Book, Author, Role, Tag
from .extensions import db
from .actions import change_active
from .decorators import admin_required
from .widgets import CKTextAreaField

path = op.join(op.dirname(__file__), 'static')


class SecureView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role.__eq__(Role.ADMIN)


class ModelView(BaseModelView, SecureView):
    column_list = ['active', 'date_created']
    form_base_class = SecureForm
    column_filters = ['active']
    column_editable_list = ["active"]
    column_sortable_list = ["date_created"]
    can_view_details = True
    can_export = True
    create_modal = True
    edit_modal = True
    
    @action(
        "change_active",
        "Change Active",
        "Are you sure you want to change the active status of selected models?",
    )
    def action_active(self, ids):
        return change_active(self=self, ids=ids)
    

class UserView(ModelView):
    column_list = ['username'] + ModelView.column_list
    column_exclude_list = ['password']
    
    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password)


class CategoryView(ModelView):
    column_list = ['name', 'books'] + ModelView.column_list
    column_editable_list = ["name"] + ModelView.column_editable_list
    
    
class AuthorView(ModelView):
    column_list = ['name'] + ModelView.column_list
    

class TagView(ModelView):
    column_list = ['name'] + ModelView.column_list
    
    
class BookView(ModelView):
    extra_js = ["//cdn.ckeditor.com/4.6.0/full-all/ckeditor.js"]
    form_overrides = {"description": CKTextAreaField}
    
    column_list = ['name', 'category'] + ModelView.column_list
    
    
class LogoutView(SecureView):
    @admin_required
    @expose("/")
    def index(self):
        logout_user()
        return redirect(url_for("admin.index"))
    
    
class FileView(FileAdmin, SecureView):
    pass
    
    
manager = Admin(name='Bacala 📚', template_mode='bootstrap4')

manager.add_view(UserView(User, db.session, category="Management"))
manager.add_view(CategoryView(Category, db.session, category="Management"))
manager.add_view(AuthorView(Author, db.session, category="Management"))
manager.add_view(TagView(Tag, db.session, category="Management"))
manager.add_view(BookView(Book, db.session, category="Management"))
manager.add_view(FileView(path, '/static/', name='Files', category="Settings", endpoint="files"))
manager.add_view(
    LogoutView(name="Log Out", category="Settings", endpoint="logout")
)