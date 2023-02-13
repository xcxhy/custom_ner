import os
import argparse
import pickle

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Demo of argparse')
    parser.add_argument('--nums', type=int, default=0)
    parser.add_argument('--data_dir', type=str, default="/Users/xcxhy/Github_folder/custom_ner/dataset")
    args = parser.parse_args()

    file_name = "ner_"
    dict_dir = args.data_dir
    nums = [i for i in range(args.nums)]
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