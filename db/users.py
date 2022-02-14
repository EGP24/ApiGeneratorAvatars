from db.database import metadata, database
from ormar import Model, Integer, String


class User(Model):
    class Meta:
        tablename = 'users'
        metadata = metadata
        database = database

    id: int = Integer(primary_key=True, autoincrement=True)
    username: str = String(max_length=150)
    password: str = String(max_length=150)