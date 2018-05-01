import pypinyin
from pypinyin import pinyin, lazy_pinyin

ALL_SYLLABLE = ['a', 'o', 'e', 'i', 'u', 'v',
       'b', 'p', 'm', 'f', 'd', 't', 'n', 'l',
       'g', 'k', 'h', 'j', 'q', 'x',
       'zh', 'ch', 'sh', 'r', 'z', 'c', 's', 'y', 'w',
       'ang', 'eng', 'ing', 'ong', 'an', 'en', 'in',
       'un', 'ai', 'ei', 'ui', 'ao', 'ou', 'iu', 'ie', 'ue', 'er',
       'zhi', 'chi', 'shi', 'ri', 'zi', 'ci', 'si',
       'yi', 'wu', 'yu', 'ye', 'yue', 'yuan', 'yin','yun','ying']

ALL_CATE = ['平舌音', '翘舌音', '鼻音', '边音', '前鼻音', '后鼻音']

ALL_CATEGORISES = ALL_CATE + ALL_SYLLABLE


# 分类： 平舌音第1类，翘舌音2， 鼻音3， 边音4， 前鼻音5， 后鼻音6, 其余7
dicPC = {'z':1, 'c':1, 's':1, 'zi':1, 'ci':1, 'si':1,
         'zh':2, 'ch':2, 'sh':2, 'r':2, 'zhi':2, 'chi':2, 'shi':2, 'ri':2,
         'm':3, 'n':3,
         'l':4,
         'an':5, 'en':5, 'in':5, 'un':5, 'yin':5, 'yuan':5, 'yun':5,
         'ang':6, 'eng':6, 'ing':6, 'ong':6, 'ying':6}

dicCateName = {1:'平舌音', 2:'翘舌音', 3:'鼻音', 4:'边音', 5:'前鼻音', 6:'后鼻音'}


# 所有音的数字序列
dic = {'a':1, 'o':2, 'e':3, 'i':4, 'u':5, 'v':6,
       'b':7, 'p':8, 'm':9, 'f':10, 'd':11, 't':12, 'n':13, 'l':14,
       'g':15, 'k':16, 'h':17, 'j':18, 'q':19, 'x':20,
       'zh':21, 'ch':22, 'sh':23, 'r':24, 'z':25, 'c':26, 's':27, 'y':28, 'w':29,
       'ang':30, 'eng':31, 'ing':32, 'ong':33, 'an':34, 'en':35, 'in':36,
       'un':37, 'ai':38, 'ei':39, 'ui':40, 'ao':41, 'ou':42, 'iu':43, 'ie':44, 'ue':45, 'er':46,
       'zhi':47, 'chi':48, 'shi':49, 'ri':50, 'zi':51, 'ci':52, 'si':53,
       'yi':54, 'wu':55, 'yu':56, 'ye':57, 'yue':58, 'yuan':59, 'yin':60, 'yun':61, 'ying':62}


PinYinToCateName = { "pingsheyin" : "平舌音",
                     "qiaosheyin" : "翘舌音",
                     "biyin": "鼻音",
                     "bianyin" : "边音",
                     "qianbiyin" : "前鼻音",
                     "houbiyin" : "后鼻音"}

dicVK = {v:k for k,v in dic.items()}


def categoryBelong(lists): # ['b', 'o']
    results = []
    values = []
    for list in lists:
        value = dicPC.get(list, 7)
        if value != 7 and value not in values:
            results.append(dicCateName[value])
        values.append(value)

    return results

sheng = ['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'zh', 'ch', 'sh',
             'r', 'z', 'c', 's', 'y', 'w']
yuns = ['ang', 'eng', 'ing', 'ong', 'an', 'en', 'in',
           'un', 'ai', 'ei', 'ui', 'ao', 'ou', 'iu', 'ie', 'ue', 'er']
dans = ['a', 'o', 'e', 'i', 'u', 'v']
alls = ['ang', 'eng', 'ing', 'ong', 'an', 'en', 'in', 'un', 'ai', 'ei',
            'ui', 'ao', 'ou', 'iu', 'ie', 'ue', 'er', 'a', 'o', 'e', 'i', 'u', 'v']
fu = ['ai', 'ei', 'ui', 'ao', 'ou', 'iu', 'ie', 'ue', 'er']
qian = ['an', 'en', 'in', 'un']
hou = ['ang', 'eng', 'ing', 'ong']
zheng = ['zhi', 'chi', 'shi', 'ri', 'zi', 'ci', 'si',
             'yi', 'wu', 'yu', 'ye', 'yue', 'yuan', 'yin', 'yun', 'ying']

ones = zheng + dans + ['an', 'ang', 'ai', 'en', 'ao', 'ei', 'ou']


def chinese2pinyin(str):  # 分解拼音拼读
    pins = lazy_pinyin(str, errors='ignore')
    pinsep = lazy_pinyin(str, style=pypinyin.INITIALS)

    is_zheng = [False] * len(pins)
    sepp = []
    count = []
    counter = 0

    for i in range(len(pins)):

        if pins[i][0] == 'w' or pins[i][0] == 'y':
            pinsep[i] = pins[i][0]


        if pins[i] in ones:
            is_zheng[i] = True
            sepp.append(pins[i])
            count.append(counter)
            counter += 1
            continue


        if is_zheng[i] == False:
            is_tri = False
            for all in alls:
                find_re = pins[i].find(all, 0)
                if find_re > -1 and find_re == len(pinsep[i]) +1:
                    count.append(counter)
                    counter += 3
                    sepp.append(pins[i][:find_re-1])
                    sepp.append(pins[i][find_re-1] )
                    sepp.append(pins[i][find_re:])
                    is_tri = True
                    break
                elif find_re > -1 and find_re == len(pinsep[i]):
                    count.append(counter)
                    counter += 2
                    sepp.append(pins[i][:find_re])
                    sepp.append(pins[i][find_re:])
                    is_tri = True
                    break

            if is_tri == False:
                for all in alls:
                    find_re = pins[i].find(all, 0)
                    if find_re > -1:
                        count.append(counter)
                        counter += 2
                        sepp.append(pins[i][:find_re])
                        sepp.append(pins[i][find_re:])
                        break

    print(sepp)
    print(count)

    return sepp, count

def getCate(str):  # 得到分类结果(类型，音节)
    ans, ansc = chinese2pinyin(str)
    t1s = []
    t2s = []
    results = []
    for an in ans:
        t1s.append(dicPC.get(an, 7))
        t2s.append(dic.get(an, 63))

    for t1, t2 in zip(t1s, t2s):
        results.append((t1, t2))

    print(results)
    return results   # （6, 43）

def getInfo(examplesBefore, textsBefore):  # input the words in Chinese
    examples = getCate(examplesBefore)
    texts = getCate(textsBefore)   # getCate()后的结果
    infos = ''

    trainScores = [0]*68

    if len(examples) != len(texts):
        result = False
        infos = '发音不清，请重试'
    else:
        if examples == texts:
            result = True
            infos = '正确'
        else:
            result = False
            for i in range(len(examples)):
                numExamCate = examples[i][0]
                numTextCate = texts[i][0]
                numExamAccu = examples[i][1]
                numTextAccu = texts[i][1]
                info = ''
                if numExamCate != numTextCate and numExamCate != 7:
                    info += dicCateName[numExamCate] + '未发准。'
                    trainScores[ALL_CATEGORISES.index(dicCateName[numExamCate])] -= 1
                elif numExamCate == numTextCate and numExamCate != 7:
                    trainScores[ALL_CATEGORISES.index(dicCateName[numExamCate])] += 1

                if numExamAccu != numTextAccu:
                    info += '[' + dicVK[numExamAccu] + ']'+ '错误发音成[' + dicVK[numTextAccu] + '] '
                    trainScores[ALL_CATEGORISES.index(dicVK[numExamAccu])] -= 1
                else:
                    trainScores[ALL_CATEGORISES.index(dicVK[numExamAccu])] += 1

                infos += info
    print(trainScores)
    print(infos)
    if result:
        print("is ture")
    else:
        print("is wrong")

    re_in = [result, infos]

    return re_in, trainScores

def getInfoOnly(examplesBefore, textsBefore):  # input the words in Chinese
    examples = getCate(examplesBefore)
    texts = getCate(textsBefore)   # getCate()后的结果
    infos = ''

    if len(examples) != len(texts):
        result = False
        infos = '发音不清，请重试'
    else:
        if examples == texts:
            result = True
            infos = '正确'
        else:
            result = False
            for i in range(len(examples)):
                numExamCate = examples[i][0]
                numTextCate = texts[i][0]
                numExamAccu = examples[i][1]
                numTextAccu = texts[i][1]
                info = ''
                if numExamCate != numTextCate and numExamCate != 7:
                    info += dicCateName[numExamCate] + '未发准。'

                if numExamAccu != numTextAccu:
                    info += '[' + dicVK[numExamAccu] + ']'+ '错误发音成[' + dicVK[numTextAccu] + ']。'

                infos += info
    print(infos)

    re_in = [result, infos]

    return re_in


def compExam(example, text):  # compare the text call this
    re_in, trainScores = getInfo(example, text)
    return re_in, trainScores

def compExamOnly(example, text):
    re_in = getInfoOnly(example, text)
    return re_in


if __name__ == '__main__':
    #ans, ansc = chinese2pinyin('我于你莫发镇装磅网苹果惊喜弯挂')
    #ans1, ansc1 = chinese2pinyin('西安吃欧')
    #if ans == ans1:
     #   print('Yes')
    #else:
     #   print('no')
    #getInfo('苹果裤子', '拼古哦骨子')
    getCate("电视机")

