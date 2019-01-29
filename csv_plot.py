import pandas as pd
import matplotlib.pyplot as plt, mpld3
import matplotlib.dates as mdates

from speedtest_csv import file_path, port_num, automatic_browser_open, use_web_view

df = pd.read_csv(file_path, sep=',')
df['timestamp'] = pd.to_datetime(df['timestamp'])

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10,5))

def create_fig(ax, x, x_label, y, y_label):
	ax.plot(x,y,'o-')
	ax.set_title('{} vs {}'.format(y_label.capitalize(),x_label))
	ax.set(xlabel=x_label,ylabel=y_label)
	ax.xaxis_date()
	ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')

create_fig(ax1, df['timestamp'],'Date',df['download'],'Download speed / Mbps')
create_fig(ax2, df['timestamp'],'Date',df['upload'],'Upload speed / Mbps')

fig.autofmt_xdate(rotation=90)

if use_web_view is True:
	mpld3.show(fig, port = port_num, open_browser = automatic_browser_open)
else: 
	plt.show()