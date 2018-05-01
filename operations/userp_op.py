# -*- coding: UTF-8 -*-

from database.conn import session_scope, DB_CONNECT_STRING
from database.tables import Userp
import copy

def addUser(telephone, password):
    with session_scope(DB_CONNECT_STRING) as session:
        new_user = Userp(telephone=telephone, password=password)
        session.add(new_user)

def queryToGetPswByTel(telephone):
    with session_scope(DB_CONNECT_STRING) as session:
        data = session.query(Userp).filter(Userp.telephone == telephone).first()
        newdata = copy.deepcopy(data)

    return newdata

