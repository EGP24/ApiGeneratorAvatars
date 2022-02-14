from starlette.config import Config

config = Config('.env')
POSTGRES_USERNAME = config('EE_POSTGRES_USERNAME', cast=str)
POSTGRES_PASSWORD = config('EE_POSTGRES_PASSWORD', cast=str)
POSTGRES_DB = config('EE_POSTGRES_DB', cast=str)
REDIS_URL = config('EE_REDIS_URL', cast=str)
REDIS_PASSWORD = config('EE_REDIS_PASSWORD', cast=str)
SECRET_KEY = config('EE_SECRET_KEY', cast=str)
ACCESS_TOKEN_EXPIRE_MINUTES = config('EE_ACCESS_TOKEN_EXPIRE_MINUTES', cast=int)
ALGORITHM = config('EE_ALGORITHM', cast=str)