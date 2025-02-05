from neo4j import GraphDatabase

class GraphDatabaseManager:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_node(self, label, properties):
        with self.driver.session() as session:
            session.write_transaction(self._create_node, label, properties)

    @staticmethod
    def _create_node(tx, label, properties):
        query = f"CREATE (n:{label} {{"
        query += ", ".join([f"{key}: ${key}" for key in properties.keys()])
        query += "})"
        tx.run(query, **properties)

    def create_relationship(self, label1, properties1, label2, properties2, relationship_type, relationship_properties):
        with self.driver.session() as session:
            session.write_transaction(self._create_relationship, label1, properties1, label2, properties2, relationship_type, relationship_properties)

    @staticmethod
    def _create_relationship(tx, label1, properties1, label2, properties2, relationship_type, relationship_properties):
        query = f"MATCH (a:{label1} {{"
        query += ", ".join([f"{key}: ${key}1" for key in properties1.keys()])
        query += f"}}), (b:{label2} {{"
        query += ", ".join([f"{key}: ${key}2" for key in properties2.keys()])
        query += f"}}) CREATE (a)-[r:{relationship_type} {{"
        query += ", ".join([f"{key}: ${key}" for key in relationship_properties.keys()])
        query += "}}]->(b)"
        params = {f"{key}1": value for key, value in properties1.items()}
        params.update({f"{key}2": value for key, value in properties2.items()})
        params.update(relationship_properties)
        tx.run(query, **params)

    def get_node(self, label, properties):
        with self.driver.session() as session:
            result = session.read_transaction(self._get_node, label, properties)
            return result.single()

    @staticmethod
    def _get_node(tx, label, properties):
        query = f"MATCH (n:{label} {{"
        query += ", ".join([f"{key}: ${key}" for key in properties.keys()])
        query += "}}) RETURN n"
        result = tx.run(query, **properties)
        return result

    def delete_node(self, label, properties):
        with self.driver.session() as session:
            session.write_transaction(self._delete_node, label, properties)

    @staticmethod
    def _delete_node(tx, label, properties):
        query = f"MATCH (n:{label} {{"
        query += ", ".join([f"{key}: ${key}" for key in properties.keys()])
        query += "}}) DETACH DELETE n"
        tx.run(query, **properties)
