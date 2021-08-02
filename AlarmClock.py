import time

currentTime = time.localtime()
timeString = time.strftime("%m/%d/%Y, %H:%M:%S", currentTime)

print("Current Time: " + timeString)
    