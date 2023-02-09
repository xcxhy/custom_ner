import os
import json
import pickle
import sys
import spacy
import nltk
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer() 

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

def get_tag(text):
    sentence_taged = nltk.pos_tag(nltk.word_tokenize(text))
    return sentence_taged


def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None
# @profile
def get_lemmatize(text):
    # 获取单词的词性
    tokens = word_tokenize(text)   # 分词
    tagged_sent = pos_tag(tokens)  # 获取单词词性
    
    lemmas_sent = []
    for tag in tagged_sent:
    
        wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN  # tag[1]指单词词性
        # if len(tag[0]) < 3 and tag[0].endswith('s'):
        #     lemmas_sent.append(tag[0])
        
        # else:
        lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos)) 
    if lemmas_sent == []:
        return 0 # tag[0]指单词本身
    return  lemmas_sent[0]  
