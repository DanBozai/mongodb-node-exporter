from prometheus_client import start_http_server, Gauge
from pymongo import MongoClient
import time

mongo_url = 'mongodb://192.168.1.162:27017'
client = MongoClient(mongo_url)

mongo_db_up = Gauge('mongo_db_up', 'mongoDB Up/Down Status')

def main():
    try:
        client = MongoClient(mongo_url,serverSelectionTimeoutMS=5000)
        db = client['admin']
        db.command('ping')
        mongo_db_up.set(1)
        print("Mongodb is up")

        
    except Exception as err:
        print(' MongoDB connection failed:', err)
        mongo_db_up.set(0)

    finally:
        client.close()
        


start_http_server(3030)

while True:
    main()
    time.sleep(15)
