import atexit
from time import clock
from functools import reduce

def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % \
        reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],
            [(t*1000,),1000,60,60])

line = "="*40
def log(s, elapsed=None):  #timing.log(s) in order to get running time in a crucial point while running (s variable as a description to the reason log was called)
    print(line)
    secs =  clock() - elapsed if elapsed else clock()
    print(str(secs), '-', s)
    if elapsed:
        print("Elapsed time:", elapsed)
    print(line+'\n')
    return secs # returns seconds as float

def endlog():
    end = clock()
    elapsed = end-start
    log("End Program", elapsed)

def now():
    return secondsToStr(clock())

start = clock()
atexit.register(endlog)
log("Start Timing")