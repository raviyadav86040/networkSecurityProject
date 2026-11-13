from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongo_url = os.getenv("MONGO_DB_URL")

client = MongoClient(mongo_url)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)