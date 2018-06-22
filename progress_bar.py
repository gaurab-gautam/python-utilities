# Marquee Style Progress Bar
# USAGE: call start method to start progress bar; 
#	 call stop method to stop progress bar

# imports
import sys
import time
import threading

###############################  Constant Values ######################################
MAX_STEPS = 20
PROGRESS_INDICATOR = '#'
INITIAL_BAR = "[--------------------]"
INTERVAL = 1  # 1 second interval
INDICATOR_START_POS = 1
#######################################################################################


class ProgressThread(threading.Thread):  

    def __init__(self, interval, print_progress_func, indicator_pos):
        threading.Thread.__init__(self)
        
        # interval for scheduling print
        self._interval = interval
        
        # indicator direction
        self._forward = True
        
        # indicator position
        self._indicator_pos = INDICATOR_START_POS
        
        # pointer to progress bar print function
        self._print_progress_func = print_progress_func
        
        # stop even stops thread when called
        self.stop_event = threading.Event()        

    def stop(self, timeout=None):
        if self.isAlive() is True:
            # set event to terminate thread
            self.stop_event.set()
                
            # call to terminate the thread
            self.join()
            
    def run(self):
        while not self.stop_event.is_set():
            # increment position index if going forward
            # decrement position index if going backward
            if self._forward is True:
                self._indicator_pos += 1
            else:
                self._indicator_pos -= 1
                 
            # reset when indicator reaches start or end position
            if self._indicator_pos >= MAX_STEPS:
                self._forward = False
            elif self._indicator_pos <= INDICATOR_START_POS:
                self._forward = True  
                
            # call print function
            self._print_progress_func (self._indicator_pos)
            
            # sleep for interval provided
            time.sleep(self._interval)  
            

# print progress bar
def print_bar(indicator_pos):
    bar = INITIAL_BAR
    bar = bar[:indicator_pos] + '#' + bar[indicator_pos + 1 :]
    
    sys.stdout.write('\r' + bar)
    sys.stdout.flush()
 

# start progress bar
def start():
    global progress

    indicator_pos = True
    progress = ProgressThread(INTERVAL, print_bar, [indicator_pos])
    progress.start() 


# stop progress bar
def stop():
    progress.stop()
    
    
    
    
    
    

    
    


    
