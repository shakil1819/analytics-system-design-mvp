import unittest
from fastapi.testclient import TestClient
from main import app, main

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_collect_data(self):
        response = self.client.get("/collect_data")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Data collection endpoint"})

    def test_scrape_data(self):
        response = self.client.get("/scrape_data")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Web scraping endpoint"})

    def test_stream_data(self):
        response = self.client.get("/stream_data")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Streaming ingestion endpoint"})

    def test_batch_import(self):
        response = self.client.get("/batch_import")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Batch data import endpoint"})

    def test_main_function(self):
        try:
            main()
        except Exception as e:
            self.fail(f"main() raised Exception unexpectedly: {e}")

if __name__ == "__main__":
    unittest.main()
