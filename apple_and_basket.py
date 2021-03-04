#N students take K apples and distribute them among each other evenly.The remaining (the divisble) part
#remains in the basket. How many apples will each single student get? How many apples will remain in the basket?
#The program reads the number N and K. It should print the 2 answers from the question above.

N = int(input("Enter the number of students: "))
K = int(input("Total Number of Apples: "))
X = K/N

print(f"Each student will get {X} number of apple")

print (f"If you eat more than {X} apples a day, you'll gain weight")