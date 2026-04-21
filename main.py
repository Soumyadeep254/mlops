import pandas as pd
import os 

data={'Name': ["John", "Alice","Bob"], 'Age': [25, 30, 35], 'City': ["New York", "Los Angeles", "Chicago"]}
df = pd.DataFrame(data)

new_row = {'Name': "Eve", 'Age': 28, 'City': "San Francisco"}
df.loc[len(df.index)] = new_row

new_row_2 = {'Name': "Charlie", 'Age': 32, 'City': "Seattle"}
df.loc[len(df.index)] = new_row_2

data_dir = "data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

csv_path = os.path.join(data_dir, "data.csv")
df.to_csv(csv_path, index=False)
print(f"DataFrame saved to {csv_path}")

