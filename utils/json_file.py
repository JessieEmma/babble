# -*- coding: utf-8 -*-
import json
import time
import os
from utils.topinyin import ALL_CATEGORISES

def store(filename, data):
    with open(filename, 'w', encoding='utf8') as json_file:
        json_file.write(json.dumps(data, ensure_ascii=False))

def load(filename, sample='models/sample.json'):
    if not os.path.exists(filename):
        filename = sample
    with open(filename, encoding='utf8') as json_file:
        data = json.load(json_file)
        return data

def copyFile(target, source='models/sample.json'):
    data = load(source)
    store(target, data)

def updateFile(filename, contents, names=ALL_CATEGORISES):
    data = load(filename)
    for name, content in zip(names, contents):
        data[name] += content
    store(filename, data)

def generateFileName(tele):
    now = str(time.time()).replace('.',"")
    filename = now + tele + '.json'
    return filename

def getDataInFile(filename):
    data = load(filename)
    return data




if __name__ == "__main__":
    store('e.json','1234')