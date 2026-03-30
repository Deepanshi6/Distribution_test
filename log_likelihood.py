import numpy as np
from scipy import stats
import pandas as pd

df = pd.read_csv('nifty_data.csv')

df['Close'] = df['Close'].astype(str).str.replace(',', '').str.strip()
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
df['Close'] = df['Close'].ffill()

data = df['Close'].pct_change().dropna() * 100

# Normal fit
mu = np.mean(data)
sigma = np.std(data)

ll_n = np.sum(stats.norm.logpdf(data, mu, sigma))

#t fit (CORRECT)
df_t, loc_t, scale_t = stats.t.fit(data)

ll_t = np.sum(stats.t.logpdf(data, df_t, loc_t, scale_t))

print("Log-Likelihood Normal:", ll_n)
print("Log-Likelihood t:", ll_t)

# AIC 
k_norm = 2
k_t = 3

aic_norm = 2*k_norm - 2*ll_n
aic_t = 2*k_t - 2*ll_t

print("AIC Normal:", aic_norm)
print("AIC t:", aic_t)
print("Delta AIC:", aic_norm - aic_t)
if aic_t < aic_norm:
    print("t-distribution is a better fit to the data.")
else:
    print("Normal distribution is a better fit.")

delta_aic = aic_norm - aic_t

print("Delta AIC (Normal - t):", delta_aic)

if delta_aic > 10:
    print("Strong evidence: t-distribution fits significantly better than normal.")
elif delta_aic > 4:
    print("Moderate evidence: t-distribution fits better than normal.")
elif delta_aic > 2:
    print("Weak evidence: slight improvement with t-distribution.")
elif delta_aic > -2:
    print("No meaningful difference between models.")
else:
    print("Normal distribution fits better (unexpected for financial returns).")