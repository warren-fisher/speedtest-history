import pandas as pd
import matplotlib.pyplot as plt, mpld3
import matplotlib.dates as mdates

from speedtest_csv import file_path, port_num, automatic_browser_open, use_web_view

df = pd.read_csv(file_path, sep=',')
df['timestamp'] = pd.to_datetime(df['timestamp'])

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10,5))

ax1.plot(df['timestamp'],df['download'],'o-')
ax1.set_title("Time vs. Download speed / Mbps")
ax1.set(xlabel="Date", ylabel="Download speed / Mbps")
ax1.set_ylim([0,1000])
ax1.xaxis_date()
ax1.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')

ax2.plot(df['timestamp'],df['upload'],'o-')
ax2.set_title("Time vs Upload speed / Mbps")
ax2.set(xlabel="Date", ylabel="Upload speed / Mbps")
ax2.set_ylim([0,50])
ax2.xaxis_date()
ax2.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')

fig.autofmt_xdate(rotation=90)

if use_web_view is True:
	mpld3.show(fig, port = port_num, open_browser = automatic_browser_open)
else: 
	plt.show()
	







