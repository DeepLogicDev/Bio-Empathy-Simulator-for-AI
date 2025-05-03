import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from sklearn.model_selection import train_test_split

df = pd.read_csv('../datasets/emotions/fer2013.csv')
X = np.array([np.fromstring(pixels, sep=' ') for pixels in df['pixels']])
X = X.reshape(-1, 48, 48, 1).astype('float32') / 255.0
y = tf.keras.utils.to_categorical(df['emotion'], num_classes=7)

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.1)

model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(48,48,1)),
    MaxPooling2D(),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(7, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=15, batch_size=64)

model.save('models/emotion_model.h5')
