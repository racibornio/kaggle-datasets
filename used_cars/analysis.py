import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

pd.set_option('display.float_format', '{:,.2f}'.format)

csv_path = Path(__file__).parent / "used_car_dataset.csv"

initial_df = pd.read_csv(csv_path)

df = initial_df.copy()
print('Sample data:')
print(df.head())
print()

print('Data set metadata:')
print(df.info())
print()

unique_years_list = sorted(df['Year'].unique().tolist())
print(f'Unique years: {unique_years_list}')
print()


print('Sample price:', df['AskPrice'].sample())
print()
print(df['AskPrice'].dtype)
df['AskPrice'] = (df['AskPrice'].astype(str).str.replace('₹', '').str.replace(',', '').str.strip().astype(float))
print('Sample price after clean-up:', df['AskPrice'].sample())
print()


print()
# data frame from columns of interest
prices_yearly_df = pd.DataFrame({
    'min_price' : df.groupby(['Year'])['AskPrice'].min(),
    'max_price' : df.groupby(['Year'])['AskPrice'].max(),
    'avg_price' : df.groupby(['Year'])['AskPrice'].mean(),
    'median_price' : df.groupby(['Year'])['AskPrice'].median()
}).reset_index()
print()
print('New data set:')
print(prices_yearly_df)

prices_yearly_df.plot(kind='line', x='Year', y=['min_price', 'max_price', 'avg_price', 'median_price'])
plt.title="Prices per year"
plt.xlabel="Year"
plt.ylabel="Prices"
plt.legend="True"
plt.grid()
plt.show()