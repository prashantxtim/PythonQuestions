#Write a program to convert seconds to day, hour, minutes and seconds.

second = int(input("Enter the second: "))
minutes = second/60
hours = ((second / 60) / 60)
day = (((second/60)/60)/24)
remain_second = second % 60
print(f"The time in minutes is {minutes}")
print(f"The time in hours is {hours}")
print(f"The time in day is {day}")
print(f"Remaining seconds is {remain_second}")