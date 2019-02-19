### MODULES ###
import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import seaborn as sns

### USER DEFINED FUNCTIONS ###
def read_streamflow_data(file = './data/sacramento-bendbridge-paleo.csv'):
	import pandas as pd
	df = pd.read_csv(file, index_col=0, parse_dates=True)
	return df

### MAIN ###
df = read_streamflow_data()


# TODO

# 1. add a column to the dataframe and convert the annual flow from acre-foot to cubic meters 

# 2. plot the time series of the flow in cubic meters
# plt.plot()

# 3. calculate the mean, median and standard deviation of the annual flow per calendar century (e.g. 901 - 1000, 1001 - 1100, ... 2001 - 2019)

# (opt. add those three timeseries to the plot created in 2)

# 4. re-order the data-frame so that the data are ordered by increasing mean flow