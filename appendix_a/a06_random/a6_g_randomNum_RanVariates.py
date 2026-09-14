import random

# Importing the random module and calling some of the functions inside it

chkVal = random.random()
print(f"1 ----> random.random() : {chkVal}")

chkVal = random.randrange(1, 6)
print(f"2 ----> random.randrange(1, 6) : {chkVal}")

chkVal = random.uniform(1, 3)
print(f"3 ----> random.uniform(1, 3) : {chkVal}")

chkVal = random.normalvariate(1, 0)
print(f"4 ----> random.normalvariate(1, 0) : {chkVal}")   

chkVal = random.expovariate(3)
print(f"5 ----> random.expovariate(3) : {chkVal}")

