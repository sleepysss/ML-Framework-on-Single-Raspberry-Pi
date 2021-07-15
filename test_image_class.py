import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import cv2

#load model
model=load_model('//home//pi//pythonpython//file_1.h5')

#our testing image
test_images=[]
img=cv2.imread('//home//pi//Pictures//cat//catcat//cat.21.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img=cv2.resize(img,(150,150))
test_images.append(img)

test_images=np.array(test_images)
test_images=test_images.astype('float32')/255
predict=model.predict_classes(test_images)
print("class0:cat  class1:dog")
print("predict class of the test image: ",predict)