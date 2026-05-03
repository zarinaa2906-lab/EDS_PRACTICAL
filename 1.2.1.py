# write your code here
n = int(input())
marks = list(map(int,input().split()))
failed = False
for m in marks:
	if m < 40:
		failed=True
		break
if failed:
	print("Fail")
else:
	total = sum(marks)
	agg = total/n
	print("Aggregate Percentage: "f"{agg:.2f}")
	if agg > 75:
		print("Grade: Distinction")
	elif agg >= 60:
		print("Grade: First Division")
	elif agg >= 50:
		print("Grade: Second Division")
	elif agg >= 40:
		print("Grade: Third Division")
				