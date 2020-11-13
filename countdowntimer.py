#every thursday 9.35 pm IST a new game is set free
#UTC that time is thurday 4.35pm --16.35pm
#weekdays numbers 0-moday,1-tuesday,,,,,3-THURSDAY
import time as t
## Countdown function starts here
def stopwatch(sec):
    while sec:
        minn, secc = divmod(sec, 60)
        timeformat = '{:02d}:{:02d}'.format(minn, secc)
        print(timeformat, end='\r')
        t.sleep(1)
        sec -= 1
    print('Today is the day you get a new game\n')
## calling stopwatch function
Today = datetime.datetime.utcnow()
if Today.weekday() == 3:
    stopwatch(15)###time now
else:
    #86400 seconds in 1 day, sleep for 1 day
    sleep(86400)