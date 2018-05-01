# -*- coding: UTF-8 -*-

from database.tables import Pic, Category, CatePic
from database.conn import session_scope, DB_CONNECT_STRING
from utils.alchemy_utils import dataToDic
from excep import queryNoneEx
import copy

def queryPicnameById(pic_id):
    with session_scope(DB_CONNECT_STRING) as session:
        datas = session.query(Pic.pic_id, Pic.picname).filter(Pic.pic_id==pic_id).all()

    keys = ['pic_id', 'picname']
    results = dataToDic(keys, datas)

    return results

def queryPicnameByIds(pic_ids):
    with session_scope(DB_CONNECT_STRING) as session:
        datas = session.query(Pic.pic_id, Pic.picname).filter(Pic.pic_id.in_(pic_ids)).all()

    keys = ['pic_id', 'picname']
    results = dataToDic(keys, datas)

    return results

def queryPicpathById(pic_id):
    with session_scope(DB_CONNECT_STRING) as session:
        data = session.query(Pic).filter(Pic.pic_id == pic_id).first()
        print(data)
        newdata = copy.deepcopy(data)

    path = newdata.picpath
    print(path)

    return path

def queryPicpathByWord(word):
    with session_scope(DB_CONNECT_STRING) as session:
        data = session.query(Pic.picpath).filter(Pic.picname == word).first()

    keys = ['picpath']
    results = dataToDic(keys, data)

    return results

def queryAllPic():
    with session_scope(DB_CONNECT_STRING) as session:
        datas = session.query(Pic.pic_id, Pic.picname).all()

    keys = ['pic_id', 'picname']
    results = dataToDic(keys, datas)

    return results


def queryAllCate():
    with session_scope(DB_CONNECT_STRING) as session:
        datas = session.query(Category.cate_id, Category.cate).all()

    keys = ["cate_id", "cate"]
    results = dataToDic(keys, datas)

    return results


def queryPicByCateid(cate_id):
    with session_scope(DB_CONNECT_STRING) as session:
        datas = session.query(Pic.pic_id, Pic.picname).join(CatePic).filter(CatePic.cate_id == cate_id).all()

    for data in datas:
        print(data)
    keys = ['pic_id', 'picname']
    results = dataToDic(keys, datas)

    return results

def queryPicByCateName(cate):
    with session_scope(DB_CONNECT_STRING) as session:
        datas = session.query(Pic.pic_id, Pic.picname).join(Category).filter(Category.cate == cate).all()

    for data in datas:
        print(data)
    keys = ['pic_id', 'picname']
    results = dataToDic(keys, datas)

    return results

def updateCate(cate, cate_id):
    with session_scope(DB_CONNECT_STRING) as session:
        data = session.query(Category).filter(Category.cate_id==cate_id).first()
        if not data:
            raise queryNoneEx

        data.cate = cate
        print("changed")

def updateCatePic(cate_id, pic_id):
    with session_scope(DB_CONNECT_STRING) as session:
        data = session.query(CatePic).filter(CatePic.pic_id==pic_id).first()
        if not data:
            raise queryNoneEx

        data.cate_id = cate_id
        print("changed")

def queryCateIdByCate(cate):
    with session_scope(DB_CONNECT_STRING) as session:
        data = session.query(Category.cate_id).filter(Category.cate==cate).first()
        newdata = data

    return newdata

def queryPiclistByCate(cate):
    with session_scope(DB_CONNECT_STRING) as session:
        datas = session.query(CatePic.pic_id).join(Category).filter(Category.cate==cate).all()
        results = []
        for data in datas:
            results.append(data[0])

    return results  # a list

def queryPicIdByPicname(picname):
    with session_scope(DB_CONNECT_STRING) as session:
        data = session.query(Pic.pic_id).filter(Pic.picname==picname).first()
        newdata = data

    return newdata

def addCatePics(cate_ids, pic_id):
    with session_scope(DB_CONNECT_STRING) as session:
        re = []
        for cate_id in cate_ids:
            re.append(CatePic(cate_id=cate_id, pic_id=pic_id))

        session.add_all(re)



if __name__ == '__main__':
    print(queryCateIdByCate("平舌音"))