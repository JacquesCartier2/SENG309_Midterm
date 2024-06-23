import pandas as pd


def csv_to_list(file_path):

    df = pd.read_csv(file_path)
    data_list = df.values.tolist()
    data_list.insert(0, df.columns.tolist())
    return data_list

file_path = "Maths.csv"
data_list = csv_to_list(file_path)

for row in data_list:
    print(row)

