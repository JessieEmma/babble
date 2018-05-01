# -*- coding: UTF-8 -*-

from operations.userc_op import queryModelById, updateChildInfoById
from controllers.cate_pic_con import produceWords, produceRandomExistWords
from utils.json_file import load
from utils.figuration import getDicMinsAndRandomKeys, getErrorString
from utils.topinyin import ALL_CATE

DEFAULT_SCORES = 1000
DEFAULT_ERRORS = 50

def getModelFileName(user_id):
    modelPathFileName = queryModelById(user_id)[0]['models']

    return modelPathFileName

def getTrainingIds(user_id):
    modelPathFileName = getModelFileName(user_id)
    modelPath = 'models/'+modelPathFileName
    data = load(modelPath)
    cates = getDicMinsAndRandomKeys(data)
    results = produceWords(cates)
    if len(results) < 5:
        produceRandomExistWords(results, data)

    return results

def updateNewInfo(data, user_id):
    string = getErrorString(data, ALL_CATE, DEFAULT_SCORES, DEFAULT_ERRORS)
    try:
        updateChildInfoById(user_id, string)
        result = True
    except:
        result = False

    return result


if __name__=='__main__':
    print(getTrainingIds(15))