import tensorflow as tf
import keras
from keras import layers
from keras.layers.experimental import preprocessing
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split


df = pd.read_csv("file1.csv", index_col=0)
df = sklearn.utils.shuffle(df)
df_features = df
df_label = df_features.pop("Result")

df_features = np.array(df_features)

X_train, X_test, y_train, y_test = train_test_split(
    df_features, df_label, test_size=0.33)

normalize = preprocessing.Normalization()
normalize.adapt(df_features)

blackjack_model = tf.keras.Sequential([
    normalize,
    layers.Dense(64, activation='relu'),
    # keras.layers.Dropout(0.2),
    layers.Dense(64),
    layers.Dense(1)
])

blackjack_model.compile(loss = tf.losses.MeanSquaredError(),
                      optimizer = tf.optimizers.Adam())

blackjack_model.fit(X_train, y_train, epochs=10, 
    validation_data=(X_test, y_test))

np.round(blackjack_model.predict([[2,0,3,13]]))[0][0]

blackjack_model.save('saved_model/blackjack_model')