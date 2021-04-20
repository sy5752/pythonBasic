from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import cv2

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(str(train_labels[0]))

for i in range (len(train_labels)):
    label = str(train_labels[0])
    cv2.imwrite('image/'+label+'_'+str(i)+'.jpg', train_images[i])
  
        

cv2.waitKey(0)
cv2.destroyAllWindows()

print(test_labels[0])

for i in test_images[0]:
    for j in i:
        if j > 0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()


train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)


model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])
 
 
model.fit(train_images, train_labels, epochs=5, batch_size=128)

print(model.predict(test_images[:1]))
 
 
# test_loss, test_acc = model.evaluate(test_images, test_labels)
# print('test_acc: ', test_acc)