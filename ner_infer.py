import os 
import sys
sys.path.append("/home/data_normal/nlp/xuhao/xcxhy/Automatic_Delivery")
import spacy
from tqdm import tqdm
from spacy.tokens import DocBin
from util import get_lemmatize
from util import *


class NER_INFER(object):
    def __init__(self,model_path="./model-best"):
        self.best_nlp = spacy.load(model_path)

    def detector(self,text):
        result = []
        doc = self.best_nlp(text)
        for ent in doc.ents:
            result.append((ent.text, ent.label_))
        return result

if __name__=='__main__':
    ner = NER_INFER()
    text = "Auto Parts for Honda Civic Type R Style Rear Spoiler 2006-2011"
    text_list = list(map(get_lemmatize, text.lower().split(" ")))
    text_l = " ".join(text_list)
    print(text_l)
    print(ner.detector(text_l))
    text = (("Engine Parts for Honda Like Engine Mounting/Engine Mount 50820-Sva-A05 (A4530) , 50880-Sna-A81, 50890-Sna-A81, 50850-Sna-A82 for Honda Civic 2006-2011 Assy (AT)").lower())
    print(ner.detector(text))
    text = ("Headlight Headlamp Switch 97061353309dml 97061353308 97061353309 for Porsche").lower()
    print(ner.detector(text))

    # path = "/home/data_normal/nlp/xuhao/xcxhy/Automatic_Delivery/Text_only/text_ner/data/real_ner_dict.pkl"
    # model_path = "/home/data_normal/nlp/xuhao/xcxhy/Automatic_Delivery/Text_only/text_ner/model-best"
    # data = read_pkl(path)
    # test_data = data["annotations"][-1000:]
    
    # with open("/home/data_normal/nlp/xuhao/xcxhy/Automatic_Delivery/Text_only/text_ner/data/test.txt", 'a') as f:
    #     for test_example in tqdm(test_data):
    #         manual = []
    #         text = test_example['text']
    #         labels = test_example['entities']
    #         predict = ner.detector(text)
    #         for start, end, label in labels:
    #             manual.append((text[start:end], label.upper()))
    #         f.write('text : {}'.format(text) + '\n')
    #         f.write('manual : {}'.format(manual) + '\n')
    #         f.write('predict : {}'.format(predict) + '\n')
    #         f.write('\n')
            
        

    
