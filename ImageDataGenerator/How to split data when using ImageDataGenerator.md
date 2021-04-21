# How to split data with ImageDataGenerator flowed out from a single directory

**even not split directory directly**

---



We can easily use this code below to use data in a directory.

I also coded it with keras.It is not a big deal but it is how to split again for having three generators .



```python
from keras.preprocessing.image import ImageDataGenerator

random_seed = 414

datagen_first = ImageDataGenerator(rescale = 1./255, validation_split=0.2)

train_generator = datagen_first.flow_from_directory(image_dir,target_size = (640, 640), seed=random_seed,
                                                    batch_size = 1, class_mode = 'binary', subset='training')
test_generator = datagen_first.flow_from_directory(image_dir, target_size=(640, 640), seed=random_seed,
                                              batch_size=1, class_mode='binary', subset='validation')

```

This is not a big deal, but how to split again for three generators .  I need three dataset, train, valid and test data, for training and evaluating a model.  There is a way. Let's go to find the way to split it to three pieces.



I have dataset which contains data and labels in a single directory.

The first I can is to flow out all data  from a single directory using validation_split. Now I have two, train_generator and test_generator, 8:2.  







```python
data, labels = train_generator.next()
```

I will try again to split train_generator to two parts, train and validation. 

Before doing that, I have to separate data and labels in train_generator with  next() function.

The type of data and labels is array so I can flow these out again using  an ImageDataGenerator function







```python
datagen_second = ImageDataGenerator(validation_split=0.2)

train_generator = datagen_second.flow(data, labels, seed=random_seed, batch_size = 1 subset='training')
valid_generator = datagen_second.flow(data, labels , seed=random_seed, batch_size = 1, subset='validation')
```

Now use a flow function not a flow_from_directory function. 

And  with all data flowed out from data and labels I split it again in the proportion 8:2 

That's all. 

Now I have three data split from a single directory without splitting by myself a directory. 

