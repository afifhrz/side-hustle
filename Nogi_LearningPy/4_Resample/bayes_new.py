from scipy import stats
import arviz as az
import numpy as np
import matplotlib.pyplot as plt
import pymc3 as pm
import seaborn as sns
import pandas as pd
from theano import shared
from sklearn import preprocessing
print('Running on PyMC3 v{}'.format(pm.__version__))
# data = pd.read_csv('renfe.csv')
# data.drop('Unnamed: 0', axis = 1, inplace=True)
# data = data.sample(frac=0.01, random_state=99)
# data.head(3)