from prometheus_client import start_http_server, Gauge
from pymongo import MongoClient
import time

mongo_url = 'mongodb://192.168.1.162:27017'
client = MongoClient(mongo_url)

mongo_db_up = Gauge('mongo_db_up', 'MongoDB Up/Down Status')

def mongodb_connect():
    try:
        client = MongoClient(mongo_url,serverSelectionTimeoutMS=5000)
        db = client['admin']
        db.command('ping')
        mongo_db_up.set(1)

        
    except Exception as err:
        print(' MongoDB connection failed', err)
        mongo_db_up.set(0)

    finally:
        client.close()
        


start_http_server(3030)

while True:
    mongodb_connect()
    time.sleep(15)
