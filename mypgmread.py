import array as ar

def mypgmwrite(x):
    # define the width  (columns) and height (rows) of your image
    width = 3
    height = 3
    
    buff=ar.array('B') # declare 1-d array of unsigned char and assign it random values

    for i in range(101,110):
      buff.append(i)

    fout = open(x,'wb')

    # define PGM Header
    pgmHeader = 'P5' + '\n' + '#mypgmwrite' + '\n' + str(width) + ' ' + str(height) + '\n' + str(255) + '\n'

    # write the header to the file
    fout.write(pgmHeader.encode())

    # write the data to the file 
    buff.tofile(fout)

    fout.close()

mypgmwrite("test.pgm")