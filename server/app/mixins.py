from sqlalchemy import Column, Integer, Boolean, DateTime
from datetime import datetime

from .extensions import db

class ModelMixin(db.Model):
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(Boolean, default=True)
    date_created = Column(DateTime, default=datetime.now())
    date_updated = Column(DateTime, default=datetime.now())
    
    def save(self):
        db.session.add(self)
        db.session.commit()