from datetime import datetime, date, time

today = date.today()
print(today)

tomorrow = date(2023, 8, 29)
print(tomorrow)

next_week = date.fromisoformat('2023-08-31')
print(next_week)

right_now = datetime.now()
print(right_now)

print(right_now.timestamp())

my_date = datetime.fromtimestamp(1500000000)
print(my_date)

