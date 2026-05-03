import numpy as np

# Input matrices
print("Enter Matrix A:")
matrix_a = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Matrix B:")
matrix_b = np.array([list(map(int, input().split())) for i in range(3)])


# Addition
print("Addition (A + B):")
add=np.array(matrix_a+matrix_b)
print(add)
# Subtraction
print("Subtraction (A - B):")
sub=np.array(matrix_a-matrix_b)
print(sub)
# Multiplication (element-wise)
print("Element-wise Multiplication (A * B):")
multi=np.array(matrix_a*matrix_b)
print(multi)
# Matrix multiplication (dot product)
print("A dot B:")
trans=(matrix_a.dot(matrix_b))
print(trans)
# Transpose
print("Transpose of A:")
tran=matrix_a.transpose()
print(tran)