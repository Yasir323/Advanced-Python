from concurrent.futures import thread
import threading
import pyodbc
import time

thread_local = threading.local()


class ThreadWithReturnValue(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)

        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        threading.Thread.join(self)
        return self._return


def get_connection(databse: str, server: str = '107.6.175.250', username: str = 'sh!v@n!@gg@rw@1',
                   password: str = 'Y.c^jq#tv9g6y+#EhK=5#TQ') -> pyodbc.Connection:
    if not hasattr(thread_local, 'connection'):
        thread_local.connection = pyodbc.connect(
            DRIVER=pyodbc.drivers()[-1],
            SERVER=server,
            DATABASE=databse,
            UID=username,
            PWD=password,
            MARS_Connection='yes',
            timeout=3
        )
    return thread_local.connection


def get_data(database: str, table: str, columns: list):
    ts = time.perf_counter()
    conn = get_connection(database)
    print(time.perf_counter() - ts)
    cols = ''
    for col in columns[:-1]:
        cols += col
        cols += ', '
    cols += columns[-1]
    with conn.cursor() as cur:
        query = f"SELECT {cols} from {database}..{table};"
        cur.execute(query)
        data = cur.fetchall()
    conn.close()
    return data


if __name__ == '__main__':
    threads = []
    databases = ['gps', 'theBoons']
    tables = ['tolls_new', 'tollNameDataUpdated']
    columns = [
        ['tollid', 'name', 'latitude', 'longitude'],
        ['merchantId', 'merchantName', 'latitude', 'longitude']
    ]
    for index, database in enumerate(databases):
        print(f"Main    : create and start thread {index}.")
        t = ThreadWithReturnValue(target=get_data, args=(database, tables[index], columns[index]))
        threads.append(t)
        t.start()

    for index, t in enumerate(threads):
        print(f"Main    : before joining thread {index}")
        print(t.join())
        print(f"Main    : thread {index} done.")
