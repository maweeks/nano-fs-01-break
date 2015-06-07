import time
import webbrowser
count = 0
start_time = time.ctime()
print ("This program started at "+start_time)
while (count < 8):
	time.sleep(3600)
	webbrowser.open("http://matt.weeks.codes")
	count += 1
	print ("Take a break, the time is now,  "+start_time)