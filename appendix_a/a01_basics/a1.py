

# # A.1.1
# Starting a new Python interactive session.
# print("Addition of two numbers ---- A.1.1") 
# a = 1
# b = 2
# print(f"{a}, {b} : {a + b} ")

# # A.1.2
# print("Addition of two numbers ---- A.1.2")
# num1, num2 = input("Enter a two number: ").split()
# # print(f"You entered: {getNumber}")
# print(f"Result : {int(num1) + int(num2)}")


# A.1.3
# from random import choice

# print("Random number generator ---- A.1.3")

# lower = input("Enter smallest number: ")
# upper = input("Enter largest number: ")
# n = input("How many numbers do you want to generate? ")

# # Parse string into integers
# lower = int(lower)
# upper = int(upper)
# n = int(n)  

# # Constuct a list from a range object
# numbers = list(range(lower, upper + 1))

# selection =[]

# for i in range(n):
#     r = choice(numbers)
#     selection.append(r)
#     numbers.remove(r)

# print("Your numbers :", selection)