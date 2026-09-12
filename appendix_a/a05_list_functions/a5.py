# A.5 list functions
# Transposing a matirx using the zip function. Matrix is first unpacked using the start(*) operator

matrix = [[1,2], [3,4]]
matrix_transposed = list(zip(*matrix))

print(f"matrix => {matrix}")    
print(f"matrix_transposed => {matrix_transposed}")