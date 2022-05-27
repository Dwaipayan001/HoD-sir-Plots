import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np


df = pd.read_csv("global.csv", index_col='Time', parse_dates=[0])
data = df.sort_values(by="Time")
train = data["Maximum Depth"]


d = train[626:1214] # 1973-2021

order = 1
coef = np.polyfit(np.arange(len(d)),
                  d.values.ravel(),
                  order)


poly_mdl = np.poly1d(coef)
trend = pd.Series(data = poly_mdl(np.arange(len(d))),
                  index = d.index)

slope = coef[0]


print("{:.4f}".format(slope))
print(slope)


plt.plot(d)
plt.plot(trend)
plt.grid()
plt.legend(['Seasonality','Trend'],loc='upper left')
plt.xlabel("Time",size=12)
plt.title("Maximum Depth",size=15)
plt.ylabel("Maximum Depth",size=12)
plt.show()



