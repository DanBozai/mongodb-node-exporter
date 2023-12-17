import argparse
def parse_args():
    
    parser = argparse.ArgumentParser(description="MongoDB Status Monitoring Service")
    parser.add_argument('--no_config', action='store_true', help="Disable yaml configuration file")
    parser.add_argument('--config','-c', type=str, default="/etc/mongodb-node-exporter/mongodb-node-exporter.yaml", help="path to configuration file  default='/etc/mongodb-node-exporter/mongodb-node-exporter.yaml'")
    parser.add_argument('--mongodb_uri',type=str, default="mongodb://localhost:27017",help="connection string; URI example: mongodb://localhost:27017")
    
    return parser.parse_args()