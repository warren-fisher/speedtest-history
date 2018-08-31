import pandas as pd
import matplotlib.pyplot as plt, mpld3
import matplotlib.dates as mdates

from speedtest_csv import filename, port_num, automatic_browser_open, use_web_view

df = pd.read_csv(filename, sep=',')

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10,5))

ax1.plot(df['timestamp'],df['download'],'o-')
ax1.set_title("Time vs. Download speed / Mbps")

ax2.plot(df['timestamp'],df['upload'],'o-')
ax2.set_title("Time vs Upload speed / Mbps") 

fig.autofmt_xdate(rotation=90)

if use_web_view is True:  
	mpld3.show(fig, port = port_num, open_browser = automatic_browser_open)
else: 
	plt.show()






