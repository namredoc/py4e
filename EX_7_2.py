


while True:
        try:
            count = 0
            avg = 0.0
            fname = input("Enter file name: ")
            if fname == 'quit':
                print("See you later")
                break
            fh = open(fname)
        except:
            print('File',fname,'cannot be opened.')
            continue


        for line in fh:
            if not line.startswith("X-DSPAM-Confidence:"):
                continue
            else:
                count = count + 1
                d_dots = line.find(':')
                v_string = line[d_dots +1:]
                value = float(v_string.strip())
                avg = avg + value

        print("Average spam confidence:", avg/count)