# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app
app = Flask(__name__)

# Configure the URI for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/library.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, to turn off the warning

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Import data models (to be created later)
from data_models import db, Author, Book

# Initialize the app with db
db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
