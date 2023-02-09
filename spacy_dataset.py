import os
import pickle
import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
from spacy.util import filter_spans

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
if __name__ == '__main__':
    path = "/Users/xcxhy/AIProject/dataset/ner/new_real_ner_dict.pkl"
    with open(path, 'rb') as f:
        data = pickle.load(f)
    train(data)
    
    
        
        
    