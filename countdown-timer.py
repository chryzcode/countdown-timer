# import the time library
import time

# define a functin
def countdown(t):
     # a loop
    while t:
        # divmod is to show numbers and the remainder. So, it would be shoe=wing the minutes and the seconds
        mins, sec = divmod (t, 60)
        # the display format of the mins and secs
        timer = '{:02d}:{:02d}'. format(mins,sec)
        print(timer, end='\r')
         #sleep the time after a second
        time.sleep(1)
        # the deduction of the time countdown
        t -= 1
    print('Time up')

t = input('Enter the time in seconds: ')
countdown(int(t))
