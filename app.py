from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up secret key for session management
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Set up database URI (adjust the path as needed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    genre = db.Column(db.String(100))
    published_year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    author = db.relationship('Author', backref=db.backref('books', lazy=True))

# Define the Author model
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Create tables
with app.app_context():
    db.create_all()

# Home route - Display all books
@app.route('/')
def home():
    books = Book.query.all()  # Get all books
    return render_template('home.html', books=books)

# Add a new book
@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        published_year = request.form['published_year']
        author_name = request.form['author_name']

        author = Author.query.filter_by(name=author_name).first()
        if not author:
            author = Author(name=author_name)
            db.session.add(author)
            db.session.commit()

        book = Book(title=title, genre=genre, published_year=published_year, author=author)
        db.session.add(book)
        db.session.commit()

        flash(f'Book "{title}" added successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('add_book.html')

# View details of a specific book
@app.route('/book/<int:book_id>')
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book_detail.html', book=book)

# View details of a specific author and list their books
@app.route('/author/<int:author_id>')
def author_detail(author_id):
    author = Author.query.get_or_404(author_id)
    books_by_author = Book.query.filter_by(author_id=author_id).all()
    return render_template('author_detail.html', author=author, books=books_by_author)

# Delete a book
@app.route('/book/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    author_id = book.author_id
    db.session.delete(book)
    db.session.commit()

    # Check if the author has other books, and delete the author if not
    if not Book.query.filter_by(author_id=author_id).first():
        author = Author.query.get_or_404(author_id)
        db.session.delete(author)
        db.session.commit()

    flash(f'Book "{book.title}" deleted successfully!', 'success')
    return redirect(url_for('home'))

# Search for books by keyword
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        keyword = request.form['keyword']
        books = Book.query.filter(Book.title.ilike(f'%{keyword}%')).all()
        if not books:
            flash('No books found with that keyword!', 'danger')
        return render_template('home.html', books=books)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
