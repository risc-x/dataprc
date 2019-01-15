# separate v and h, and delete first 71 lines in a file. Finally, create two files.

for i in range(1, 21):
    with open('v{}.txt'.format(i)) as reader,\
    open('vv{}.txt'.format(i), 'w') as writerv, \
    open('vh{}.txt'.format(i), 'w') as writerh:
        for index, line in enumerate(reader):
            if index < 46:
                continue
            elif index == 46:
                if line[7] == 'h':
                    h = 0
                else:
                    h = 1
            elif index < 71:
                continue
            else:
                if h == 0:
                    writerh.write(line[:79])
                    writerh.write('\n')
                    writerv.write(line[79:])
                else:
                    writerv.write(line[:79])
                    writerv.write('\n')
                    writerh.write(line[79:])          
