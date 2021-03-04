#Given the integer N- the number of minutes that is passed since midnight -how many hours and minutes are displayed
# on the 24 hrs digital clock? The program should print two numbers: the number of hours (between 0 and 23) and the
#number of minutes (between 0 and 59).
#for example, if N = 150 ,then 150 minutes have passed since midnight -i:e now is 2:30 am.So the program should print 2 30.

hours = int(input("How many hours have passed after midnight? "))
minutes = int(input("How many minutes have passed after midnight? "))
hours_in_minutes = hours*60
minutes_after_midnight = (hours_in_minutes)+(minutes)
print(f"{minutes_after_midnight} minutes have passed after midnight")