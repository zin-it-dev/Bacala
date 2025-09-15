import click, re

from flask.cli import with_appcontext

from config import Config
from .repositories import UserRepository, CategoryRepository
from .models import Role
from .utils import load_json

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
    
    new_superuser = repo.create_user(username, email, password, role=Role.ADMIN)
    click.echo(click.style(f"Superuser {new_superuser.username} created successfully!", fg="green"))


@click.command("seed")
@with_appcontext
def seed_db():
    click.echo(click.style("Seeding database...", fg="blue"))
    
    categories = load_json("category")
    
    for cate in categories:
        CategoryRepository().create(name=cate["name"])
    
    click.echo(click.style("Seeded database successfully!", fg="green"))