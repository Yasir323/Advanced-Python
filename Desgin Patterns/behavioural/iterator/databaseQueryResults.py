def execute_query(query):
    return


class DatabaseQueryResult:
    def __init__(self, query):
        self.query = query
        self.cursor = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor is None:
            self.cursor = execute_query(self.query)
        record = self.cursor.fetchone()
        if not record:
            self.cursor.close()
            raise StopIteration
        return record


# Usage
query_result = DatabaseQueryResult('SELECT * FROM employees')

for record in query_result:
    print(record)
