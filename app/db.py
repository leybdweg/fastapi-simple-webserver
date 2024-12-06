import os

import pymongo

client = pymongo.AsyncMongoClient(
    host="localhost",
    port=27017,
    username="admin",  # FIXME: in production it should com from ENVs
    password="adminpassword",  # FIXME: in production it should com from ENVs
)

db_name = ''
match os.environ.get('ENV', 'TEST'):
    case 'TEST':
        db_name = 'reserver_test'
    case _:
        db_name = 'reserver'

reserverDb = client[db_name]
