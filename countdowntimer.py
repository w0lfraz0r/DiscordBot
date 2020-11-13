#every thursday 9.35 pm IST a new game is set free
#UTC that time is thurday 4.35pm
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
stopwatch(15)