import unittest

import api


class BookApiTests(unittest.TestCase):
    def setUp(self):
        self.original_books = api.books[:]
        api.books[:] = [
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
        self.client = api.app.test_client()

    def tearDown(self):
        api.books[:] = self.original_books

    def test_get_books_returns_json_inventory(self):
        response = self.client.get("/books")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), api.books)

    def test_get_book_returns_matching_book(self):
        response = self.client.get("/books/2")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            {
                "id": 2,
                "title": "Pride and Prejudice",
                "author": "Jane Austen",
                "price": 9.99,
            },
        )

    def test_get_missing_book_returns_json_404(self):
        response = self.client.get("/books/999")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {"error": "Book not found."})

    def test_post_book_adds_valid_book(self):
        response = self.client.post(
            "/books",
            json={"title": "Dune", "author": "Frank Herbert", "price": 12.5},
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.get_json(),
            {
                "id": 3,
                "title": "Dune",
                "author": "Frank Herbert",
                "price": 12.5,
            },
        )
        self.assertEqual(len(self.client.get("/books").get_json()), 3)

    def test_post_book_rejects_negative_price(self):
        response = self.client.post(
            "/books",
            json={"title": "Dune", "author": "Frank Herbert", "price": -1},
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.get_json(),
            {"error": "Price must be a non-negative number."},
        )


if __name__ == "__main__":
    unittest.main()
