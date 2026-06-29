import pandas as ps
import time
def load_dataset(filepath):
    df = ps.read_csv(filepath)
    print("\nTop 5 rows:\n")
    print(df.head())
    time.sleep(1)
    print("\nLast 5 rows:\n")
    print(df.tail())
    time.sleep(1)
    print("\nShape of the dataset:\n")
    print(df.shape)
    time.sleep(1)
    print("\nColumn names in the dataset:\n")
    print(df.columns)
    time.sleep(1)
    print("\nData types of each column:\n")
    print(df.dtypes)
    time.sleep(1)
    return df