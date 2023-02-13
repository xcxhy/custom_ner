
import spacy
import spacy
import os
import pickle
import time
from tqdm import tqdm
from spacy import displacy
from spacy.tokens import DocBin
from spacy.util import filter_spans

if __name__==" __main__":
    os.system("curl -o base_config.cfg https://gist.githubusercontent.com/vinothpandian/d821b2ffd47682aa436a831e7e3e333e/raw/c15dd08676ece5df4e181d02499952d88d062de8/base_config.cfg")
    os.system("python -m spacy init fill-config base_config.cfg config.cfg")
    os.system("python -m spacy train config.cfg --output ./ --paths.train ./training_data.spacy --paths.dev ./training_data.spacy --gpu-id 0")
    print("Train Over!")