#A school decided to replace the desks in three classrooms.Each desks sits two students .
#Given the number of students in each class,print the smallest possible number of desks that can be purchesed.
#The program  should read three integers :the number of students in each of the three classes ,a ,b and c respectively.
#In the first class there are three groups.The first group has 20 students and thus needs 10 desks.The second group has
#21 students,so they can get by with no fever than 11 desks.11 desks are also enough for the third group of 22 students.
#so, we need 32 desks in total.

stds_in_class_a = 20
min_desk_in_class_a = (stds_in_class_a//2)
print(f"The minimum number of desks required in class a is {min_desk_in_class_a}.")

stds_in_class_b = 21
min_desk_in_class_b = ((stds_in_class_b//2)+1)
print(f"The minimum number of desks required in class b is {min_desk_in_class_b}.")

stds_in_class_c = 22
min_desk_in_class_c = (stds_in_class_c//2)
print(f"The minimum number of desks required in class c is {min_desk_in_class_c}.")