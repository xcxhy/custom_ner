import spacy
import os
import pickle
import time
from tqdm import tqdm
from spacy import displacy
from spacy.tokens import DocBin
from spacy.util import filter_spans

def split_train(path, training_data, index):
    if index == 0:
        nlp = spacy.blank("en")
    else:
        nlp = spacy.load(path)
    doc_bin = DocBin()
    Skip = 0
    for training_example in tqdm(training_data):
        text = training_example["text"]
        labels = training_example['entities']
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in labels:
            span = doc.char_span(start, end, label=label) #  alignment_mode="contract"
            if span is None:
                Skip += 1
            else:
                ents.append(span)
        filtered_ents = filter_spans(ents)
        doc.ents = filtered_ents
        doc_bin.add(doc)
    doc_bin.to_disk("/home/data_normal/nlp/xuhao/xcxhy/Automatic_Delivery/Text_only/text_ner/training_data.spacy")
    print("skip:", Skip)

if __name__=='__main__':
    nums = 5
    path = "/home/data_normal/nlp/xuhao/xcxhy/Automatic_Delivery/Text_only/text_ner/data/real_ner_dict.pkl"
    model_path = "/home/data_normal/nlp/xuhao/xcxhy/Automatic_Delivery/Text_only/text_ner/model-best"
    # os.system("curl -o base_config.cfg https://gist.githubusercontent.com/vinothpandian/d821b2ffd47682aa436a831e7e3e333e/raw/c15dd08676ece5df4e181d02499952d88d062de8/base_config.cfg")
    # os.system("python -m spacy init fill-config base_config.cfg config.cfg")
    with open(path, "rb") as f:
        data = pickle.load(f)
    for index in range(nums):
        split_train(model_path, data['annotations'][index*1000:(index+1)*1000], index)
        time.sleep(10)
        os.system("python -m spacy train config.cfg --output ./ --paths.train ./training_data.spacy --paths.dev ./training_data.spacy --gpu-id 2")
        time.sleep(10)
    print("Train Over!")