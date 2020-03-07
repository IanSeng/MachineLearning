import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)
X = dataset.iloc[:,:-1].values