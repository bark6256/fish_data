import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy as db
from sqlalchemy import create_engine


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
# print(fish_target)

fish_data = np.vstack((bream_data, smelt_data))
# print(fish_data)
# print("="*50)

index_data = np.arange(bream_length.size + smelt_length.size)
np.random.shuffle(index_data)
# print(index_data)

train_input = fish_data[index_data[:35]]  # 훈련 데이터 (모델)
train_target = fish_target[index_data[:35]] # 타겟 데이터 (모델)

test_input = fish_data[index_data[35:]]  # 훈련 데이터 (검증)
test_target = fish_target[index_data[35:]] # 타겟 데이터 (검증)

# print(train_input[:5,])
# print(train_target[:5,])


# plt.scatter 는 데이터 프레임은 안된다. 넘파이는 된다.
plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(test_input[:,0], test_input[:,1])
plt.xlabel("length")
plt.ylabel("weight")
plt.show()

# 넘파이를 데이터프레임으로 변경
train_input = pd.DataFrame(train_input, columns=['length','weight'])
train_target = pd.DataFrame(train_target, columns=['targer'])
train_df = pd.concat((train_target, train_input), axis=1)
print(train_df)

test_input = pd.DataFrame(test_input)
test_target = pd.DataFrame(test_target)
test_df = pd.concat((test_target, test_input), axis=1)

# db 연결이 안되는듯 하다.
engine = db.create_engine("mariadb+mariadbconnector://fish:fish1234@127.0.0.1/fishdb")
print('test')

train_df.to_sql(name='train',con=engine, if_exists='replace',index=False)
