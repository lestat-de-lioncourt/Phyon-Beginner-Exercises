# factors.py

# Find the factors of a positive integer

n = int(input("Enter a positive integer: "))

#Determine the factor of an integer and print out the factors of that number

for i in range(1,n + 1):
    if n%i == 0:
        print(f"{i} is a factor of {n}")


