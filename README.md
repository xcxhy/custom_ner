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

 If you have both sentences and entity words, you might as well use the get_ner_dataset.py to directly generate the files needed for training through matching.
 **Attention:** This requires you to use the category you want to identify to name the file, for example, we use "brand.txt" to name the brand entity.
