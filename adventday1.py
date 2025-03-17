import sys
nums = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}
with open(sys.argv[1]) as f:
    ans = 0
    for line in f:
        line = line.strip() 
        lineval = ''
        secondval = ''
        for i, c in enumerate(line):
               if len(lineval) == 0:
                    if c.isdigit(): 
                            lineval += c
                    elif len(line) >= i+3 and line[i:i+3] in nums: 
                            lineval += str(nums[line[i:i+3]])
                    elif len(line) >= i+4 and line[i:i+4] in nums:
                            lineval += str(nums[line[i:i+4]])
                    elif len(line) >= i+5 and line[i:i+5] in nums:
                            lineval += str(nums[line[i:i+5]])
               if len(lineval) > 0:
                    if c.isdigit(): 
                           secondval = c
                    elif len(line) >= i+3 and line[i:i+3] in nums:
                           secondval = str(nums[line[i:i+3]]) 
                    elif len(line) >= i+4 and line[i:i+4] in nums:
                           secondval = str(nums[line[i:i+4]]) 
                    elif len(line) >= i+5 and line[i:i+5] in nums: 
                           secondval = str(nums[line[i:i:5]]) 

        lineval += secondval
        ans += int(lineval)
print(ans)
