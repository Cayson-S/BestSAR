import numpy as np
import pandas as pd

sardata = pd.read_csv("sardata.csv")
sardata = sardata.drop(sardata.columns[[0]], axis=1)

# Check the data
#print(sardata.head())

for col in sardata.columns:
    print(sardata.loc[:, col].nunique())
    if sardata.loc[:, col].nunique() <= 1:
        sardata_dropped = sardata.drop(col, axis = 1)

print(sardata_dropped.head())
