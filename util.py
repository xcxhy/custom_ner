import os
import json
import pickle

def read_pkl(path):
    try:
        with open(path, 'rb') as f:
            data = pickle.load(f)
        return data
    except:
        print("read pkl error!")
        return
def write_pkl(path, data):
    try:
        with open(path, 'wb') as f:
            pickle.dump(data, f)
        print("write {} end!".format(path))
        return
    except:
        print("write error!")
        return

def read_list_txt(path):
    with open(path, 'r') as f:
        data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip('\n')
    return data

def write_list_txt(path, data):
    with open(path, 'w') as f:
        for value in data:
            f.write(value +"\n")
    return

def read_dict_json(path):
    with open(path,'r+') as file:
        content=file.read()
    content=json.loads(content)
    return content

def write_dict_json(path, data):
    dict_json=json.dumps(data, indent = 4)#转化为json格式文件
    #将json文件保存为.json格式文件
    with open(path,'w') as file:
        # json.dump(dict_json, file, indent = 4)
        file.write(dict_json)
    return