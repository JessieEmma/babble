# -*- coding: UTF-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ColumnDefault, Integer, String, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

db_string = 'mysql+pymysql://root:root@localhost:3306/dbabble?charset=utf8'

Base = declarative_base()


class Userp(Base):
    # 表的名字
    __tablename__ = 'userp'

    # 表的结构
    telephone = Column(String(20), primary_key=True)
    password = Column(String(30), nullable=False)

    p_c = relationship('Userc', lazy='dynamic')

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False


class Userc(Base):
    __tablename__ = 'userc'

    user_id = Column(Integer, primary_key=True, autoincrement=True, index=True)  #increment automatically
    telephone = Column(String(20), ForeignKey('userp.telephone'))
    nickname = Column(String(20))
    birthyear = Column(String(10), nullable=False)
    gender = Column(Integer, default=0, nullable=False)  #0 is boy, 1 is girl
    info = Column(Text(100))
    scores = Column(Integer, default=0, nullable=False)
    models = Column(String(50))

    def __repr__(self):
        return 'user_id is' + self.user_id

class Pic(Base):
    __tablename__ = 'pic'

    pic_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    picname = Column(String(20), nullable=False)
    picpath = Column(String(50), nullable=False)

    cate_pic = relationship('CatePic', lazy='dynamic')

class Category(Base):
    __tablename__ = 'category'

    cate_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    cate = Column(String(20), nullable=False)

    cate_pic = relationship('CatePic', lazy='dynamic')

class CatePic(Base):
    __tablename__ = 'cate_pic'

    cate_id = Column(Integer, ForeignKey('category.cate_id'),primary_key=True)
    pic_id = Column(Integer, ForeignKey('pic.pic_id'), primary_key=True)


if __name__ == '__main__':
    # 初始化数据库连接:
    engine = create_engine(db_string, echo=True)


    def init_db():
        Base.metadata.create_all(engine)


    def drop_db():
        Base.metadata.drop_all(engine)


    drop_db()
    init_db()
