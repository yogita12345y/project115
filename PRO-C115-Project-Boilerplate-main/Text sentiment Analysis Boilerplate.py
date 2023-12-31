# -*- coding: utf-8 -*-
"""PRO-C115-Project-Boilerplate.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-Q2e9EPhBXHNnl8HmFYtSrYGKzKvF4Zd
"""

# Load the dataset from Github repository
!git clone https://github.com/yogita12345y/project-116.git

# Make a dataframe using the 'pandas' module
import pandas as pd
dataframe = pd.read_excel('/content/product_dataset/updated_product_dataset.xlsx')
print(dataframe.head())

# Get unique emotions from the 'Emotion' column in the Dataset
dataframe["Emotion"].unique()

# Add Labels to the dataset
encode_emotions = {"Neutral": 0, "Positive": 1, "Negative": 2}

# replace the emotions with the Label
dataframe.replace(encode_emotions, inplace = True)
dataframe.head()

# Convert the dataframe into list for easy processing
training_sentences = []
training_labels = []

for i in range(len(dataframe)):
  sentence = dataframe.loc[i, "Text"]
  training_sentences.append(sentence)
  label = dataframe.loc[i, "Emotion"]
  training_labels.append(label)

# printing 10th element
training_sentences[10], training_labels[10]

# Tokenize and pad your data
import tensorflow as tf

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

vocab_size = 10000
embedding_dim = 16
max_length = 100
trunc_type='post'
padding_type='post'
oov_tok = "<OOV>"
training_size = 20000

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(training_sentences)

word_index = tokenizer.word_index

training_sequences = tokenizer.texts_to_sequences(training_sentences)
training_padded = pad_sequences(training_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

# Converting to numpy array
import numpy as np

training_padded = np.array(training_padded)
training_labels = np.array(training_labels)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,Conv1D,LSTM,MaxPooling1D,Dense,Dropout

model=tf.keras.Sequential([
    Embedding(vocabsize,embeding_dim,input_length=100),
    Dropout(0.2),
    Conv1D(filters=256,kernel_size=3,activation="relu"),
    MaxPooling1D(pool_size=3),
    Conv1D(filters=128,kernel_size=3,activation="relu"),
    MaxPooling1D(pool_size=3),
    LSTM(128),
    Dense(128,activation="relu"),
    Dropout(0.2),
    Dense(64,activation="relu"),
    Dense(6,activation="softmax")
])
model.compile(loss="sparse_categorical_crossentropy",optimizer="adam",metrics=["accuracy"])
model.summary()

# Get model Summary before training

# Train your Model

# Save your Model

# Test your model to make predictions