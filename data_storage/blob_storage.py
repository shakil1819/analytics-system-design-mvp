import boto3
from minio import Minio
from botocore.exceptions import NoCredentialsError

class BlobStorage:
    def __init__(self, storage_type, config):
        self.storage_type = storage_type
        self.config = config
        if storage_type == 's3':
            self.client = boto3.client(
                's3',
                aws_access_key_id=config['aws_access_key_id'],
                aws_secret_access_key=config['aws_secret_access_key'],
                region_name=config['region_name']
            )
        elif storage_type == 'minio':
            self.client = Minio(
                config['endpoint'],
                access_key=config['access_key'],
                secret_key=config['secret_key'],
                secure=config['secure']
            )
        else:
            raise ValueError("Unsupported storage type")

    def upload_file(self, file_name, bucket, object_name=None):
        if self.storage_type == 's3':
            try:
                self.client.upload_file(file_name, bucket, object_name or file_name)
                print(f"File {file_name} uploaded to S3 bucket {bucket}")
            except NoCredentialsError:
                print("Credentials not available")
        elif self.storage_type == 'minio':
            try:
                self.client.fput_object(bucket, object_name or file_name, file_name)
                print(f"File {file_name} uploaded to Minio bucket {bucket}")
            except Exception as e:
                print(f"Error occurred: {e}")

    def download_file(self, bucket, object_name, file_name):
        if self.storage_type == 's3':
            try:
                self.client.download_file(bucket, object_name, file_name)
                print(f"File {file_name} downloaded from S3 bucket {bucket}")
            except NoCredentialsError:
                print("Credentials not available")
        elif self.storage_type == 'minio':
            try:
                self.client.fget_object(bucket, object_name, file_name)
                print(f"File {file_name} downloaded from Minio bucket {bucket}")
            except Exception as e:
                print(f"Error occurred: {e}")
