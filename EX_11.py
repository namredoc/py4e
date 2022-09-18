import re

# Solution 1

numlist = list()
fh = open('test_text.txt')
lines = fh.read()
numbers = re.findall('[0-9]+', lines)
for number in numbers:
	number = int(number)
	numlist.append(number)
print(numbers, sum(numlist))


# =========================

# Solution 2


summ = 0
numm = 0
fh = open('regex_sum_1618683.txt')
for line in fh:
	line = line.rstrip()
	numbers = re.findall('[0-9]+', line)
	for number in numbers:
		numm = numm + 1
		number = int(number)
		summ = summ + number

print(summ, numm)