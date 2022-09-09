#fname = input("Enter file:")
#fh = open(fname)
fh = open('mbox-short.txt')

counts = dict()

for line in fh:
    if not line.startswith('From '):
        continue
    else:
        line = line.split()
        # print(line)
        e_address = line[1]
        # print(e_address)
        counts[e_address] = counts.get(e_address, 0) + 1

# print(counts)

f_address = None
f_count = None
for e_address,count in counts.items():
    if f_count is None or count > f_count:
        f_address = e_address
        f_count = count
print(f_address, f_count)


