import unittest
from data_storage.blob_storage import BlobStorage
from data_storage.nosql_databases import NoSQLDatabase
from data_storage.graph_databases import GraphDatabaseManager
from config.config import Config

class TestBlobStorage(unittest.TestCase):
    def setUp(self):
        config = Config()
        self.blob_storage = BlobStorage('s3', config.blob_storage)

    def test_upload_file(self):
        result = self.blob_storage.upload_file('test_file.txt', 'test_bucket')
        self.assertIsNone(result)

    def test_download_file(self):
        result = self.blob_storage.download_file('test_bucket', 'test_file.txt', 'downloaded_test_file.txt')
        self.assertIsNone(result)

class TestNoSQLDatabase(unittest.TestCase):
    def setUp(self):
        config = Config()
        self.nosql_database = NoSQLDatabase('dynamodb', config.nosql_database)

    def test_put_item(self):
        item = {'id': {'S': '1'}, 'name': {'S': 'test_item'}}
        result = self.nosql_database.put_item('test_table', item)
        self.assertIsNone(result)

    def test_get_item(self):
        key = {'id': {'S': '1'}}
        result = self.nosql_database.get_item('test_table', key)
        self.assertIsNotNone(result)

    def test_delete_item(self):
        key = {'id': {'S': '1'}}
        result = self.nosql_database.delete_item('test_table', key)
        self.assertIsNone(result)

class TestGraphDatabaseManager(unittest.TestCase):
    def setUp(self):
        config = Config()
        self.graph_database_manager = GraphDatabaseManager(config.graph_database['uri'], config.graph_database['user'], config.graph_database['password'])

    def test_create_node(self):
        properties = {'id': '1', 'name': 'test_node'}
        result = self.graph_database_manager.create_node('TestLabel', properties)
        self.assertIsNone(result)

    def test_create_relationship(self):
        properties1 = {'id': '1', 'name': 'test_node1'}
        properties2 = {'id': '2', 'name': 'test_node2'}
        relationship_properties = {'since': '2023'}
        result = self.graph_database_manager.create_relationship('TestLabel1', properties1, 'TestLabel2', properties2, 'KNOWS', relationship_properties)
        self.assertIsNone(result)

    def test_get_node(self):
        properties = {'id': '1'}
        result = self.graph_database_manager.get_node('TestLabel', properties)
        self.assertIsNotNone(result)

    def test_delete_node(self):
        properties = {'id': '1'}
        result = self.graph_database_manager.delete_node('TestLabel', properties)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
