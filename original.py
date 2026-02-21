import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt


df=pd.read_csv('nifty_data.csv')

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%b %d, %Y')

# Remove commas from 'Close' and convert to numeric
df['Close'] = df['Close'].replace({',': ''}, regex=True).astype(float)

plt.figure(figsize=(14,10))

plt.plot(df['Date'], df['Close'])
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Nifty Close Price Over Time')
plt.show()