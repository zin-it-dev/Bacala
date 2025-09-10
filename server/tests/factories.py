import factory

from app.extensions import db
from app.models import Category

class CategoryFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Category
        sqlalchemy_session = db.session

    name = factory.Faker('name')