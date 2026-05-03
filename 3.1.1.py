import numpy as np

# write your code here...
rows,columns=map(int,input().split())
elements=[]
for i in range (rows):
	row=list(map(int,input().split()))
	elements.extend(row)
array=np.array(elements).reshape(rows,columns)
print(array)
print(array.ndim)
print(array.shape)
print(array.size)