# Simple py program to print time using datetime module
import datetime
now = datetime.datetime.now()
print("Current Date and Time")
print(now.strftime("%Y-%m-%d  %H:%M:%S"))
