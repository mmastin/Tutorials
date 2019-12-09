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
# print(grp.get_group(1))

df = pd.DataFrame({'col1': [1,3,11,2], 'col2': [9, 23, 0, 2]})
# print(df)

# print(df.sum())

df = pd.DataFrame({'col1': [1,1,0,0], 'col2': [1,2,3,4]})

grp = df.groupby('col1')
# print(grp.get_group(0))

