from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

x = np.array([5, 4, 6, 5, 5, 5, 6, 6, 2, 7, 7])  # Convert to NumPy array
y = np.array([85, 103, 70, 82, 89, 98, 66, 95, 169, 70, 48])  # Convert to NumPy array

dataku = pd.DataFrame({'x': x, 'y': y})

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x.reshape(-1, 1), y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

x_line = np.linspace(np.min(x), np.max(x), num=100).reshape(-1, 1)
y_line = regressor.predict(x_line)  # Predict y-axis values for the x-axis sequence

plt.scatter(dataku.x, dataku.y)
plt.plot(x_line, y_line, color='red')  # Plot the predicted values


plt.xlabel("Usia Mobil(tahun)")
plt.ylabel("Harga Mobil($100)")
plt.title("Grafik Usia Mobil vs Harga Mobil")
plt.show()
