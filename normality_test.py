#relative change= change in closing price/previous closing price
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
df=pd.read_csv('nifty_data.csv')

# Remove commas from 'Close' and convert to numeric, handling errors
df['Close'] = df['Close'].astype(str).str.replace(',', '').str.strip()
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

# Forward-fill missing values in 'Close'
df['Close'] = df['Close'].ffill()

df['relative_close_change'] = df['Close'].pct_change()*100

st,p=stats.shapiro(df['relative_close_change'].dropna())
print('Shapiro-Wilk Test Statistic:', st)
print('Shapiro-Wilk Test p-value:', p)
#output
'''
Shapiro-Wilk Test Statistic: 0.8849108279585431
Shapiro-Wilk Test p-value: 9.496275851454806e-50
'''

from sklearn.preprocessing import StandardScaler

# Standardize data (important for KS test)
scaler=StandardScaler()
data_scaled=scaler.fit_transform(df['relative_close_change'].dropna().values.reshape(-1,1)).flatten()


stat, p = stats.kstest(data_scaled, 'norm')

print("KS Test")
print("Statistic:", stat)
print("p-value:", p)
#output
'''
KS Test
Statistic: 0.08792475801328803
p-value: 7.828607546219425e-31
'''

#p value very small , we reject null hypthesis that data is normally distributed

print("Skewness:", stats.skew(df['relative_close_change'].dropna()))
print("Kurtosis:", stats.kurtosis(df['relative_close_change'].dropna()))
#output
'''
Skewness: 0.6160282875216987
Kurtosis: 15.377373210158499
'''
 
#Hence , it is  right skewed and has very high kurtosis (leptokurtic)
import numpy as np
data=df['relative_close_change'].dropna()
mu=np.mean(data)
sigma=np.std(data)
x=np.linspace(min(data), max(data), 100)
plt.hist(data, bins=50, density=True, alpha=0.6, color='g')
plt.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', lw=2)
plt.title("Normal distribution fit")
plt.show()