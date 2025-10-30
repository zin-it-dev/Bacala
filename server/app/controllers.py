from flask import request, flash, redirect, url_for, jsonify
from flask_login import login_user

from .repositories import UserRepository, CategoryRepository
from .models import Role
from .utils import generate_color


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


def barchart_json():
    results = CategoryRepository().stats_amount_books_by_cate()

    datasets = []
    bgColors = [generate_color() for _ in results]
    labels, data = [item[1] for item in results], [item[2] for item in results]

    datasets.append({"label": "Amount", "data": data, "backgroundColor": bgColors})

    return jsonify({"labels": labels, "datasets": datasets})
