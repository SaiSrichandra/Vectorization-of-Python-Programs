#!/usr/bin/env python

# internal modules
import hasy_tools
import numpy as np
# 3rd party modules
from keras.callbacks import CSVLogger, ModelCheckpoint
from keras.layers import Dense, Flatten
from keras.models import Sequential

# Load the data
data = hasy_tools.load_data()

x_train = data["x_train"]
y_train = data["y_train"]
x_test = data["x_test"]
y_test = data["y_test"]

# One-Hot encoding
y_train = np.eye(hasy_tools.n_classes)[y_train.squeeze()]
y_test = np.eye(hasy_tools.n_classes)[y_test.squeeze()]

# Preprocessing
x_train = hasy_tools.preprocess(x_train)
x_test = hasy_tools.preprocess(x_test)

# Define the model
model = Sequential()
model.add(Flatten())
model.add(Dense(256))
model.add(Dense(hasy_tools.n_classes, activation="softmax"))

# Compile model
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Fit the model
csv_logger = CSVLogger("log.csv", append=True, separator=";")
checkpointer = ModelCheckpoint(
    filepath="checkpoint.h5", verbose=1, period=10, save_best_only=True
)
model.fit(
    x_train, y_train, epochs=500, batch_size=128, callbacks=[csv_logger, checkpointer]
)

# Serialize model
model.save("model.h5")

# evaluate the model
scores = model.evaluate(x_test, y_test)
print("\n{}: {:.2f}%".format(model.metrics_names[1], scores[1] * 100))
