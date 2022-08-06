import os
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa
from sqlalchemy.orm import relationship



base = declarative_base()
conn_string = f"""
    mysql+pymysql://
    {os.environ.get('DB_USER')}
    :{os.environ.get('DB_PASSWORD')}
    @{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}
    /{os.environ.get('DB_NAME')}
""".translate(str.maketrans({'\n': '', '\r': '', ' ': ''}))
# print(conn_string)
engine = sa.create_engine(conn_string)
base.metadata.bind = engine
session = orm.scoped_session(orm.sessionmaker())(bind=engine)
base.metadata.create_all()
