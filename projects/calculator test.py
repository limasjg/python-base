import time

time_sec = int(input("Enter a time in seconds: "))

for x in range(time_sec, 0, -1):
    hours = x // 3600
    minuts = x // 60 % 60
    seconds = x % 60
    print(f"{hours:02}:{minuts:02}:{seconds:02}")
    time.sleep(1)
print("Time is Over!")