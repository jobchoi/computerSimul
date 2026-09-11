# A.3.1
# Binary operations on integer numbers
print("Binary operations on integer numbers --- A.3.1")
a = 10 # 0000 1010
b = 25 # 0001 1001

# AND
c = a & b 
print(f"a & b : {c}") # 0000 1000 (8)

# OR
c = a | b
print(f"a | b : {c}") # 0001 1011 (27)

# XOR
c = a ^ b
print(f"a ^ b : {c}") # 0001 0011 (19)  

# Ones Complement
# Numbers are in 2's complement representation
c = ~a
print(f"~a : {c}") # 1111 0101 (-11)

# Right Shift
c = a >> 2
print(f"a >> 2 : {c}") # 0000 0010 (2)

# Left Shift
c = a << 2
print(f"a << 2 : {c}") # 0010 1000 (40)


# # A.3.2
# # Handling unsigned binary numbers
# print("\nHandling unsigned binary numbers --- A.3.2")

# Convert an integer to a binary string
b = bin(5)
print(f"bin(5) : {b}") # 0b101  

# Convert a binary string to an integer
a = int(0b_101)
# a = int(0b101)
print(f"int(0b_101) : {a}") # 5
# print(f"int(0b101) : {a}") # 5

# Unsigned binary numbers
a = 0b_0000_0011    # 3
b = 0b_1000_0011    # 131

print(f"a + b : {a + b}") # 134
print(f"a & b : {a & b}") # 3
print(f"a | b : {a | b}") # 135
print(f"a ^ b : {a ^ b}") # 132
print(f"~a : {~a}") # -4
print(f"a >> 2 : {a >> 2}") # 0
print(f"a << 2 : {a << 2}") # 12

# Print resulutin binary format
print(bin(a>>2)) # 0b0
print(bin(a<<2)) # 0b1100
