from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from data_models import db, Author, Book  # Import Author, Book models and db object

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/library.sqlite'
app.config['SECRET_KEY'] = 'your-secret-key'  # For flash messages

db.init_app(app)


@app.route('/')
def index():
    return "Welcome to the Digital Library!"


# Route to add an author
@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        name = request.form['name']
        birth_date = request.form['birth_date']
        date_of_death = request.form['date_of_death']

        new_author = Author(name=name, birth_date=birth_date, date_of_death=date_of_death)

        try:
            db.session.add(new_author)
            db.session.commit()
            flash('Author added successfully!', 'success')
            return redirect(url_for('add_author'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding author: {str(e)}', 'danger')
            return redirect(url_for('add_author'))

    return render_template('add_author.html')


# Route to add a book
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        isbn = request.form['isbn']
        publication_year = request.form['publication_year']
        author_id = request.form['author_id']

        new_book = Book(title=title, isbn=isbn, publication_year=publication_year, author_id=author_id)

        try:
            db.session.add(new_book)
            db.session.commit()
            flash('Book added successfully!', 'success')
            return redirect(url_for('add_book'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding book: {str(e)}', 'danger')
            return redirect(url_for('add_book'))

    # Get the list of authors for the dropdown
    authors = Author.query.all()
    return render_template('add_book.html', authors=authors)


if __name__ == '__main__':
    app.run(debug=True)
