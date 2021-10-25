import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

bream_length  = pd.read_csv('C:\\fish\\bream_length.csv', names=['길이'])
bream_weight  = pd.read_csv('C:\\fish\\bream_weight.csv', names=['무게'])
smelt_length  = pd.read_csv('C:\\fish\\smelt_length.csv', names=['길이'])
smelt_weight  = pd.read_csv('C:\\fish\\smelt_weight.csv', names=['무게'])

bream_length = bream_length.to_numpy()
bream_weight = bream_weight.to_numpy()

smelt_length = smelt_length.to_numpy()
smelt_weight = smelt_weight.to_numpy()

bream_data = np.hstack((bream_length, bream_weight))
# print(type(bream_data))
# print(bream_data)

smelt_data = np.hstack((smelt_length, smelt_weight))
# print(smelt_data)
# print("="*50)

fish_target = np.concatenate((np.ones(bream_length.size), np.zeros(smelt_length.size)))
print(fish_target)

fish_data = np.vstack((bream_data, smelt_data))
# print(fish_data)
# print("="*50)


# plt.scatter 는 데이터 프레임은 안된다. 넘파이는 된다.
plt.scatter(bream_data[:,0], bream_data[:,1])
plt.scatter(smelt_data[:,0], smelt_data[:,1])
plt.xlabel("length")
plt.ylabel("weight")
plt.show()