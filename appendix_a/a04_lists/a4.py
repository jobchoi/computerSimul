# A.4.1
# Lists and some of their operations
a = []

print(a)

b = [1, 2, 3, "Arrival", False]

print(f"b[0] => {b[0]}") 
print(f"b[2] => {b[2]}")
print(f"b[0:2] => {b[0:2]}")

c = [0] * 6

print(f"c => {c}")
print(f"len(c) => {len(c)}")

print(f"'Arrival' in b => {'Arrival' in b}")

d = b+b
print(f"d => {d}")