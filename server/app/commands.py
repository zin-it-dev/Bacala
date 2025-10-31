import click, re

from flask.cli import with_appcontext

from config import Config
from .repositories import UserRepository, CategoryRepository, BookRepository
from .models import Role
from .utils import load_json, password_validator

@click.command("createsuperuser")
@click.argument("email")
@click.argument("username")
def create_superuser(email, username):
    repo = UserRepository()
    
    if not re.match(Config.EMAIL_REGEX, email):
        click.echo(click.style("Email is invalid! Please try again.", fg="red"))
        return
    
    if repo.is_exists(email=email):
        click.echo(click.style("Email is exists! Please try again.", fg="red"))
        return
    
    if repo.is_exists(username=username):
        click.echo(click.style("Username is exists! Please try again.", fg="red"))
        return
    
    password = click.prompt("Password", hide_input=True, confirmation_prompt=True)
    
    if password_validator(password):
        new_superuser = repo.create_user(username, email, password, role=Role.ADMIN)
        click.echo(click.style(f"Superuser {new_superuser.username} created successfully!", fg="green"))
    else:
        click.echo(click.style("Password is invalid! Please try again.", fg="red"))
        return

@click.command("seed")
@with_appcontext
def seed_db():
    click.echo(click.style("Seeding database...", fg="blue"))
    
    categories = load_json("categories")
    books = load_json('books')
    
    for cate in categories:
        CategoryRepository().create(name=cate["name"])
        
    for book in books:
        BookRepository().create(
            name=book['name'],
            description=book['description'],
            price=book['price'],
            category_id=book['category']
        )
    
    click.echo(click.style("Seeded database successfully!", fg="green"))