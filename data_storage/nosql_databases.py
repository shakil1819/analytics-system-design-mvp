import boto3
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

class NoSQLDatabase:
    def __init__(self, db_type, config):
        self.db_type = db_type
        self.config = config
        if db_type == 'dynamodb':
            self.client = boto3.client(
                'dynamodb',
                aws_access_key_id=config['aws_access_key_id'],
                aws_secret_access_key=config['aws_secret_access_key'],
                region_name=config['region_name']
            )
        elif db_type == 'elasticsearch':
            awsauth = AWS4Auth(
                config['aws_access_key_id'],
                config['aws_secret_access_key'],
                config['region_name'],
                'es'
            )
            self.client = Elasticsearch(
                hosts=[{'host': config['host'], 'port': config['port']}],
                http_auth=awsauth,
                use_ssl=True,
                verify_certs=True,
                connection_class=RequestsHttpConnection
            )
        else:
            raise ValueError("Unsupported database type")

    def put_item(self, table_name, item):
        if self.db_type == 'dynamodb':
            self.client.put_item(TableName=table_name, Item=item)
        elif self.db_type == 'elasticsearch':
            self.client.index(index=table_name, body=item)

    def get_item(self, table_name, key):
        if self.db_type == 'dynamodb':
            response = self.client.get_item(TableName=table_name, Key=key)
            return response.get('Item')
        elif self.db_type == 'elasticsearch':
            response = self.client.get(index=table_name, id=key)
            return response.get('_source')

    def delete_item(self, table_name, key):
        if self.db_type == 'dynamodb':
            self.client.delete_item(TableName=table_name, Key=key)
        elif self.db_type == 'elasticsearch':
            self.client.delete(index=table_name, id=key)
