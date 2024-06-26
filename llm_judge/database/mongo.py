import os
from dotenv import load_dotenv
from pymongo.server_api import ServerApi
from pymongo import MongoClient
from pymongo.database import Database

DATABASE_NAME = "llm-judge"
COLLECTIONS = {"questions", "answers", "judgments", "prompts", "evals"}

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path, override=True)

class DatabaseClient:
    client: MongoClient
    db: Database

    @classmethod
    def connect(cls):
        # print(os.environ["MONGO_URI"])
        cls.client = MongoClient(os.environ["MONGO_URI"], server_api=ServerApi("1"))
        cls.db = cls.client[DATABASE_NAME]

    @classmethod
    def disconnect(cls):
        cls.client.close()

    @classmethod
    def get_collection(cls, collection_name: str):
        if collection_name not in COLLECTIONS:
            raise ValueError(f"Collection {collection_name} does not exist")
        return cls.db[collection_name]

DatabaseClient.connect()
