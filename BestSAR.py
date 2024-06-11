import numpy as np
import pandas as pd

sardata = pd.read_csv("sardata.csv")
sardata = sardata.drop(sardata.columns[[0]], axis=1)

# Check the data
#print(sardata.head())

for col in sardata.columns:
    if sardata.loc[:, col].nunique() <= 1:
        sardata_dropped = sardata.drop(col, axis = 1)

# Convert categorical data to dummy variables
sardata_dropped = pd.get_dummies(sardata_dropped, columns = ["R1", "R2", "R3", "R4", "R5", "R6"])

print(sardata_dropped.columns)