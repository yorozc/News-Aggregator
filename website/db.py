from pymongo import MongoClient
import certifi 
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGODB_URI")

client = MongoClient(
    uri,
    TLS=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=30000,
                     )

db = client["newsUsers"]
users = db["users"] # creates collection if doesn't exist

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)