from os import listdir
from os.path import isfile, join
from time import sleep
from subprocess import call

#preprocessing script for a sample file
def preprocess(fname):
	w = open('sample.log','w')
	with open(fname) as f:
		content = f.readlines()
	set = -1
	for l in content:
		arr = l.split(" ")
		bytes = int(arr[4])
		timeelapsed = float(arr[5])
		bandwidth = bytes/timeelapsed
		w.write(str(timeelapsed)+" "+str(bandwidth)+'\n')
	w.close()

#throttle the bandwidth as per the traces present in fname
def throttle(fname):
	w = open(fname,'r')
	contents = w.readlines()
	cnt = 0;
	for l in contents:
		cnt = cnt+1
		arr = l.split(" ")
		bwidth = float(arr[1])*8
		t_ms = arr[0]
		t_s = float(t_ms)/(1000.0)
		s = "wondershaper wlan0 "+str(bwidth)+" "+str(bwidth)		# we are using wondershaper
		out = call(s,shell = True)									# this uses TC in background
		print(s+" throttling running "+ str(cnt))
		if(out != 0):
			print "error!"
		sleep(t_s)
		
if __name__ == '__main__':
	preprocess("/home/saiakhil/BTP/BandwidthTraces/hsdpa-tcp-logs/bus.ljansbakken-oslo/report.2010-09-28_1407CEST.log")
	throttle("/home/saiakhil/BTP/sample.log")