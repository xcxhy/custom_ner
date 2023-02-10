import os
import pickle

if __name__=='__main__':
    dict_dir = "/home/data_normal/nlp/xuhao/xcxhy/Knowledge_Graph/counter_query_freq/ner_dataset"
    file_name = "ner_"
    nums = [i for i in range(3)]
    for i in nums:
        if i == 0:
            use_path = os.path.join(dict_dir, (file_name + str(i) + '.pkl'))
            with open(use_path, 'rb') as tf:
                use_dict = pickle.load(tf)
        else:
            use_path = os.path.join(dict_dir, (file_name + str(i) + '.pkl'))
            with open(use_path, "rb") as tf:
                temp_dict = pickle.load(tf)
            use_dict['annotations'] = use_dict['annotations'] + temp_dict['annotations']
    
    with open(os.path.join(dict_dir, 'new_real_ner_dict.pkl'), "wb") as f:
        pickle.dump(use_dict, f)