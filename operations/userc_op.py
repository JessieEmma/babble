# -*- coding: UTF-8 -*-

from database.conn import session_scope, DB_CONNECT_STRING
from database.tables import Userc
from utils.alchemy_utils import dataToDic
from utils.json_file import generateFileName
from excep import queryNoneEx
import datetime
year = datetime.datetime.now().year

def addChildren(telephone, nickname, birthyear, gender):
    with session_scope(DB_CONNECT_STRING) as session:
        models = generateFileName(telephone)
        new_user = Userc(telephone=telephone, nickname=nickname, birthyear=birthyear, gender=gender, info='暂无新信息',scores=0, models=models)
        session.add(new_user)

def queryChildrenByTel(telephone):
    with session_scope(DB_CONNECT_STRING) as session:
        datas = session.query(Userc.user_id, Userc.nickname).filter(Userc.telephone == telephone).all()

    keys = ['user_id', 'nickname']
    results = dataToDic(keys, datas)

    return results

def queryChildAllInfoById(user_id):
    with session_scope(DB_CONNECT_STRING) as session:
        datas = session.query(Userc.user_id, Userc.nickname, Userc.gender, year-Userc.birthyear, Userc.info).filter(Userc.user_id == user_id).first()

    keys = ['user_id', 'nickname', 'gender', 'birthyear', 'info']
    results = dataToDic(keys, datas)

    return results

def updateChildInfoById(user_id, info):   # can raise an Exp
    with session_scope(DB_CONNECT_STRING) as session:
        data = session.query(Userc).filter(Userc.user_id==user_id).first()
        if not data:
            raise queryNoneEx

        data.info = info
        print("changed")

def queryModelById(user_id):
    with session_scope(DB_CONNECT_STRING) as session:
        datas = session.query(Userc.models).filter(Userc.user_id==user_id).first()

    keys = ['models']
    results = dataToDic(keys, datas)

    return results  # [{'models': 'nihao'}]


if __name__ == "__main__":
    #try:
     #   updateChildInfoById(1,"dja")
      #  print("T")
    #except:
     #   print("F")
     print(queryModelById(12)[0]['models'])





