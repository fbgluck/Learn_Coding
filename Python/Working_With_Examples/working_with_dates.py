# Ref: https://docs.python.org/3/library/datetime.html
import datetime as obj_dt  # Allows us to work with dates
date_now = obj_dt.datetime.now()
print(f"It is now {date_now}")

birth_date = obj_dt.datetime(1956, 6, 3)
print(f"You were born on {birth_date}")

how_long = date_now - birth_date
# 24hr*60min*60sec
print(f'You have been alive for {how_long.days*86400:,} seconds')
# seconds seems to have a max value that recycles so we can't use the following
# print (f"You have been alive for {how_long.seconds} seconds")
print(f"You have been alive for {how_long.days:,} days")
print(f"You have been alive for {how_long.days/365:.3f} Years")
