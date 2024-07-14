from pymongo import MongoClient

import argparse
import json

def main():
    """Main function to be ran..."""
    parser = argparse.ArgumentParser(description='CRM Tool for MongoDB')
    parser.add_argument('--db', required=True, help='Name of the MongoDB database')
    parser.add_argument('--collection', required=True, help='Name of the MongoDB collection')
    parser.add_argument('--host', default='localhost', help='MongoDB host (default: localhost)')
    parser.add_argument('--port', type=int, default=27017, help='MongoDB port (default: 27017)')
    parser.add_argument('--params', type=str, help='Specific parameters in JSON format')

    args = parser.parse_args()
    
    db_name = args.db
    collection_name = args.collection
    host = args.host
    port = args.port
    params = json.loads(args.params) if args.params else {}
    
    print(f"Connecting to MongoDB database '{db_name}' and collection '{collection_name}' on {host}:{port}")

    client = MongoClient(f"mongodb://{host}:{port}/")
    db = client[f'{db_name}']
    collection = db[f'{collection_name}']





if __name__ == '__main__':
    main()
