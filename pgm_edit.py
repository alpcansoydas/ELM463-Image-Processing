def pgm_edit(x):
    image = open(x,'rb')
    filename = "mylena.pgm"
    fout = open(filename,'wb')
    header1 = image.readline()
    header2 = image.readline()
    header3 = image.readline()
    header4 = image.readline()
    pixel_data = image.read() #pixel data
    
    pgmHeader = header1  + header2  + header3  + header4
    
    pixel_data_list = list(pixel_data) # Converting bytearray to list to manipulate data
    
    for i in range(30*512,51*512+1):
        pixel_data_list[i] = 0

    y = bytearray(pixel_data_list) # Converting back to bytearray
    
    # write the header and data to the file
    fout.write(pgmHeader)
    fout.write(y)

    image.close()
    fout.close()

pgm_edit('lena.pgm')



