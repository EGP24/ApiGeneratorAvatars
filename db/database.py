from core.config import POSTGRES_USERNAME, POSTGRES_PASSWORD, POSTGRES_DB, REDIS_URL, REDIS_PASSWORD
from sqlalchemy import create_engine, MetaData
from databases import Database
from aioredis import from_url

database_url = f'postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@postgres:5432/{POSTGRES_DB}'
engine = create_engine(database_url)

metadata = MetaData()
database = Database(database_url)
redis = from_url(REDIS_URL, password=REDIS_PASSWORD)