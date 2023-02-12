# custom_ner
Use our code can easy to train a custom new model to infer.

this project is implemented based on [spacy](https://github.com/explosion/spaCy).So I'm just a porter.

First you can use the test.py to ner some car brands, types and component.
For the model, we use a small amount of manual annotation.

We simply extracted a part of car brands, types and component from the wiki, manually labeled them with a small amount, and then matched them from the text to automatically create a NER dataset. This eliminates the need to use such NER annotation tools.

General annotation tools likes, 

[Doccano](https://doccano.herokuapp.com)

[Tagtog](https://www.tagtog.net)

[LightTag](https://www.lighttag.io)

[Prodigy](https://demo.prodi.gy/?=null&view_id=ner_manual)

 If you have both sentences and entity words, you might as well use the **get_ner_dataset.py** to directly generate the files needed for training through matching.

```
python get_ner_dataset.py
```

You can modify your file location and other parameters in the ner_data_config() function in the file, and there are corresponding annotations. This is a code that can use multi-process to speed up the operation, so nums and batch are particularly important. If your data volume Not much, you can directly set nums to 0 when using a single process, and set batch to the length of your data.

Also you can use this code to set the parameters, but note that there must be no spaces before and after "="

```
python get_ner_dataset.py with entity_path="./dataset/entity" \                                         
class_path="./dataset/class.txt" text_type='pkl' \  
text_path="/Users/xcxhy/AIProject/dataset/ner/prodid_to_prodname_dict.pkl" \ 
save_dir="./dataset" nums=0 batch=500000  
```

 **Attention:** This requires you to use the category you want to identify to name the file, for example, we use "brand.txt" to name the brand entity.
