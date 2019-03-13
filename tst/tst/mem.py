# some imports
from subprocess import check_output
import psutil


# name of the process to find details
name = 'hello'


# fuction to return memory and other details related to any process id
def memoryUsage(name):
	details = {}
	pid = int(check_output(["pidof",name]))
	process = psutil.Process(pid)
	mem = process.memory_info()[0] / float(2 ** 20)

	details['Process Name'] = process.name()
	details['Process pid'] = pid	
	details['Directory'] = process.cwd()
	details['Memory Load'] = str(process.memory_percent())+' %'
	details['CPU Load'] = str(process.cpu_percent())+' %'
	memoryInfo = process.memory_full_info()

	return details,memoryInfo



d,m = memoryUsage(name)

for i in d:
	print i, ' -> ',d[i]


# some formatting
memoryDetails = {

	'Resident Set Size':m[0],
	'Virtual Memory Size':m[1],
	'Shared memory with Other Process':m[2],
	'Text Code Memory':m[3],
	'lib':m[4],
	'Data or Physical Memory other than executable code':m[5],
	'Unique set size':m[7],
	'Proportional set size':m[8]
	}

print('\n\n----------Memory Details-----\n')
for key,value in memoryDetails.items():
	print key,' ->', value, 'Bytes' 

