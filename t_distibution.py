#looking at t distribution
import pandas as pd
import scipy.stats as stats

df=pd.read_csv('nifty_data.csv')

# Remove commas from 'Close' and convert to numeric, handling errors
df['Close'] = df['Close'].astype(str).str.replace(',', '').str.strip()
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

# Forward-fill missing values in 'Close'
df['Close'] = df['Close'].ffill()

df['relative_close_change'] = df['Close'].pct_change()*100

#t distribution
data=df['relative_close_change'].dropna()
df,loc,scale=stats.t.fit(data)
print("Degrees of Freedom:", df)
print("Location of head:", loc) 
print("Scale or spread:", scale)

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(min(data), max(data), 100)
plt.hist(data, bins=50, density=True, alpha=0.6)
plt.plot(x, stats.t.pdf(x, df, loc, scale), 'r-', lw=2)
plt.title("t-distribution fit")
plt.show()