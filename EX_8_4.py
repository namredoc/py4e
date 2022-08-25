fname = input("Enter file name: ")
fh = open(fname)


lst = list()

fh = open('romeo.txt')
lst = list()
for line in fh:
    line = line.split()

    for word in line:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)





# for line in fh:
#     line = line.rstrip()
#     # lst.append(line)
#     words = line.split()
#     lst.append(words)
# print(lst)
# # print(lst.rstrip()


    # for word in s_line:
    #     if word in s_line:
    #         pass
    #     else:
    #         lst.append(word) 
    #     print(lst)



# for word in s_line:
#     if word in s_line:
#         continue
#     else:
#         lst.append(word)
# print(lst)






    # lst.append(line)
    # print(s_line)


# print(line.rstrip())
