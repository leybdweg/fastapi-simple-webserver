import pymongo

client = pymongo.AsyncMongoClient(
    host="localhost",
    port=27017,
    username="admin",  # FIXME: in production it should com from ENVs
    password="adminpassword",  # FIXME: in production it should com from ENVs
)

reserverDb = client.reserver
