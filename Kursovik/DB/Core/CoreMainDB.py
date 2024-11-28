from sqlalchemy import create_engine, text, insert, select, update, delete
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
# from base import metadata_obj
from Kursovik.DB.Core.config import settings

sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True
)

with sync_engine.connect() as conn:
    print("Successfully connected to database")
session_factory = sessionmaker(sync_engine)
