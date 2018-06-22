# import datetime library
from datetime import datetime


class StopWatch:
    def __init__(self):
        self._start_time = datetime.now()
        
    def start(self):
	# record start time
        print ("Start time: " + self._start_time.strftime("%Y-%m-%d %H:%M:%S"))
        
    def stop(self):
	# record end time and elapsed time
        end_time = datetime.now()
        elapsed = (end_time - self._start_time).seconds

	# convert to hours, minutes and seconds
        hours = elapsed//3600
        minutes = (elapsed//60)%60
        seconds = elapsed%60
        
	# display end time
        print ("End time: " + end_time.strftime("%Y-%m-%d %H:%M:%S"))

	# display run time (elapsed time)
        print ("Run time: " + '{:02}'.format(hours) + ":" + '{:02}'.format(minutes) + ":" + '{:02}'.format(seconds))
    






