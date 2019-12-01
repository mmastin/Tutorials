import numpy as np

#np broadcasting
X, Y = np.meshgrid(np.arange(2), np.arange(2))
# print(X)
# print(Y)
# print(X+Y)

x = np.array([0,1])
y = np.array([0,1])
# z = x + y[:, None]  # add broadcast dimension
z = x + y[:, np.newaxis]
# print(z)

x = np.array([0,1])
y = np.array([0,1,2])
X, Y = np.meshgrid(x,y)
# print(X)
# print(Y)
# print(X+Y)
# print(x+y[:, None])

#matplotlib

import matplotlib.pyplot as plt
# plt.plot(range(10))
# plt.show()

import pandas as pd

x = pd.Series(range(5), [1,2,11,9,10])
grp = x.groupby(lambda i: i%2)  # odd or even
print(grp.get_group(1))