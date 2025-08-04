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
print()

print('Wyświetl pierwszą kolumnę:')
print(df['YEAR'])
print()

print('Wyświetl drugą kolumnę:')
print(df['MONTH_NUM'])
print()

print('Pokaż unikaty pierwszej kolumny - lata:')
print(df['YEAR'].unique())
print()

print('Pokaż unikaty drugiej kolumny - miesiące:')
print(df['MONTH_NUM'].unique())
print()

print('Pokaż wartości unikatów i ilość ich wystąpień w kolumnie MONTH_NUM:')
print(df['MONTH_NUM'].value_counts())
print()

print('Czy są duplikaty dla kolumny STATE_NAME?')
print(df['STATE_NAME'].duplicated())
print()


# df['age'].unique() -> pokaż duplikaty wybranej kolumny
# df['age'].value_counts() -> pokaż wartości unikatów i ilość ich wystąpień
# df["height [m]"] = df["height [cm]"] / 100 -> nowa kolumna z kalkulacji innej
# df["bmi category"] = df["bmi"].apply(bmi_category) -> nowa kolumna z wynikiem działania funkcji
# df.drop(columns="height [m]", inplace=True) -> usunięcie kolumny
# df = df.drop('Klasyfikacja', axis=1) -> trwałe usunięcie kolumny
# df["age"] += 1 -> nadpisanie wartości w kolumnie
# df = df.rename(columns={"name" : "Imię"}) -> zmiana nazwy kolumny
# df.columns = ['Imię', 'Wiek', 'Waga', 'Wzrost', 'Kraj', 'BMI', 'Klasyfikacja'] -> zmiana nazw kolumn w kolejności występowania
# df.sort_values(by="Wzrost") -> sortowanie po kolumnie - rosnąco
# df.sort_values(by="Wzrost", ascending=False) -> sortowanie po kolumnie - malejąco