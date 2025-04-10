import pandas as pd

askingprices = pd.Series([1800000, 2200000, 2500000, 1700000, 3000000])
fairprices   = pd.Series([2000000, 2100000, 2600000, 1800000, 2900000])

gooddeals = askingprices < fairprices

gooddealindices = gooddeals[gooddeals].index.tolist()
print("Indices of good deals = ", gooddealindices)