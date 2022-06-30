import argparse

parser = argparse.ArgumentParser(description="Make a skeleton script.")

# Positional Args
parser.add_argument(
    'parent_directory',
    default='python_scripts',
    help='Name of the parent directory where the script will be stored.'
)
parser.add_argument(
    'script_name',
    help='Name of the script.'
)

# Optional Args
parser.add_argument(
    '-l',
    '--logs',
    help='Whether to use a logging mechanism.',
    action='store_true'
)

parser.add_argument(
    '-s',
    '--sql',
    help='Whether to connect to SQL Server.',
    action='store_true'
)

parser.add_argument(
    '-r',
    '--redis',
    help='Whether to connect to Redis.',
    action='store_true'
)

parser.add_argument(
    '-m',
    '--mongo',
    help='Whether to connect to MongoDB.',
    action='store_true'
)

parser.add_argument(
    '-c',
    '--cron',
    help='Whether to stamp in cronjobs.',
    action='store_true'
)

args = parser.parse_args()

"""
import os
import json
import time
import logging
import datetime
from functools import wraps
from typing import Optional, List, Tuple
import redis
import pyodbc

# Configure Logger
cwd = os.getcwd()
PARENT_DIR = '{}'
SCRIPT_NAME = '{}'
logs_dir = os.path.join(cwd, PARENT_DIR, SCRIPT_NAME)
# If log folder does not exist, make one
if not os.path.isdir(logs_dir):
    os.mkdir(logs_dir)
curr_month = datetime.datetime.utcnow().month
curr_year = datetime.datetime.utcnow().year
log_file_name = f'{curr_month}{curr_year}.log'
log_file = os.path.join(logs_dir, log_file_name)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(levelname)s: %(message)s')
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.info("Started.")


def exception_logger(logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as err:
                logger.error("{}: {}".format(type(err).__name__, str(err)))
                raise
        return wrapper
    return decorator


@exception_logger(logger)
def get_sql_conn(server: str='107.6.175.250', username: str = 'sh!v@n!@gg@rw@1', password: str = 'Y.c^jq#tv9g6y+#EhK=5#TQ') -> pyodbc.Connection:
    conn = pyodbc.connect(
        DRIVER=pyodbc.drivers()[-1],
        SERVER=server,
        UID=username,
        PWD=password,
        MARS_Connection='yes',
        timeout=3,
        TrustServerCertificate='yes'
    )
    return conn


@exception_logger(logger)
def get_redis_conn(host: str, port: int, db: int = 0, password: Optional[str] = None) -> redis.StrictRedis:
    if password:
        conn = redis.StrictRedis(
            host=host,
            port=port,
            db=db,
            password=password,
            charset="utf-8",
            decode_responses=True
        )
    else:
        conn = redis.StrictRedis(
            host=host,
            port=port,
            db=db,
            charset="utf-8",
            decode_responses=True
        )
    return conn


@exception_logger(logger)
def get_data(conn: pyodbc.Connection, last_modified: datetime.datetime) -> List[Tuple]:
    with conn.cursor() as cur:
        query = f"""SELECT a.reg_num, a.company_id, a.fastag_number, a.entity_id, b.IMEI
            FROM theBoons..boonsVehicles AS a WITH (NOLOCK)
            INNER JOIN gps..vehicles AS b WITH (NOLOCK)
            ON a.company_id = b.company_id and a.vehicle_id = b.vehicle_id
            WHERE b.IMEI IS NOT NULL AND a.modifiedDt >= ?;
        """
        cur.execute(query, (last_modified,))
        results = cur.fetchall()
    return results


@exception_logger(logger)
def put_data(redis_instance: redis.StrictRedis, key: str, data: List[Tuple]) -> None:
    with redis_instance.pipeline() as pipe:
        for reg_num, company_id, fastag_number, entity_id, imei in data:
            row = {'fastagNumber': fastag_number, 'cId': company_id, 'entId': entity_id, 'iMei': imei}
            pipe.hset(key, reg_num, json.dumps(row))
        pipe.execute()


def get_last_modified_date(file: str) -> int:
    try:
        with open(file, 'r') as fp:
            last_read = json.load(fp)['last_read']
    except FileNotFoundError as err:
        logger.error(f"{type(err).__name__}: {str(err)}")
        return 0
    except Exception as err:
        logger.error(f"{type(err).__name__}: {str(err)}")
        raise
    return last_read


def stamp_curr_modified_date(file: str, date_: datetime.datetime) -> None:
    data = {'last_read': int(date_.timestamp())}
    with open(file, 'w') as fp:
        json.dump(data, fp, indent=4)


def register_in_cronjobs(redis_instance: redis.StrictRedis) -> None:
    end_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    redis_instance.hset('cronJobLastRun', SCRIPT_NAME, end_time)


if __name__ == '__main__':
    start_time = datetime.datetime.utcnow()
    
    # Get last modified date
    file_name = SCRIPT_NAME + '.json'
    file = os.path.join(os.getcwd(), PARENT_DIR, SCRIPT_NAME, file_name)
    last_modified_stamp = get_last_modified_date(file)
    last_modified_date = datetime.datetime.fromtimestamp(last_modified_stamp)
    print(last_modified_date)
    
    # Get data from SQL
    conn = get_sql_conn()
    logger.info('Connected to SQL SERVER.')
    data = get_data(conn, last_modified_date)
    size = len(data)
    logger.info('Size of Data: {}'.format(size))
    print(data)

    # Dump data into redis
    if size > 0:
        redis_server = get_redis_conn(host=HOST1, port=PORT1)
        logger.info('Connected to Redis 6399.')
        put_data(redis_server, key=SCRIPT_NAME, data=data)
        logger.debug('Data dumped successfully.')

    # Stamp new modified date
    stamp_curr_modified_date(file, start_time)
    # Stamp in cronjobs
    redis7004 = get_redis_conn(host=HOST2, port=PORT2, password=PASSWORD2)
    register_in_cronjobs(redis7004)
    logger.info('Done.')
"""

if args.logs:
    print("Making logs.")

if args.cron:
    print("Stamping in cronjobs.")

if args.redis:
    print("Connecting to redis.")

if args.sql:
    print("Connecting to SQl.")

if args.mongo:
    print("Connecting to MongoDB.")
