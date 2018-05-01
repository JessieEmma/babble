# -*- coding: UTF-8 -*-

from flask import Flask, request, jsonify, Response, redirect
from utils.alchemy_utils import alchemy2json
from utils.topinyin import compExam, compExamOnly, PinYinToCateName
from utils.json_file import updateFile, getDataInFile
from utils.tele_yan import send_message, verify
import json

from operations.userc_op import addChildren, queryChildrenByTel, queryChildAllInfoById
from operations.cate_pic_op import queryPicpathById, queryPicpathByWord, queryAllPic, queryPicByCateid, queryPicnameByIds, queryPicByCateName
from operations.userp_op import queryToGetPswByTel, addUser
from controllers.userc_con import getTrainingIds, getModelFileName, updateNewInfo
from controllers.cate_pic_con import showCates, getPiclistByCate
import datetime
nowYear = datetime.datetime.now().year

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
PATH = 'localhost:8080'

@app.route('/identele/<telephone>')
def sendIdentifying(telephone):  # 发送验证码
    if send_message(telephone):
        result = "True"
        return jsonify({'result': result})
    else:
        result = "False"
        return jsonify({'result': result})

@app.route('/registration/<telephone>/<code>/<password>')
def addParent(telephone, code, password):
    if code == '':
        result = 'Please input the verification code!'
        return jsonify({'result':result})
    elif verify(telephone, code):

        try:
            addUser(telephone, password)
            result = 'Successfully registered.'
            return jsonify({'result': result})
        except:
            result = 'The number has been registered!'
            return jsonify({'result': result})

    else:
        result = 'Your code is wrong, please check again!'
        return jsonify({'result':result})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_data()
    j_data = json.loads(data, encoding='utf8')

    telephone = j_data['telephone']
    print(telephone)
    psw = j_data["password"]
    print(psw)
    passwordInDB = queryToGetPswByTel(telephone).password
    print(passwordInDB)
    if psw == passwordInDB:
        result = PATH + '/children/'+telephone
        return jsonify({'result': result})
    else:
        result = "False"
        return jsonify({'result': result})


@app.route('/children/<telephone>')
def getChildren(telephone):
    datas = queryChildrenByTel(telephone)
    return Response(alchemy2json(datas), mimetype='application/json')

@app.route('/addchild', methods=["POST"])
def addChild():
    data = request.get_data()
    j_data = json.loads(data, encoding='utf8')

    telephone = j_data['telephone']
    nickname = j_data['nickname']
    agenow = j_data['agenow']
    gender = j_data['gender']

    agenowInt = int(agenow)
    birthyear = nowYear - agenowInt
    try:
        addChildren(telephone, nickname, birthyear, gender)
        result = "True"
        return jsonify({'result': result})
    except:
        result = "False"
        return jsonify({'result': result})

@app.route('/childinfo/<user_id>')
def getChildAllInfo(user_id):
    datas = queryChildAllInfoById(user_id)
    return Response(alchemy2json(datas), mimetype='application/json')

@app.route('/metals')
def getAllPic():
    datas = queryAllPic()
    return Response(alchemy2json(datas), mimetype='application/json')

@app.route('/metals/<cate>')
def getAllPicByCate(cate):
    datas = getPiclistByCate(cate)
    return Response(alchemy2json(datas), mimetype='application/json')

@app.route('/metals/cate/<cate>')
def getAllPicByCatePinyin(cate):
    cateName = PinYinToCateName[cate]
    datas = getPiclistByCate(cateName)
    return Response(alchemy2json(datas), mimetype='application/json')

@app.route("/categories")
def getAllCate():
    datas = showCates()
    return Response(alchemy2json(datas), mimetype='application/json')

@app.route("/category/<cate_id>", methods=['GET'])
def getCatePic(cate_id):
    datas = queryPicByCateid(cate_id)
    return Response(alchemy2json(datas), mimetype='application/json')

@app.route('/id2picture/<pic_id>', methods=['GET'])
def id2pic(pic_id):
    print(pic_id)
    picpath = queryPicpathById(pic_id)
    print("pic_path", picpath)
    if picpath:
        path = 'metals/' + picpath
        try:
            image = open(path, 'rb')
        except:
            path = 'metals/default.jpg'
            image = open(path, 'rb')
        resp = Response(image, mimetype='image/jpeg')
        return resp
    else:
        path = 'metals/default.jpg'
        image = open(path, 'rb')
        resp = Response(image, mimetype='image/jpeg')
        return resp

@app.route('/word2picture/<word>', methods=['GET'])
def word2pic(word):
    picpath =queryPicpathByWord(word)
    if picpath:
        path = 'metals/' + picpath[0]['picpath']
        try:
            image = open(path, 'rb')
        except:
            path = 'metals/default.jpg'
            image = open(path, 'rb')
        resp = Response(image, mimetype='image/jpeg')
        return resp
    else:
        path = 'metals/default.jpg'
        image = open(path, 'rb')
        resp = Response(image, mimetype='image/jpeg')
        return resp

@app.route('/recognisation/<user_id>', methods=['POST'])
def recognizeAndRecord(user_id):
    data = request.get_data()
    j_data = json.loads(data, encoding='utf8')
    #print(j_data)
    example = j_data['example']
    text = j_data['text']

    re_in, trainScores = compExam(example, text)
    filename = 'models/' + getModelFileName(user_id)
    updateFile(filename, trainScores)
    if re_in[0]:
        result = "True"
    else:
        result = "False"
    return jsonify({'result': result, 'info': re_in[1]})

@app.route('/onlyrecog', methods=['POST'])
def recognizeOnly():
    data = request.get_data()
    print(data)
    j_data = json.loads(data, encoding='utf8')
    #print(j_data)
    example = j_data['example']
    text = j_data['text']
    re_in = compExamOnly(example, text)
    if re_in[0]:
        result = "True"
    else:
        result = "False"
    return jsonify({'result': result, 'info': re_in[1]})

@app.route('/training/<user_id>')
def getTrainWords(user_id):
    results = getTrainingIds(user_id)
    return Response(alchemy2json(queryPicnameByIds(results)), mimetype='application/json')

@app.route('/ending/<user_id>')
def updateInfoAfterTrain(user_id):
    filename = 'models/' + getModelFileName(user_id)
    data = getDataInFile(filename)
    resultBool = updateNewInfo(data, user_id)
    if resultBool:
        result = "True"
    else:
        result = "False"
    return jsonify({'result': result})

@app.route('/childimg')
def childiimg():
    path = 'childImage/childImageDefault.jpg'
    image = open(path, 'rb')
    resp = Response(image, mimetype='image/jpeg')
    return resp

@app.route('/goose')
def getGoose():
    path = 'metals/add2/e.jpg'
    image = open(path, 'rb')
    resp = Response(image, mimetype='image/jpeg')
    return resp

if __name__ == '__main__':

    app.run(host="0.0.0.0")
    #app.run(host="localhost", port=8080)

