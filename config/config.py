class Config:
    def __init__(self):
        self.api_endpoints = {
            "base_url": "http://example.com/api",
            "timeout": 30
        }
        self.web_scraping = {
            "user_agent": "Mozilla/5.0",
            "max_retries": 3
        }
        self.kafka = {
            "bootstrap_servers": "localhost:9092",
            "topic": "data_topic"
        }
        self.batch_imports = {
            "file_path": "input_data.csv",
            "output_path": "output_data.csv"
        }
        self.data_cleansing = {
            "missing_value_strategy": "mean"
        }
        self.data_enrichment = {
            "api_url": "https://api.example.com/enrich",
            "api_key": "your_api_key"
        }
        self.blob_storage = {
            "storage_type": "s3",
            "aws_access_key_id": "your_access_key",
            "aws_secret_access_key": "your_secret_key",
            "region_name": "your_region"
        }
        self.nosql_database = {
            "db_type": "dynamodb",
            "aws_access_key_id": "your_access_key",
            "aws_secret_access_key": "your_secret_key",
            "region_name": "your_region"
        }
        self.graph_database = {
            "uri": "bolt://localhost:7687",
            "user": "neo4j",
            "password": "password"
        }
        self.analytics = {
            "data_source": "sample_data_source"
        }
        self.microservices = {
            "dockerfile_path": ".",
            "image_tag": "your_image_tag"
        }
        self.serverless = {
            "bucket_name": "your-bucket-name"
        }
        self.api_gateway = {
            "graphql_endpoint": "/graphql"
        }
