import pandas as pd
from pathlib import Path


# Set the current working directory
cwd = Path.cwd()
print(f'Current path is {cwd}')

dataset = cwd / 'atc_pre_departure_delays' / 'atc_pre_departure_delays_2025.csv'
print(f'Dataset path is {dataset}')


# Load the dataset
df = pd.read_csv(dataset)
print('Dataframe:')
print(df)