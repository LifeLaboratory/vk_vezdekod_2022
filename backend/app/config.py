import os
HEADER = {'Access-Control-Allow-Origin': '*'}
DATABASE = {
    "dbname": os.environ["DB_NAME"],
    "user": os.environ["DB_LOGIN"],
    "host": os.environ["DB_HOST"],
    "password": os.environ["DB_PASSWORD"],
    "port": os.environ["DB_PORT"]
}

HOST = os.environ["HOST"]
