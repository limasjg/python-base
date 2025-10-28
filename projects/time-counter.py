# Create a time counter using the time library
import time

# initial = int(input("Enter initial time: "))
# final = int(input("Enter a final time: "))

# for x in reversed(range(initial, final+1)):
#     print(x)
#     time.sleep(1)
# print("its TIME!")

# temp = int(input("Enter the time that you want to count: "))

# for x in reversed(range(1, temp+1)):
#     print(x)
#     time.sleep(1)
# print("its TIME!")

# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x /60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#     days = x // 86400
#     remaining_seconds = x % 86400
#     hours = remaining_seconds // 3600
#     remaining_seconds = remaining_seconds % 3600
#     minutes = remaining_seconds // 60
#     seconds = remaining_seconds % 60
#     print(f"Day/s {days} {hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

my_time = int(input("Enter a time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = (x // 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)