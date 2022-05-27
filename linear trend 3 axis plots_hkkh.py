import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

glob = pd.read_csv("hkkh.csv", index_col='Time', parse_dates=[0], encoding = "ISO-8859-1")
data = glob.sort_values(by="Time")
train_mag = glob["Strong Earthquake 6.0 - 6.9M"]
train_temp = glob["Global Temperature Anomaly"]

fig, ax1 = plt.subplots()

# Magnitude
order = 1
coef_fst = np.polyfit(np.arange(len(train_mag)),
                      train_mag.values.ravel(), order)

poly_mdl = np.poly1d(coef_fst)
trend_hhkk_mag = pd.Series(data=poly_mdl(np.arange(len(train_mag))),
                           index=train_mag.index)

print("The slope of the Magnitude curve is {:.4f}".format(coef_fst[0]))

# Temperature
order = 1
coef_sec = np.polyfit(np.arange(len(train_temp)),
                      train_temp.values.ravel(), order)

poly_mdl = np.poly1d(coef_sec)
trend_hhkk_temp = pd.Series(data=poly_mdl(np.arange(len(train_temp))),
                            index=train_temp.index)

print("The slope of the Temperature curve is {:.4f}".format(coef_sec[0]))

plt.ylim(0,10)
plt.plot(trend_hhkk_mag, color="red")
plt.plot(train_mag, color='blue')

plt.xlabel("Time", fontweight='bold', color='black', size=16)
plt.title("Strong Earthquake 6.0 - 6.9M", color="black", fontweight='bold', size=16)

ax = ax1.twinx()
ax.plot(trend_hhkk_temp, color='black')
ax.plot(train_temp, color='green')

ax1.set_ylabel("Temporal Variation of the Total number of \n earthquakes in HKKH region", fontweight='bold', color='blue',
               size=16)

plt.ylabel("Global Temperature Anomaly (°C)", fontweight='bold', color='green', size=16)

plt.grid()
plt.show()
