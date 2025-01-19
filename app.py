from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app
app = Flask(__name__)

# Set up the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/library.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, to turn off the warning

# Initialize SQLAlchemy
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)
