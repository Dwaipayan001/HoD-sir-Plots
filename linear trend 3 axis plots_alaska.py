import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

alaska = pd.read_csv("alaska.csv", index_col='Time', parse_dates=[0])

data = alaska.sort_values(by="Time")
train_mag = alaska["Major Magnitude 7M+"]
train_temp = alaska["Global Temperature Anomaly"]

fig, ax1 = plt.subplots()

# First Plot
order = 1
coef_fst = np.polyfit(np.arange(len(train_mag)),
                      train_mag.values.ravel(), order)

poly_mdl = np.poly1d(coef_fst)
trend_alaska_mag = pd.Series(data=poly_mdl(np.arange(len(train_mag))),
                             index=train_mag.index)

print("The slope of the Magnitude curve is {:.4f}".format(coef_fst[0]))

# Second Plot
order = 1
coef_sec = np.polyfit(np.arange(len(train_temp)),
                      train_temp.values.ravel(), order)

poly_mdl = np.poly1d(coef_sec)
trend_alaska_temp = pd.Series(data=poly_mdl(np.arange(len(train_temp))),
                              index=train_temp.index)

print("The slope of the Temperature curve is {:.4f}".format(coef_sec[0]))

# plt.locator_params('y',nbins=30)

# plt.ylim(ymin=6,ymax=8)

# in case plot looking messy , uncomment below line


choice = int(input("Enter the Choice : 1 - Default , 2 - For User Scale"))

if choice == 2:
    scale = int(input("Enter the Scale Range"))
    plt.ylim(0, scale)
    plt.plot(trend_alaska_mag, color="red")
    plt.plot(train_mag, color='blue')
else:
    plt.plot(trend_alaska_mag, color="red")
    plt.plot(train_mag, color='blue')

plt.xlabel("Time", fontweight='bold', color='black', size=16)
plt.title("Major Magnitude 7M+", color="black", fontweight='bold', size=16)

ax = ax1.twinx()

ax.plot(trend_alaska_temp, color='black')
ax.plot(train_temp, color='green')

ax1.set_ylabel("Temporal Variation of the Total number of \n earthquakes in Alaska Region", fontweight='bold',
               color='blue', size=16)

plt.ylabel("Global Temperature Anomaly (°C)", fontweight='bold', color='green', size=16)

plt.grid()
plt.show()
