import numpy as np
import pandas as pd

bream_length  = pd.read_csv('C:\\fish\\bream_length.csv')
bream_weight  = pd.read_csv('C:\\fish\\bream_weight.csv')
smelt_length  = pd.read_csv('C:\\fish\\smelt_length.csv')
smelt_weight  = pd.read_csv('C:\\fish\\smelt_weight.csv')

print(type(bream_length))
print(bream_length)
print("="*50)
print(type(bream_weight))
print(bream_weight)
print("="*50)
print(type(smelt_length))
print(smelt_length)
print("="*50)
print(type(smelt_weight))
print(smelt_weight)
print("="*50)