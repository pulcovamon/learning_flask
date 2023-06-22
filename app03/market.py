'''
I am using this tutorial:
https://www.youtube.com/watch?v=Qr4QMBUPxWo
'''

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

db = SQLAlchemy(app)

class Item(db.Model):
    identifier = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=9), nullable=False, unique=True)
    description = db.Column(db.String(1024), nullable=False, unique=True)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '123456789', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '321654987', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '987654321', 'price': 150}
    ]
    return render_template('market.html', items=items)