import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from src.config.environment_config import Environment

Environment.config_environment("localhost")

DATABASE_DIALECT = os.environ["DB_DIALECT"]
DATABASE_USER = os.environ["DB_USER"]
DATABASE_PASSWORD = os.environ["DB_PASSWORD"]
DATABASE_HOST = os.environ["DB_HOST"]
DATABASE = os.environ["DB"]
IP_HOST = os.environ["IP_HOST"]
PORT_HOST = os.environ["PORT_HOST"]

origins=["*"]

DATABASE_URL = f"{DATABASE_DIALECT}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE}"

engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()