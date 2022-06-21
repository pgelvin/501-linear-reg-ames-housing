# Standard imports for linear regression
import pandas as pd
import numpy as np

# Visualization
import seaborn as sns
import matplotlib.pyplot as plt

# Specific statistical imports
# 'from' imports only what we need and not the entire library
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split

# Statistics imports
from scipy import stats
import statsmodels.api as sm

# magic and parameters
%matplotlib inline
plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['font.size'] = 14
plt.style.use("fivethirtyeight")

# import the dataset and review LOCALLY
df = pd.read_csv(r'C:\Users\pgelvin\Desktop\Datasets\ames_housing.csv')
df


