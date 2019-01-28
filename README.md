# Speedtest-history
Speedtest-history allows a user to view a history of speedtest.net results.
### Feature support
- Optional blocking/allowing of specific speedtest servers
- Saves results of speedtest.net to a .csv
- View historical upload/download speeds using matplotlib and pandas
- Optionally view the plots on a local web view 
### Planned Features
- Create a web-based view for hosting on a Raspberry Pi or similar microcontroller
- Optional automatic contacting to ISP or system admin
- Better xaxis formatting
- Automatically choose suitable yaxis scale
- Choose a specific area code to limit speedtest servers to within a certain area 
- Create infrastructure for raspberry pi to be able to receive speedtest data from other devices
	- Categorize data by device type, location, ethernet or not etc. 
### Bugs to fix
- Fix xaxis dates using incorrect timezones
- Fix local web view dates overlapping
### Dependancies 
- Python 3
- Pandas
- Matplotlib
- Speedtest-cli 
- mpld3 
- jinja2 

