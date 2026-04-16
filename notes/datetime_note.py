import datetime

date = datetime.date(2024, 12, 30)
today = datetime.datetime.today()

time = datetime.time(14, 30, 45)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d-%m-%Y")
# print(now)

target_date = datetime.datetime(2020, 12, 30)
current_date = datetime.datetime.now()

# if target_date > current_date:
#     print("The target date is in the future.")
# else:
#     print("The target date is in the past.")

print(current_date - target_date)