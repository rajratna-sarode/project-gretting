import time 
timestamp=time.strftime('%H:%M:%S')

timestamp=time.strftime('%H')

if (int(timestamp))<12 :
    print("good morning sir")
elif (int(timestamp))<16:
    print("good afternoon sir")
else:
    print("good evening sir")