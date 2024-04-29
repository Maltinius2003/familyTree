from datetime import datetime, timedelta

date1 = datetime(1582, 10, 4)
date2 = datetime(1582, 10, 15)

if date1.year == 1582 and date1.month == 10 and date1.day < 15 and date2.year == 1582 and date2.month == 10 and date2.day >= 15:
    difference = date2 - date1 - timedelta(days=10)
else:
    difference = date2 - date1

print(f"The difference between {date1} and {date2} is {difference.days} days.")