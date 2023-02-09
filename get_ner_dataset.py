import os
import sys
from copy import copy, deepcopy
sys.path.append("/home/data_normal/nlp/xuhao/xcxhy/Knowledge_Graph/")
import pickle
import json
import re
from sacred import Experiment
import pandas as pd
import numpy as np
from collections import Counter
from tqdm import tqdm 
from itertools import chain
from util import *



ex = Experiment("NER_DATA")


class NER_Dataset(object):
    def __init__(self,config):
        self.entity_path = config['entity_path']

        # self.brand_path = config["brand_path"]
        # self.model_path = config["model_path"]
        # self.specification_path = config["specification_path"]
        self.text_path = config["text_path"]
        self.save_dir = config["save_dir"]
        self.nums = config['nums']
        self.batch = config['batch']
        self.class_path = config["class_path"]
        self.text = self.read_text()
        self.classes = self.read_class()
        self.entity_names, self.entities = self.read_keywords()
            
    def read_text(self):
        prodid_to_prodname_dict = pickle.load(open(self.text_path, "rb"))
        text = [j[0] for i,j in prodid_to_prodname_dict.items()]
        return text
    
    def read_class(self):
        return read_list_txt(self.class_path)
    
    def read_keywords(self):
        result = []
        for root, dirs, files in os.walk(self.entity_path):
            file_name = files
        
        paths = [os.path.join(self.entity_path, name) for name in file_name]
        for path in paths:
            data = read_list_txt(path)
            # path_list = path.split('/')
            # file_name = os.path.splitext(path_list[-1])[0]
            # vars()[file_name] = data
            result.append(self.b_words(data))
        names = [name.split(".")[0] for name in file_name]
        return names, result
    
    def b_words(self, match_words):
        for i in range(len(match_words)):
            match_words[i] = '\\b' + match_words[i] + "\\b"
        return match_words

    def match_words(self, text, match_words):
        result = []
        for word in match_words:
            is_matches = re.findall(word, text)
            if is_matches != []:
                matches = re.finditer(word, text)
                for i in matches:
                    res = i.span()
                    result.append(res)
        return result
    
    # def match_regulation(self, values):
    #     return
    
    def get_dataset(self):
        methods = self.entity_names
        training_data = {"classes" : [method.upper() for method in methods] , "annotations" : []}
        lemmatize_sentences = []
        
        for sentence in tqdm(self.text[self.nums*self.batch:(self.nums+1)*self.batch]):
            temp_dict = {}
            sentence_list = sentence.strip().split(' ')
            lemma_sentence_list = list(map(get_lemmatize, sentence_list))
            try:
                single_sentence = " ".join(lemma_sentence_list).lower()
            except:
                continue
            lemmatize_sentences.append(single_sentence)
            
            temp_dict['entities'] = []
            for i in range(len(methods)):
                data = self.entities[i]
                single_entity = self.match_words(single_sentence, data)
                if len(single_entity) == 0:
                    continue
                for value in single_entity:
                    start, end, label = int(value[0]), int(value[1]), methods[i].upper()
                    temp_dict['entities'].append((start, end, label))
            if len(temp_dict['entities']) == 0:
                continue
            else:
                temp_dict['text'] = single_sentence
            # for method in methods:
            #     if method == 'entities':
            #         data = self.entities
            #         single_entity = self.match_words(single_sentence, data)

            #     elif method == 'brands':
            #         data = self.brands
            #         single_brand = self.match_words(single_sentence, data)
                    
            #     elif method == 'models':
            #         data = self.models
            #         single_model = self.match_words(single_sentence, data)
            # if single_entity == [] and single_brand == [] and single_model == []:
            #     continue
            # else:
            #     temp_dict['text'] = single_sentence
            #     for value1 in single_entity:
            #         start1, end1, label1 = int(value1[0]), int(value1[1]), "PRODUCT"
            #         temp_dict['entities'].append((start1, end1, label1))
            #     for value2 in single_brand:
            #         start2, end2, label2 = int(value2[0]), int(value2[1]), "BRAND"
            #         temp_dict['entities'].append((start2, end2, label2))
            #     for value3 in single_model:
            #         start3, end3, label3 = int(value3[0]), int(value3[1]), "MODEL"
            #         temp_dict['entities'].append((start3, end3, label3))
                
                    
                # elif method == 'specifications':
                #     data = self.specifications
                #     res = self.match_words(single_sentence, data)
                    # data = vars()[method]
            training_data['annotations'].append((temp_dict))
            # regulation_result = self.match_regulation(sentence_result)
            # result.append(regulation_result)
        
        return training_data
    
    
    def save_file(self):
        ner_data = self.get_dataset()
        # js_ner = json.loads(ner_data)
        
        with open(os.path.join(self.save_dir, "ner_{}.pkl".format(str(self.nums))), 'wb') as f:
            pickle.dump(ner_data, f)
        return
    

@ex.config
def ner_data_config():
    entity_path = "./dataset/entity"
    class_path = "./dataset/class.txt"
    # entity_path = "/home/data_normal/nlp/xuhao/xcxhy/Knowledge_Graph/counter_query_freq/dict/entities.txt"
    # brand_path = "/home/data_normal/nlp/xuhao/xcxhy/Knowledge_Graph/counter_query_freq/dict/brands.txt"
    # model_path = "/home/data_normal/nlp/xuhao/xcxhy/Knowledge_Graph/counter_query_freq/dict/models.txt"
    # specification_path = "/home/data_normal/nlp/xuhao/xcxhy/Knowledge_Graph/counter_query_freq/dict/specifications.txt"
    text_path = "/Users/xcxhy/AIProject/dataset/ner/prodid_to_prodname_dict.pkl"
    save_dir = "./dataset"
    nums = 0
    batch = 500000
    
_config = ner_data_config()

@ex.automain
def main(_config):
    ner = NER_Dataset(_config)
    ner.get_dataset()
    ner.save_file()
    