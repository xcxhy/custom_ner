#!/bin/bash

start=`date +%s`

cd /Users/xcxhy/Github_folder/custom_ner # The directory where the executable file is located

entity_path="./dataset/entity"  # The entities file 
class_path="./dataset/class.txt" # class file path
text_type='txt' # Type of text
text_path="./dataset/text.txt" # the text path
save_dir="./dataset" # The save dir
nums=0 # Use process nums
batch=500 # Amount of data handled by each process 

for ((i=0; i<=nums; i++))
do 
{
    nohup python get_ner_dataset.py with entity_path=$entity_path \
    class_path=$class_path text_type=$text_type text_path=$text_path \
    save_dir=$save_dir nums=$i batch=$batch > result/result${i}
}&
done
wait

python concat_dict.py --nums $nums --data_dir $save_dir

end=`date +%s`  #定义脚本运行的结束时间
 
echo "TIME:`expr $end - $start`"