class DatabaseConnector:
    def connect(self):
        raise NotImplementedError()


class MySQLConnector(DatabaseConnector):
    def connect(self):
        print("Connecting to MySQL database...")


class PostgreSQLConnector(DatabaseConnector):
    def connect(self):
        print("Connecting to PostgreSQL database...")


class SQLiteConnector(DatabaseConnector):
    def connect(self):
        print("Connecting to SQLite database...")


class DatabaseConnectorFactory:
    """
    You can use the Factory Method pattern to create a database connector
    factory that provides different database connectors based on a given
    configuration. Each connector class can handle the specific implementation
    details for connecting to different database engines (e.g., MySQL, PostgreSQL,
    SQLite).
    """
    @staticmethod
    def create_connector(db_type):
        if db_type == 'mysql':
            return MySQLConnector()
        elif db_type == 'postgresql':
            return PostgreSQLConnector()
        elif db_type == 'sqlite':
            return SQLiteConnector()
        else:
            raise ValueError("Invalid database type")


# Usage
factory = DatabaseConnectorFactory()
connector = factory.create_connector('mysql')
connector.connect()
