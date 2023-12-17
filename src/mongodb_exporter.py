import os
from prometheus_client import start_http_server, Gauge
from pymongo import MongoClient
import time
from config_yaml_loader import load_yaml_file
from arg_parser import parse_args

config_args=parse_args()

print("Debug:config_args",config_args)

if not os.path.isfile(config_args.config):
    print(f"WARNING: Configuration file {config_args.config} does not exist")

    
    
if (config_args.no_config):
    print('Debug: run with --no_config enabled')
else:
    yaml_config_data= load_yaml_file(config_args.config)
    if yaml_config_data:
        print("yaml: ",yaml_config_data)
        config_args.mongodb_uri=yaml_config_data['mongodb_uri']
        
    else:
        print("WARNING: No configuration data available.")
    

    
    
    
MONGODB_URI = config_args.mongodb_uri

print(MONGODB_URI)




client = MongoClient(MONGODB_URI)

mongo_db_up = Gauge('mongo_db_up', 'MongoDB Up/Down Status')

def mongodb_connect():
    try:
        client = MongoClient(MONGODB_URI,serverSelectionTimeoutMS=5000)
        db = client['admin']
        db.command('ping')
        mongo_db_up.set(1)

        
    except Exception as err:
        print('MongoDB connection failed', err)
        mongo_db_up.set(0)

    finally:
        client.close()
        


start_http_server(3030)

while True:
    mongodb_connect()
    time.sleep(15)
