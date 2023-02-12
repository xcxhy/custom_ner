#!/bin/bash

cd /home/data_normal/nlp/xuhao/xcxhy/Knowledge_Graph/counter_query_freq/ner_dataset

nohup python get_ner_dataset.py with nums=0 > result/result0 & \
# nohup python get_ner_dataset.py with nums=1 > result/result1 & \
# nohup python get_ner_dataset.py with nums=2 > result/result2 & \
# nohup python get_ner_dataset.py with nums=3 > result/result3 & \