from flask import request, flash, redirect, url_for
from flask_login import login_user

from .repositories import UserRepository
from .models import Role


def login():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = request.form.get("remember")

    user = UserRepository().check_login(email=email, password=password)

    if user and user.role.__eq__(Role.ADMIN):
        login_user(user, remember=remember)
        flash("Welcome, admin! You are successfully logged in.", "success")
    else:
        flash("Invalid email or password. Please try again.", "warning")

    return redirect(url_for("admin.index"))