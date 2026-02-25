#comparison in t distribution vs normal distribution
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
df=pd.read_csv('nifty_data.csv')

#remove commas and make close price numeric
df['Close'] = df['Close'].astype(str).str.replace(',', '').str.strip()
df['Close']=pd.to_numeric(df['Close'], errors='coerce')
#forward fill missing values
df['Close']=df['Close'].ffill()

df['relative_close_change']=df['Close'].pct_change()*100

data=df['relative_close_change'].dropna()

import numpy as np
mu=np.mean(data)
sigma=np.std(data)

df_t, loc_t, scale_t = stats.t.fit(data)

x=np.linspace(min(data), max(data), 100)
plt.hist(data, bins=50, density=True, alpha=0.5, color='g',label='Data')
plt.plot(x, stats.norm.pdf(x, mu, sigma), 'b-', lw=2, label='Normal Fit')
plt.plot(x, stats.t.pdf(x, df_t, loc_t, scale_t), 'r-', lw=2, label='t-Distribution Fit')
plt.title("Comparison of Normal  and t-Distribution Fits")
plt.legend()
plt.show()

