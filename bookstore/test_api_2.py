import runpy
import unittest


class BookApiTests(unittest.TestCase):
    def setUp(self):
        namespace = runpy.run_path("backend_2\\api_2")
        self.app = namespace["app"]
        self.books = namespace["books"]
        self.initial_books = self.books[:]
        self.client = self.app.test_client()

    def tearDown(self):
        self.books[:] = self.initial_books

    def test_get_books_returns_json_inventory(self):
        response = self.client.get("/books")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), self.initial_books)

    def test_get_book_returns_matching_book(self):
        response = self.client.get("/books/2")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), self.initial_books[1])

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
