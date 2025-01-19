# Book Library App

Welcome to the **Book Library App**! This is a simple web application built with Flask and SQLAlchemy, designed to allow users to manage a digital book library. You can add, search, view, and delete books from your collection.

## Features 
- **Add New Books**: You can add books to your library with details like title, author, and publication year.
- **Search Books**: Search for books by title or author name.
- **View Book Details**: View detailed information about each book in your library.
- **Delete Books**: Easily delete books from your library.
- **Author Management**: Automatically removes authors if they have no more books in the library.

## Technologies Used
- **Flask**: Python web framework for routing and rendering views.
- **SQLAlchemy**: ORM for interacting with the database.
- **SQLite**: Lightweight database used for storage.
- **HTML/CSS**: For structuring and styling the user interface.


## Setup & Installation

To run the **Book Library App** locally, follow these steps:

###

```bash
git clone https://github.com/MoeManius/BookAlchemy.git
cd book-library

2. Set Up the Virtual Environment
Create a virtual environment and activate it:

On Windows:
bash
python -m venv .venv
.venv\Scripts\activate

On macOS/Linux:
python3 -m venv .venv
source .venv/bin/activate

3. Install Dependencies
Install all the required packages using pip:
bash
pip install -r requirements.txt

4. Run the Application
Once everything is set up, run the app:
bash
python app.py
By default, the application will be hosted at http://127.0.0.1:5000/.

How to Use the App
Add a New Book:

Click the "Add New Book" button on the homepage.
Fill in the details like book title, author, and year of publication.
Submit the form to add the book to the library.

Search for a Book:
Use the search bar on the homepage to find books by title or author.
The list of books will be filtered based on the search query.
View Book Details:

Click on a book title from the homepage to view more detailed information about that book.
Delete a Book:

From the homepage, you can delete a book by clicking the "Delete" button next to the book.