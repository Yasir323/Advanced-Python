"""Suppose you are developing a database abstraction layer that can work with different database management systems (
e.g., MySQL, PostgreSQL, SQLite) while providing a unified API. By utilizing the Bridge pattern, you can separate the
database abstraction layer from the specific database implementations, allowing you to switch between different
databases without modifying the client code. """


# Abstraction - Database Abstraction Layer
class Database:
    def __init__(self, db_implementation):
        self.db_implementation = db_implementation

    def connect(self):
        self.db_implementation.connect()

    def execute_query(self, query):
        self.db_implementation.execute_query(query)

    def disconnect(self):
        self.db_implementation.disconnect()


# Implementations - Database Implementations
class DBImplementation:
    def connect(self):
        pass

    def execute_query(self, query):
        pass

    def disconnect(self):
        pass


class MySQLDB(DBImplementation):
    def connect(self):
        print("Connected to MySQL database")

    def execute_query(self, query):
        print(f"Executing query in MySQL: {query}")

    def disconnect(self):
        print("Disconnected from MySQL database")


class PostgreSQLDB(DBImplementation):
    def connect(self):
        print("Connected to PostgreSQL database")

    def execute_query(self, query):
        print(f"Executing query in PostgreSQL: {query}")

    def disconnect(self):
        print("Disconnected from PostgreSQL database")


class SQLiteDB(DBImplementation):
    def connect(self):
        print("Connected to SQLite database")

    def execute_query(self, query):
        print(f"Executing query in SQLite: {query}")

    def disconnect(self):
        print("Disconnected from SQLite database")


# Usage
mysql_db = MySQLDB()
db = Database(mysql_db)
db.connect()
db.execute_query("SELECT * FROM users")
db.disconnect()

postgres_db = PostgreSQLDB()
db = Database(postgres_db)
db.connect()
db.execute_query("SELECT * FROM products")
db.disconnect()

sqlite_db = SQLiteDB()
db = Database(sqlite_db)
db.connect()
db.execute_query("SELECT * FROM orders")
db.disconnect()

"""In this example, the Database class represents the database abstraction layer, and the DBImplementation is the 
implementation hierarchy that provides specific implementations for different databases. By using the Bridge pattern, 
you can create a Database instance with a specific database implementation and perform database operations using a 
consistent API, regardless of the underlying database system. """
