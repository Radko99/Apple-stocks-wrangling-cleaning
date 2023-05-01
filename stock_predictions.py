# Loading libraries
import pandas as pd
import numpy as np

market = pd.read_csv("Historyczne ceny AAPL.csv")
market = pd.DataFrame(market)

# Market first 10 rows
print(market.head(10))

# Market data frame shape
print(market.shape)

# Market data frame types
print(market.dtypes)

# Market data frame missing values
print(market.isnull().sum())
market.info()
