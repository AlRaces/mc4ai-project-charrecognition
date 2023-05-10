import streamlit as st
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Input, Flatten
from tensorflow.random import set_seed
from tensorflow.keras.backend import clear_session

# cho người dùng chọn epoch, test size, train size 
# có 3 cái slidebar cho epoch, test size, train size. Khi nào người dùng chọn đủ 3 cái thì bấm nút submit, sau đó split train, test theo số lượng của người dùng rồi train model dựa trên epoch

clear_session()
set_seed(42)
np.random.seed(42)

model = Sequential()
model.add(Input(shape=X_train.shape[1:]))
model.add(Flatten())
model.add(Dense(62, activation='softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics='accuracy')
model.summary()

DATASET = np.load("np_dataset.npy")
LABELS = np.load("labels.npy")
NAMES = np.load("names.npy")
