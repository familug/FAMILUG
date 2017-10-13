#!/usr/bin/env python3

from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
import numpy
from numpy import genfromtxt

seed = 7
numpy.random.seed(7)

# data from https://ctf.cyradar.com/#machine-learning
train = genfromtxt('/home/hvn/me/notebook/train.csv', delimiter=',')
train = train[1:, :]
X_data, y_data = train[:, 1:], train[:, 0]
X_data = X_data/255
print(y_data)
y_data = np_utils.to_categorical(y_data)
num_pixels = X_data.shape[1]

# split dataset to train and test
# Standard MNIST has rate 6:1 for Train vs Test
pivot = int(X_data.shape[0] / 7 * 6)
X_train, y_train = X_data[:pivot], y_data[:pivot]
X_test, y_test = X_data[pivot:], y_data[pivot:]
print('Train/Test size: ', X_train.shape, X_test.shape)

num_classes = y_train.shape[1]


def baseline_model():
    # create model
    model = Sequential()
    model.add(Dense(num_pixels, input_dim=num_pixels, kernel_initializer='normal', activation='relu'))
    model.add(Dense(num_classes, kernel_initializer='normal', activation='softmax'))
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


# build the model
model = baseline_model()
# Fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=200, verbose=2)
# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("Baseline Error: %.2f%%" % (100-scores[1]*100))

mydata = genfromtxt('/home/hvn/me/notebook/answer.csv', delimiter=',')
r = mydata[1:, :] / 255
model.predict(r)
kq = model.predict(r)
print(kq.argmax(1))
