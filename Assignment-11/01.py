import pandas as pd
import datetime

datejan15 = pd.to_datetime('2012-01-15')
print("\nDate time object for Jan 15 2012 = ", datejan15)

datespecific = pd.to_datetime('2012-01-15 21:20:00')
print("\nSpecific date and time of 9:20 pm = ", datespecific)

localdate = pd.to_datetime(datetime.datetime.now())
print("\nLocal date and time = ", localdate)

dateonly = pd.to_datetime('2023-04-10').date()
print("\nA date without time = ", dateonly)

currentdate = pd.Timestamp.now().date()
print("\nCurrent date = ", currentdate)

timefromdate = pd.Timestamp.now().time()
print("\nTime from a date time = ", timefromdate)

currentlocaltime = datetime.datetime.now().time()
print("\nCurrent local time = ", currentlocaltime)