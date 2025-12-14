from sqlalchemy import inspect
from src.database.configure_sqllite import db

def get_schema():
   

    return db.get_table_info()
