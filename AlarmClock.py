from datetime import datetime
import time

# Set hour and minute for alarm
print("Enter hour: ", end="")
input_hour = int(input())

print("Enter minute: ", end="")
input_minute = int(input())

# Print the current time
now = datetime.now()
currentTime = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
print(currentTime)

# creates new datetime from entered hour and minute
input_time = datetime(now.year, now.month, now.day, input_hour, input_minute)

initialSleep = True

while(input_time.hour != now.hour or input_time.minute != now.minute):
    time.sleep(60 - now.second)
        
    now = datetime.now()
    currentTime = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
    print(currentTime)


print("!!!ALARM GOING OFF!!!")



