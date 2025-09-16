from flask import request, flash, redirect, url_for, jsonify
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


def linechart_json():
    labels = ["January", "February", "March", "April", "May", "June", "July"]
    providers = ["Central", "Eastside", "Westside"]
    data = [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]
    
    datasets = []
    colors = ["rgba(75, 192, 192, 0.6)", "rgba(255, 99, 132, 0.6)", "rgba(54, 162, 235, 0.6)"]
    
    for i, provider in enumerate(providers):
        datasets.append({
            "label": provider,
            "data": data[i],
            "borderColor": colors[i % len(colors)],
        })
    
    return jsonify({
        "labels": labels,
        "datasets": datasets
    })