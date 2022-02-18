# app/routes

from itertools import product
from flask import render_template
from run import app

@app.route("/")
def index():
    return render_template("app/index.html")

@app.route("/products")
def app_products():
    from models import Products
    products=Products.query.all()
    return render_template("app/products.html",products=products)