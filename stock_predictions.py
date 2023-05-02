import pandas as pd
import numpy as np

market = pd.read_csv("AAPL Historical Data.csv", decimal=",")
market = pd.DataFrame(market)


# Market first 10 rows
print(market.head(10))

# Market data frame shape
print(market.shape)

# Market data frame types
print(market.dtypes)

## Changing col name "Vol." to be more usefull
market = market.rename(columns = {"Vol.":"Vol"})

market[['Vol', "Unit"]] = market.Vol.str.split("M", expand = True)
market = market.drop(columns = ["Unit"])

print(market.head(10))

# Market data frame missing values
print(market.isnull().sum().sort_values(ascending = False))

# Convert data


## Drop unecessary cols
# market.drop


