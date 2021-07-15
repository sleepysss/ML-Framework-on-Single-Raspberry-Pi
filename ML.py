from tensorflow.keras.utils import to_categorical
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
import numpy as np
import os
import cv2
from sklearn.model_selection import train_test_split
#from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications import inception_v3

#####################
#     first part    #
#####################

#read the file and label 
#label cat:0 dog:1
train_images=[]
train_labels=[]

path1='//home//pi//Pictures//cat//catcat'
path2='//home//pi//Pictures//dog//dogdog'
#cat
for file in os.listdir(path1):
    print(file)
    img=cv2.imread(path1+'//'+file)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img=cv2.resize(img,(150,150))
    train_images.append(img)
    train_labels.append(0)
#dog   
for file in os.listdir(path2):
    print(file)
    img=cv2.imread(path2+'//'+file)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img=cv2.resize(img,(150,150))
    train_images.append(img)
    train_labels.append(1)
    
train_images=np.array(train_images)
train_labels=np.array(train_labels)
#split dataset to test(20%in200) and train(80%in200) image
x_train,x_test,y_train,y_test=train_test_split(train_images,train_labels,test_size=0.2,random_state=33)


######################
#     second part    #
######################

#preprocess
x_train=x_train.astype('float32')/255
x_test=x_test.astype('float32')/255
y_train=to_categorical(y_train)
y_test=to_categorical(y_test)

#####################
#     third part    #
#####################

#build the model
'''
vgg16=VGG16(include_top=False,weights='imagenet',input_shape=(150,150,3))
vgg16.trainable=False
model=tf.keras.Sequential()
model.add(vgg16)
model.add(Flatten())
model.add(Dense(512,activation='relu',input_dim=4*4*512))
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2,activation='sigmoid'))
model.summary()
'''
inv3=inception_v3.InceptionV3(include_top=False,weights='imagenet',input_shape=(150,150,3))
inv3.trainable=False
model=tf.keras.Sequential()
model.add(inv3)
model.add(Flatten())
model.add(Dense(512,activation='relu',input_dim=3*3*2048))
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2,activation='sigmoid'))
model.summary()


model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['acc'])
#train model
history=model.fit(x_train,y_train,epochs=3,batch_size=50)

#######################
#     fourth part     #
#######################

#predict & test
print('testing...')
test_loss,test_acc=model.evaluate(x_test,y_test)
print('test acc:',test_acc)


#######################
#     fifth part     #
#######################

#save the model
model.save('//home//pi//Documents//model.h5')
