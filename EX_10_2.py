name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)
counts = dict()

for line in handle:
    if not line.startswith('From '):
        continue
    else:
        line = line.split()
        f_time = line[5]
        time = f_time.split(':')
        hour = (time[0])
        counts[hour] = counts.get(hour, 0) + 1



# Resolving the exercise with list of tuples
lst = list()
for key, val in counts.items():
    # hour_reorder = (val, key)
    hour_order = (key, val)
    lst.append(hour_order)

lst = sorted(lst)

for key,val in lst:
    print(key, val)


#Resolving 2
# x = sorted(counts.items())
# for key, val in x:
#     print(key, val)


