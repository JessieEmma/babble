# -*- coding: UTF-8 -*-

from operations.cate_pic_op import queryAllCate, queryPicIdByPicname, queryPicByCateid, queryCateIdByCate, addCatePics, queryPiclistByCate
from utils.topinyin import chinese2pinyin, categoryBelong, ALL_CATE
from utils.figuration import getMaxes
from itertools import chain
import random


def getCateIdByCate(cate):
    result = queryCateIdByCate(cate)[0]
    return result

def getPicIdByPicname(picname):
    result = queryPicIdByPicname(picname)[0]
    return result

def categorize2db(word):  # 将词加入分类的数据库中
    ans, ansc = chinese2pinyin(word)
    categories = categoryBelong(ans)
    cates = categories + ans

    cate_ids = []
    for cate in cates:
        cate_id = getCateIdByCate(cate)
        if cate_id not in cate_ids:
            cate_ids.append(cate_id)

    pic_id = getPicIdByPicname(word)

    addCatePics(cate_ids, pic_id)

def randomChoose(cate):
    results = queryPiclistByCate(cate)
    if results == []:
        choice = []
    elif len(results) < 5:
        choice = results
    else:
        choice = random.sample(results, 5)

    return choice

def produceWords(cates):   # call this return the pic_ids, cates is the names of cates
    lists = []
    for cate in cates:
        choice = randomChoose(cate)
        if choice != []:
            lists.append(choice)

    lists = list(chain.from_iterable(lists))
    results = getMaxes(lists)

    return results  # pic_ids

def produceRandomExistWords(oldResults, data, resultLen=5):
    t = tuple(data)
    while len(oldResults) < resultLen:
        print(oldResults)
        choice = random.sample(t, 1)[0]
        queryResult = queryPiclistByCate(choice)
        if queryResult != [] and queryResult not in oldResults:
            oldResults.append(queryResult)

    return oldResults

def filterCates(datas): # [{"cate_id": 1, "cate": "鼻边音"}]
    filters = {}
    for data in datas:
        if data["cate"] in ALL_CATE:
            filters[data["cate"]] = data["cate_id"]  # {"鼻边音": 1}

    results = []
    for f in filters:
        dic = {}
        dic["cate_id"] = filters[f]
        dic["cate"] = f
        results.append(dic)
    return results

def showCates():
    datas = queryAllCate()
    results = filterCates(datas)
    return results

def getPiclistByCate(cate):
    cate_id = queryCateIdByCate(cate=cate)[0]
    results = queryPicByCateid(cate_id)
    return results





if __name__== '__main__':
    print(randomChoose("yu"))













