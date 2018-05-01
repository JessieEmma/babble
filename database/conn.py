# -*- coding: UTF-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from database.tables import Userp
from contextlib import contextmanager
from excep import rollbackEx

DB_CONNECT_STRING = 'mysql+pymysql://root:root@localhost:3306/dbabble?charset=utf8'

def getDBSession(db_connect_line):
    engine = create_engine(db_connect_line, echo=True)
    dbSession = scoped_session(sessionmaker(bind=engine))
    return dbSession()

@contextmanager
def session_scope(db_connect_line):   #call this to connect
    session = getDBSession(db_connect_line)
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise rollbackEx('The operation failed. Roll back.')
    finally:
        session.close()


if __name__ == '__main__':
    with session_scope(DB_CONNECT_STRING) as session:
        new_user = Userp(telephone='1123', password='123456')
        session.add(new_user)


