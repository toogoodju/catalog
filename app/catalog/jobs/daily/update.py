from django_extensions.management.jobs import HourlyJob
import re
import os
import requests

class Job(HourlyJob):

	def execute(self):
		directory = 'C:/git/prod-load-balancer-config/pools'
		for filename in os.listdir(directory):
			print(os.path.join(directory, filename))
			with open(os.path.join(directory, filename), 'r') as myfile:
				data = myfile.read();
				nodesline = re.findall('nodes\s+(.*?)\n', data, re.S)
				if nodesline:
					nodes = re.findall('[\w\-.]+:\w+', nodesline[0], re.S)
					print(nodes)

	def parse_pool(rootpath):
		directory = rootpath + "/pools"
		for filename in os.listdir(directory):
			with open(os.path.join(directory, filename), 'r') as myfile:
				data = myfile.read();
			nodesline = re.findall('nodes\s+(.*?)\n', data, re.S)
			if nodesline:
				nodes = re.findall('[\w\-.]+:\w+', nodesline[0], re.S)
				payload = {'name': filename, 'nodes': nodes}
				r = requests.put('http://localhost:8000/catalog/api/pools/'+ filename + '/', data=payload)

	def parse_rules(roothpath, environment):
		directory = rootpath + "/rules"
		for filename in os.listdir(directory):
			with open(os.path.join(directory, filename), 'r') as myfile:
				data = myfile.read()

			hosts = re.findall('hostheader\s+==\s+\"(.*?)\"', data, re.S)
			for host in hosts:
				payload = {'name': host, 'environment:' environment}
				r = requests.put('http://localhost:8000/catalog/api/hosts/' + host + '/', data=payload)

				blocks = re.findall('hostheader\s+==\s+\"' + host + '\"(.*?)(?:#------|\Z)', data, re.S)
				for block in blocks:
					contexts = re.findall('case\s+\"(.*?)\"', block, re.S)

					for context in contexts:
						contextblocks = re.findall('case\s+\"' + context + '\"(.*?)(?:case|default)', block, re.S)

						for contextblock in contextblocks:
							pools = re.findall('use\(\s*\"(.*?)\"\s*\)', contextblock, re.S)

							for pool in pools:
								payload = {'path': context, 'host': host}
								r = requests.get('http://localhost:8000/catalog/api/contexts/', params=payload).json()
								
								if 'id' in r:
									payload = {'id': r['id'], 'path': context, 'host': host, 'pool': pool}
									r = requests.put('http://localhost:8000/catalog/api/contexts/' + r['id'] + '/', data=payload)
								else
									payload = {'path': context, 'host': host, 'pool': pool}
									r = requests.post('http://localhost:8000/catalog/api/contexts/', data=payload)

								



def execute():
	directory = r'C:/git/prod-load-balancer-config/pools'
	for filename in os.listdir(directory):
		print(os.path.join(directory, filename))
		with open(os.path.join(directory, filename), 'r') as myfile:
			data = myfile.read()
		nodesline = re.findall('nodes\s+(.*?)\n', data, re.S)
		if nodesline:
			nodes = re.findall('[\w\-.]+:\w+', nodesline[0], re.S)
			#print(nodes)
			payload = {'name': filename, 'nodes': nodes}
			r = requests.put('http://localhost:8000/catalog/api/pools/'+filename+'/', data=payload)
			print(r.status_code)

if __name__ == '__main__':
    execute()
