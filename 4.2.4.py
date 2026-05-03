import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

product_pairs=[]
for date,group in df.groupby('Date'):
	products=group['Product'].unique()
	if len(products)>1:
		pairs=combinations(sorted(products),2)
		product_pairs.extend(pairs)


pair_counter=Counter(product_pairs)

max_freq=max(pair_counter.values())
most_frequent_pairs=[pair for pair ,count in pair_counter.items() if count==max_freq]

for pair in most_frequent_pairs:
	print(f"{pair[0]} and {pair[1]}: {max_freq} times")
# Output the most frequent product pairs