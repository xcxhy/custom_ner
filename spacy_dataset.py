import os
import pickle
import argparse
from sacred import Experiment
import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
from util import *
from spacy.util import filter_spans

ex = Experiment("process!")

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
    
    
        
        
    