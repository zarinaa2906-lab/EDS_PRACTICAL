#write your code here...
import math
number = int(input())
if 1 <= number <= 9:  #Single-digit number
	print(number ** 2)
elif 10 <= number <= 99:  #Two digit number
	print(f"{math.sqrt(number):.2f}")
elif 100 <= number <= 999: #Three-digit number
	print(f"{math.cbrt(number):.2f}")
else:
	print("Invalid")
