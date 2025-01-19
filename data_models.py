from flask_sqlalchemy import SQLAlchemy

# Initialize the db object
db = SQLAlchemy()


# Define the Author model
class Author(db.Model):
    # Define the table name (optional, it defaults to class name lowercased)
    __tablename__ = 'authors'

    # Define the columns and their properties
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=True)
    date_of_death = db.Column(db.Date, nullable=True)

    # Custom string representation of the Author instance
    def __repr__(self):
        return f'<Author {self.name}>'

    def __str__(self):
        return f'Author: {self.name}, Born: {self.birth_date}, Died: {self.date_of_death if self.date_of_death else "N/A"}'


# Define the Book model
class Book(db.Model):
    # Define the table name (optional)
    __tablename__ = 'books'

    # Define the columns and their properties
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    publication_year = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)  # Foreign Key linking to Author

    # Establish a relationship with the Author model
    author = db.relationship('Author', backref=db.backref('books', lazy=True))

    # Custom string representation of the Book instance
    def __repr__(self):
        return f'<Book {self.title}>'

    def __str__(self):
        return f'Book: {self.title}, ISBN: {self.isbn}, Published: {self.publication_year}, Author: {self.author.name}'
