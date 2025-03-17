import sys
with open(sys.argv[1]) as f:
	keys = []
	for line in f:
		print(line)
		line = line.rstrip()
		keys += list(line.lower())
my_dict = {}
for char in keys:
	if char != ' ':
		my_dict[char] = keys.count(char)	
print('The most common character is: ',repr( max(my_dict, key = my_dict.get)))
