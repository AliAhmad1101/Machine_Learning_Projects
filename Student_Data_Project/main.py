from src.load_data import load_dataset
from src.clean_data import inspect_data,clean_data
from src.transform import transform
from src.analyze import analysis
from src.report import create_report
import pandas as ps
df = load_dataset("Data/student_dataset_v2.csv")
print(df)

inspect_data(df)

cleaned_data = clean_data(df)

df = transform(cleaned_data)

analysis(df)

create_report(df)