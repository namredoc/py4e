# Use the file name mbox-short.txt as the file name

# fname = input("Enter file name: ")
count = 0
avg = 0.0
try:
    fname = input("Enter file name: ")
    fh = open(fname)
except:
    print('File',fname,'cannot be opened.')
    exit()

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count = count + 1
        d_dots = line.find(':')
        v_string = line[d_dots +1:]
        value = float(v_string.strip())
        avg = avg + value
        # print(value, count, avg/count)   

    # print(line)
print("Average spam confidence:", avg/count)
