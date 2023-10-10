from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config

url = config("DB_URL")
client = AsyncIOMotorClient(url)
database = client.HiriumDB