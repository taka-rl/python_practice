import pandas_datareader as pdr

# Get the historical data for a stock
data = pdr.get_data_yahoo('AAPL', start='2020-01-01')

# Print the data
print(data)