from pymongo.mongo_client import MongoClient
import pandas as pd
import json
## uniform resource identifier
uri = "mongodb+srv://pwskills:Pouravi2003@cluster0.qxefg4l.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)

## create database name and collection name
DATABASE_NAME='pwskills'
COLLECTION_NAME="waferfault"
## read the data as dataframe
df=pd.read_csv(r'D:\ML Project\ML Project For Pouravi Ghosh\sensor-fault-detection\notebooks\data\wafer_23012020_041211.csv')
df = df.drop("Unnamed: 0",axis=1)
## convert data into json
json_record=list(json.loads(df.T.to_json()).values())

## now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
