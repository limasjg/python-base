import time

my_time = int(input("Enter a time in seconds: "))

for x in range(my_time, 0, -1):
    hours = int(x / 3600)
    minuts = int(x / 60) % 60
    seconds = x % 60
    print(f"{hours:02}:{minuts:02}:{seconds:02}")
    time.sleep(1)
print("Time's up!")