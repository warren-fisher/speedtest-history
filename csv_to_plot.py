import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

filename = './speedtest_cli/data.csv'
df = pd.read_csv(filename, sep=',')

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10,5))

ax1.plot(df['timestamp'],df['download'],'o-')
ax1.set_title("Time vs. Download speed / Mbps")

ax2.plot(df['timestamp'],df['upload'],'o-')
ax2.set_title("Time vs Upload speed / Mbps") 

fig.autofmt_xdate(rotation=90)

plt.show()



