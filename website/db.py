from pymongo import MongoClient
from pymongo.errors import ConfigurationError
from functools import lru_cache
import certifi
import os

def _uri():
    uri = os.getenv("MONGODB_URI")
    if not uri:
        raise ConfigurationError("MONGODB_URI not set")
    return uri

@lru_cache(maxsize=1)
def get_client() -> MongoClient:
    # Created the first time a worker uses it (safe after fork)
    return MongoClient(
        _uri(),
        tls=True,
        tlsCAFile=certifi.where(),
        serverSelectionTimeoutMS=8000,
    )

def get_db():
    return get_client()["newsUsers"]

def get_users_collection():
    return get_db()["users"]
