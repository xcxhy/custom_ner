import os
import spacy
import spacy
import pickle
import time
from tqdm import tqdm
from sacred import Experiment
from spacy import displacy
from spacy.tokens import DocBin
from spacy.util import filter_spans
from util import *

ex = Experiment('training')

def train(training_data):
    nlp = spacy.blank('en')
    doc_bin = DocBin()
    skip = 0
    for training_example in tqdm(training_data['annotations']):
        text = training_example['text']
        labels = training_example['entities']
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in labels:
            span = doc.char_span(start, end, label=label, alignment_mode='contract')
            if span is None:
                skip+=1
            else:
                ents.append(span)
        filtered_ents = filter_spans(ents)
        doc.ents = filtered_ents
        doc_bin.add(doc)
    doc_bin.to_disk("training_data.spacy")
    print("Skipping:",skip)
@ex.config
def config():
    path = "./dataset/new_real_ner_dict.pkl"
    type = "pkl"
_config = config()

@ex.automain
def main(_config):
    if _config['type'] == "pkl":
        with open(_config["path"], 'rb') as f:
            data = pickle.load(f)
    elif _config['type'] == "json":
        data = read_dict_json(_config["type"])
    train(data)
    if os.path.exists("base_config.cfg"):
        os.system("python -m spacy init fill-config base_config.cfg config.cfg")
    else:
        os.system("curl -o base_config.cfg https://gist.githubusercontent.com/vinothpandian/d821b2ffd47682aa436a831e7e3e333e/raw/c15dd08676ece5df4e181d02499952d88d062de8/base_config.cfg")
        os.system("python -m spacy init fill-config base_config.cfg config.cfg")
    os.system("python -m spacy train config.cfg --output ./ --paths.train ./training_data.spacy --paths.dev ./training_data.spacy --gpu-id -1")
    print("Train Over!")
    