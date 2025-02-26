import json

emp={'id':101,'name':'ajinkya','salary':100000,'married':False,'childs':None}

def serialization_1():

    js=json.dumps(emp)
    return js

def serialization_2():
    with open('serializationfile.txt','w') as fp:
        data=json.dump(emp,fp)
    return data


