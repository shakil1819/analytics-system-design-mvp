import unittest
from scalability_enhancements.microservices_architecture import deploy_microservice, build_image
from scalability_enhancements.distributed_processing import process_data
from scalability_enhancements.serverless_functions import lambda_handler
from scalability_enhancements.api_gateway import app as graphql_app

class TestMicroservicesArchitecture(unittest.TestCase):
    def test_deploy_microservice(self):
        response = deploy_microservice("test_image", "test_service", 1)
        self.assertIn("message", response)
        self.assertEqual(response["message"], "Microservice deployed successfully")

    def test_build_image(self):
        response = build_image(".", "test_image_tag")
        self.assertIn("message", response)
        self.assertEqual(response["message"], "Docker image built successfully")

class TestDistributedProcessing(unittest.TestCase):
    def test_process_data(self):
        input_path = "tests/data/input_data.csv"
        output_path = "tests/data/output_data.csv"
        process_data(input_path, output_path)
        # Add assertions to verify the output data

class TestServerlessFunctions(unittest.TestCase):
    def test_lambda_handler(self):
        event = {"data": {"key": "value"}}
        context = {}
        response = lambda_handler(event, context)
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('body', response)
        self.assertEqual(response['body'], '"Data processed successfully"')

class TestApiGateway(unittest.TestCase):
    def test_graphql_endpoint(self):
        client = graphql_app.test_client()
        response = client.post("/graphql", json={"query": "{ hello }"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("data", response.json())
        self.assertEqual(response.json()["data"]["hello"], "Hello, world!")

if __name__ == "__main__":
    unittest.main()
