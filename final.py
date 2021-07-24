from http.server import HTTPServer, BaseHTTPRequestHandler
import requests, json
import pandas as pd
import time
import random
import hashlib
import os
script_dir = os.path.dirname(__file__) # <-- absolute dir the script 
rel_path = "data.json"
abs_file_path = os.path.join(script_dir, rel_path)
# open json file and give it to data variable as a dictionary
with open(abs_file_path) as data_file:
	data_information = json.load(data_file)

# Defining a HTTP request Handler class
class ServiceHandler(BaseHTTPRequestHandler):
	# sets basic headers for the server
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type','text/json')
		#reads the length of the Headers
		length = int(self.headers['Content-Length'])
		#reads the contents of the request
		content = self.rfile.read(length)
		temp = str(content).strip('b\'')
		self.end_headers()
		return temp
		

	# GET Method Defination
	def do_GET(self):
		# defining all the headers
		self.send_response(200)
		self.send_header('Content-type','text/json')
		self.end_headers()
		url = "https://restcountries-v1.p.rapidapi.com/all"
		url_countries_by_region = "https://restcountries.eu/rest/v2/region/{region}"

		headers = {
			'x-rapidapi-key': "921cfc17abmsh42834139575656fp12725cjsn8ce3ad10333d",
			'x-rapidapi-host': "restcountries-v1.p.rapidapi.com"
			}



		regions_data = []
		hash_languages =[]
		countries = []
		times=[]


		data  = json.loads(requests.request("GET", url, headers=headers).text)

		for information in data:
			if information["region"]  and not information["region"]  in regions_data:
				regions_data.append(information["region"])
		# only the different existing regions
		

		for region in regions_data:
			start_time = time.time()
			response_by_region = json.loads(
				requests.request("GET", url_countries_by_region.format(region=region), headers=headers).text
			)
			# we consult the data requested by region
			country_option = random.randint(0,len(response_by_region)-1)
			countries.append(response_by_region[country_option]['name'])
			hash_languages.append(hashlib.sha1(response_by_region[country_option]['languages'][0]['name'].encode()).hexdigest())
			end_time = time.time()
			times.append(round((end_time-start_time)*1000,2))

		df = pd.DataFrame({
			"Region": regions_data,
			"Country": countries,
			"Language SHA1": hash_languages,
			"Time [ms]": times
		})


		statistics = {}
		statistics['total'] = df['Time [ms]'].sum()
		statistics['mean'] = df['Time [ms]'].mean()
		statistics['min'] = df['Time [ms]'].min()
		statistics['max'] = df['Time [ms]'].max()
		#  we build a dataframe and a data.json file with the results of the algorithm
		df.to_json(path_or_buf='data.json')
		# here we can return the answer in html format but I decided to leave the answer in json format
		# self.wfile.write(bytes(table_html[0], "utf-8"))
		self.wfile.write(json.dumps(data_information).encode())



			
# Server Initialization
server = HTTPServer(('127.0.0.1',8000), ServiceHandler)
server.serve_forever()
