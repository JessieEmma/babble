import random
from utils.topinyin import ALL_CATE

def getMaxes(lists, size=5):  # input one-divension list
    counters = []
    for data in set(lists):
        counters.append((data, lists.count(data)))

    counters.sort(key=lambda t: t[1], reverse=True)

    results = []

    if len(counters) < size:
        for i in range(len(counters)):
            results.append(counters[i][0])
    else:
        for i in range(size):
            results.append(counters[i][0])

    return results

def getDicMinsAndRandomKeys(data, minsize=4, randomsize=1):
    ds = sorted(data.items(), key=lambda x: x[1])
    t = tuple(data)
    results = []
    for d in tuple(ds)[:minsize]:
        results.append(d[0])

    results.append(random.sample(t, randomsize)[0])
    return results # cate names

def getMoreRandomKeys(oldResults, data, resultLen=5):
    t = tuple(data)
    while len(oldResults) < resultLen:
        choice = random.sample(t, 1)[0]
        if choice not in oldResults:
            oldResults.append(choice)
    return oldResults

def getErrorString(datas, cates, defaultScore, defaultError):
    results = []
    for data in datas:
        if datas[data] < defaultScore-defaultError and data in cates:
            results.append(data)

    errorString = ""
    for result in results:
        errorString += result + ' '

    if errorString != "":
        errorString += '发音需强加练习。'
    else:
        errorString = '暂无新信息'
    return errorString










if __name__ == "__main__":
    dic = {"a":2, "b":3, "c":4, 'd':1}
    results = []
    for di in dic:
        if dic[di] < 5-2 and di in ["a", "b"]:
            print(di)


