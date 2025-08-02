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
print()


##############################################
##########    eksploracja zbioru    ##########
##############################################

print('Pierwsze 5 wierszy:')
print(df.head())
print()

print('Ostatnie 5 wierszy:')
print(df.tail())
print()

print('Pierwsze 9 wierszy:')
print(df.head(9))
print()

print('Ostatnie 11 wierszy:')
print(df.tail(11))
print()

print('Losowe 5 wierszy:')
print(df.sample())
print()

print('Losowe 7 wierszy:')
print(df.sample(7))
print()

print('Informacje o kolumnach:')
print(df.info())
print()

print('Opis data frame:')
print(df.describe())
print()

print('Unikaty w kolumnach:')
print(df.nunique())