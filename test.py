import pandas as pd
data = {
    'A': [1,2,3,4,5],
    'B': [10,20,30,40, 50]
}

df = pd.DataFrame(data)

reversed1 = df.iloc[:: -1] #.iloc[::-1] to select and return all rows in reverse order
print(reversed1)