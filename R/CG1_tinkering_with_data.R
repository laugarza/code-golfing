### LIBRARIES ###
library(ggplot2)

### USER DEFINED FUNCTIONS ###
read_streamflow_data <- function(file = './data/sacramento-bendbridge-paleo.csv'){
	df <- read.csv(file, header = TRUE)
	return(df)
}

### MAIN ###
df <- read_streamflow_data()


# TODO

# 1. add a column to the dataframe and convert the annual flow from acre-foot to cubic meters 

# 2. plot the time series of the flow in cubic meters
# p <- ggplot(...)

# 3. calculate the mean, median and standard deviation of the annual flow per calendar century (e.g. 901 - 1000, 1001 - 1100, ... 2001 - 2019)

# (opt. add those three timeseries to the plot created in 2)

# 4. re-order the data-frame so that the data are ordered by increasing mean flow