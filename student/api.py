import math

from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        "id": 1,
        "title": "The Hobbit",
        "author": "J. R. R. Tolkien",
        "price": 14.99,
    },
    {
        "id": 2,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "price": 9.99,
    },
]

students = [
    {
        "id": 1,
        "name": "Jordan Lee",
        "email": "jordan.lee@example.com",
        "course": "Computer Science",
    }
]


@app.get("/books")
def get_books():
    return jsonify(books)


@app.get("/books/<int:book_id>")
def get_book(book_id):
    book = next((item for item in books if item["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found."}), 404
    return jsonify(book)


@app.post("/books")
def add_book():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object."}), 400

    title = data.get("title")
    author = data.get("author")
    price = data.get("price")
    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "A non-empty title is required."}), 400
    if not isinstance(author, str) or not author.strip():
        return jsonify({"error": "A non-empty author is required."}), 400
    if (
        isinstance(price, bool)
        or not isinstance(price, (int, float))
        or (isinstance(price, float) and not math.isfinite(price))
        or price < 0
    ):
        return jsonify({"error": "Price must be a non-negative number."}), 400

    book = {
        "id": max((item["id"] for item in books), default=0) + 1,
        "title": title.strip(),
        "author": author.strip(),
        "price": price,
    }
    books.append(book)
    return jsonify(book), 201


@app.get("/students")
def get_students():
    return jsonify(students)


@app.post("/students")
def add_student():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object."}), 400

    name = data.get("name")
    email = data.get("email")
    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "A non-empty name is required."}), 400
    if not isinstance(email, str) or not email.strip():
        return jsonify({"error": "A non-empty email is required."}), 400

    course = data.get("course", "")
    if not isinstance(course, str):
        return jsonify({"error": "Course must be a string."}), 400

    student = {
        "id": max((item["id"] for item in students), default=0) + 1,
        "name": name.strip(),
        "email": email.strip(),
        "course": course.strip(),
    }
    students.append(student)
    return jsonify(student), 201


if __name__ == "__main__":
    app.run()