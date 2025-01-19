from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()


class Author(db.Model):
    """
    Author model representing the author of a book.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birthdate = db.Column(db.String(10))
    date_of_death = db.Column(db.String(10))

    # One-to-many relationship: One author can have many books
    books = db.relationship('Book', backref='author', lazy=True)

    def __repr__(self):
        return f'<Author {self.name}>'


class Book(db.Model):
    """
    Book model representing a book in the library.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    cover_image = db.Column(db.String(255))  # Path to the book cover image
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __repr__(self):
        return f'<Book {self.title} by {self.author.name}>'
