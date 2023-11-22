import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Generate dummy data for training
x_train = np.random.rand(1000, 20)
y_train = np.random.rand(1000, 1)

# Create the model using the Sequential API
model = Sequential()
model.add(Dense(64, input_dim=20, activation='relu'))
model.add(Dense(1, activation='linear'))

# Compile the model with a loss function and optimizer
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model on the training data
model.fit(x_train, y_train, epochs=100, batch_size=64)
