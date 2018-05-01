import json
from datetime import datetime
from sqlalchemy.ext.declarative import DeclarativeMeta



def new_alchemy_encoder():
    _visited_objs = []

    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if obj in _visited_objs:
                    return None
                _visited_objs.append(obj)

                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    data = obj.__getattribute__(field)
                    try:
                        if isinstance(data, datetime):
                            data = data.strftime('%Y-%m-%d %H:%M:%S')
                        json.dumps(data)  # this will fail on non-encodable values, like other classes
                        fields[field] = data
                    except TypeError:
                        fields[field] = None
                return fields

            return json.JSONEncoder.default(self, obj)

    return AlchemyEncoder

def alchemy2json(datas):   #obj to json call this
    host = []
    for data in datas:
        host.append(data)

    return json.dumps(host, cls=new_alchemy_encoder(), check_circular=True, ensure_ascii=False)


def dataToDic(keys, datas):   # keys is the key names list, datas contains the value tuple
    results = []

    if isinstance(datas, list):
        for data in datas:
            dic = {}
            for i in range(len(keys)):
                dic[keys[i]] = data[i]
            results.append(dic)

    elif isinstance(datas, tuple):
        dic = {}
        for i in range(len(keys)):
            dic[keys[i]] = datas[i]
        results.append(dic)


    return results