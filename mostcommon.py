import sys
my_dict = {}
with open(sys.argv[1]) as f:
	for line in f:
		print(line)
		line = line.strip()
		keys = line.split()	
		stripped_words = [word.strip('?,.!').lower() for word in keys]
		for word in stripped_words:
			if word not in my_dict:
				my_dict[word] = 0
			my_dict[word] += 1

print('The most common word is:', max(my_dict.items(), key = lambda kv: kv[1])[0]) 
