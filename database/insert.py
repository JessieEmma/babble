# -*- coding: UTF-8 -*-

from database.conn import session_scope, DB_CONNECT_STRING
from database.tables import Pic, Category, CatePic
from utils.topinyin import ALL_CATEGORISES
from controllers.cate_pic_con import categorize2db

# 素材库的初始化

re1 = []
for syl in ALL_CATEGORISES:
    re1.append(Category(cate=syl))

re1.append(Pic(picname='电脑', picpath='bibianyin/diannao.jpg'))
re1.append(Pic(picname='年轮', picpath='bibianyin/nianlun.jpg'))
re1.append(Pic(picname='牛奶', picpath='bibianyin/niunai.jpg'))
re1.append(Pic(picname='森林', picpath='bibianyin/senlin.jpg'))
re1.append(Pic(picname='蜗牛', picpath='bibianyin/woniu.jpg'))

re1.append(Pic(picname='炒面', picpath='pingqiaoshe/chaomian.jpg'))
re1.append(Pic(picname='茶叶', picpath='pingqiaoshe/chaye.jpg'))
re1.append(Pic(picname='红枣', picpath='pingqiaoshe/hongzao.jpg'))
re1.append(Pic(picname='汽车', picpath='pingqiaoshe/qiche.jpg'))
re1.append(Pic(picname='狮子', picpath='pingqiaoshe/shizi.jpg'))
re1.append(Pic(picname='手机', picpath='pingqiaoshe/shouji.jpg'))
re1.append(Pic(picname='梳子', picpath='pingqiaoshe/shuzi.jpg'))
re1.append(Pic(picname='西红柿', picpath='pingqiaoshe/xihongshi.jpg'))
re1.append(Pic(picname='钻石', picpath='pingqiaoshe/zuanshi.jpg'))
re1.append(Pic(picname='钉子', picpath='qianhoubi/dingzi.jpg'))
re1.append(Pic(picname='枫叶', picpath='qianhoubi/fengye.jpg'))
re1.append(Pic(picname='苹果', picpath='qianhoubi/pingguo.jpg'))
re1.append(Pic(picname='乒乓球', picpath='qianhoubi/pingpangqiu.jpg'))
re1.append(Pic(picname='台灯', picpath='qianhoubi/taideng.jpg'))
re1.append(Pic(picname='星星', picpath='qianhoubi/xingxing.jpg'))
re1.append(Pic(picname='奥特曼', picpath='add1/aoteman.jpg'))
re1.append(Pic(picname='杯子', picpath='add1/beizi.jpg'))
re1.append(Pic(picname='冰淇淋', picpath='add1/bingqilin.jpg'))
re1.append(Pic(picname='电视机', picpath='add1/dianshiji.jpg'))
re1.append(Pic(picname='鸡蛋', picpath='add1/jidan.jpg'))
re1.append(Pic(picname='积木', picpath='add1/jimu.jpg'))
re1.append(Pic(picname='鲸鱼', picpath='add1/jingyu.jpg'))
re1.append(Pic(picname='橘子', picpath='add1/juzi.jpg'))
re1.append(Pic(picname='恐龙', picpath='add1/konglong.jpg'))
re1.append(Pic(picname='孔雀', picpath='add1/kongque.jpg'))
re1.append(Pic(picname='老虎', picpath='add1/laohu.jpg'))
re1.append(Pic(picname='猫', picpath='add1/mao.jpg'))
re1.append(Pic(picname='蚂蚁', picpath='add1/mayi.jpg'))
re1.append(Pic(picname='面包', picpath='add1/mianbao.jpg'))
re1.append(Pic(picname='绵羊', picpath='add1/mianyang.jpg'))
re1.append(Pic(picname='米饭', picpath='add1/mifan.jpg'))
re1.append(Pic(picname='奶瓶', picpath='add1/naiping.jpg'))
re1.append(Pic(picname='盆景', picpath='add1/penjing.jpg'))
re1.append(Pic(picname='蒲公英', picpath='add1/pugongying.jpg'))
re1.append(Pic(picname='扑克牌', picpath='add1/pukepai.jpg'))
re1.append(Pic(picname='铅笔', picpath='add1/qianbi.jpg'))
re1.append(Pic(picname='青蛙', picpath='add1/qingwa.jpg'))
re1.append(Pic(picname='气球', picpath='add1/qiqiu.jpg'))
re1.append(Pic(picname='秋千', picpath='add1/qiuqian.jpg'))
re1.append(Pic(picname='扇子', picpath='add1/shanzi.jpg'))
re1.append(Pic(picname='时钟', picpath='add1/shizhong.jpg'))
re1.append(Pic(picname='手表', picpath='add1/shoubiao.jpg'))
re1.append(Pic(picname='手电', picpath='add1/shoudian.jpg'))
re1.append(Pic(picname='手套', picpath='add1/shoutao.jpg'))
re1.append(Pic(picname='书包', picpath='add1/shubao.jpg'))
re1.append(Pic(picname='糖果', picpath='add1/tangguo.jpg'))
re1.append(Pic(picname='香蕉', picpath='add1/xiangjiao.jpg'))
re1.append(Pic(picname='橡皮擦', picpath='add1/xiangpica.jpg'))
re1.append(Pic(picname='小狗', picpath='add1/xiaogou.jpg'))
re1.append(Pic(picname='眼镜', picpath='add1/yanjing.jpg'))
re1.append(Pic(picname='椅子', picpath='add1/yizi.jpg'))
re1.append(Pic(picname='月亮', picpath='add1/yueliang.jpg'))
re1.append(Pic(picname='蜘蛛', picpath='add1/zhizhu.jpg'))
re1.append(Pic(picname='字典', picpath='add1/zidian.jpg'))
re1.append(Pic(picname='足球', picpath='add1/zuqiu.jpg'))
re1.append(Pic(picname='鹅', picpath='add2/e.jpg'))

lists = ['电脑', '年轮', '牛奶', '森林', '蜗牛','炒面','茶叶','红枣','汽车','狮子','手机','梳子','西红柿','钻石','钉子',
             '枫叶','苹果','乒乓球','台灯','星星', '奥特曼', '杯子', '冰淇淋', '电视机', '鸡蛋', '积木',
             '鲸鱼', '橘子', '恐龙', '孔雀', '老虎', '猫', '蚂蚁', '面包', '绵羊', '米饭', '奶瓶', '盆景',
             '蒲公英', '扑克牌', '铅笔', '青蛙', '气球', '秋千', '扇子', '时钟', '手表', '手电', '手套',
             '书包', '糖果', '香蕉', '橡皮擦', '小狗', '眼镜', '椅子', '月亮', '蜘蛛', '字典', '足球', '鹅']

if __name__ == '__main__':
    with session_scope(DB_CONNECT_STRING) as session:
       session.add_all(re1)


    for list in lists:
        categorize2db(list)
    #categorize2db(list2)


