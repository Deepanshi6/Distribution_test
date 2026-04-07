import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt


df=pd.read_csv('nifty_data.csv')

df['Close'] = (
    df['Close']
    .astype(str)
    .str.replace(',', '')
    .str.strip())

df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
df['Close'] = df['Close'].ffill()

df['relative_close_change'] = df['Close'].pct_change()*100
#we got percentage relative change in close price

#y-axis=frequency of relative change in close price

plt.figure(figsize=(14,10))
df['relative_close_change'].plot(kind='kde', title='Relative Change in Close Price Distribution')
plt.xlabel('Relative Change in Close Price (%)')
plt.ylabel('Density')
plt.show()

