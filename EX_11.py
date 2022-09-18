import re

# Solution 1

# summ = 0
# numm = 0
# fh = open('regex_sum_1618683.txt')
# for line in fh:
# 	line = line.rstrip()
# 	numbers = re.findall('[0-9]+', line)
# 	# print(numbers)
# 	for number in numbers:
# 		# print(number)
# 		numm = numm + 1
# 		number = int(number)
# 		summ = summ + number

# print(summ, numm)

# =========================

# Solution 2

# x = 0
numlist = list()
fh = open('test_text.txt')
lines = fh.read()
numbers = re.findall('[0-9]+', lines)
for number in numbers:
	number = int(number)
	numlist.append(number)
	# x = x + number
print(numbers, sum(numlist))