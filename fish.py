import numpy as np
import pandas as pd

bream_length  = pd.read_csv('C:\\fish\\bream_length.csv', names=['길이'])
bream_weight  = pd.read_csv('C:\\fish\\bream_weight.csv', names=['무게'])
smelt_length  = pd.read_csv('C:\\fish\\smelt_length.csv', names=['길이'])
smelt_weight  = pd.read_csv('C:\\fish\\smelt_weight.csv', names=['무게'])

bream_data = pd.concat((bream_length, bream_weight), axis=1)
print(type(bream_data))
print(bream_data)

smelt_data = pd.concat((smelt_length, smelt_weight), axis=1)
print(smelt_data)
print("="*50)

fish_data = pd.concat((bream_data, smelt_data), axis=0, ignore_index=True)
print(fish_data)
