import speedtest
import pandas as pd
import os
import datetime as dt

dirname = './speedtest_data'
filename = 'data.csv'
file_path = dirname + '/' + filename
port_num = 8888 
automatic_browser_open = False
use_web_view = True
bit_to_megabit_ratio = 1048576**-1
# Insert a list of specific server IDs from http://www.speedtest.net/speedtest-servers-static.php to allow/block. 
allowed_servers = []
blocked_servers = []

def remove_key(d, key):
	r = dict(d)
	del r[key]
	return r

def make_dir(directory): 
	try: 
		os.makedirs(directory)
	except FileExistsError: 
		return 

def main():		
	s = speedtest.Speedtest()
	s.get_servers(allowed_servers, blocked_servers)
	s.get_best_server()
	s.download()
	s.upload()

	results_dict = s.results.dict()

	keys_to_remove = ['server','bytes_sent','bytes_received','share','client','ping']
	for key in keys_to_remove: 
		results_dict = remove_key(results_dict, key)

	results_dict['download'] *= bit_to_megabit_ratio
	results_dict['upload'] *= bit_to_megabit_ratio

	df_new = pd.DataFrame([results_dict])
	try:
		df_old = pd.read_csv(file_path, sep=',') 
		df_final = pd.concat([df_old, df_new], ignore_index = True) # ignore_index prevents an index output of 0, 1, 2, 0 which happens when concatenating two dataframes with index 0, 1, 2 and 0
	except FileNotFoundError: # if a file is not found we want the dataframe to only consist of our latest data
		make_dir(dirname) 
		df_final = df_new

	df_final.to_csv(file_path, encoding='utf-8', index=False) # Our index does not matter at this point. It is easier to set the index as timestamp when displaying data

	print(df_final)
	
if __name__=='__main__':
	main()

