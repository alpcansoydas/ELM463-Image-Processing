def mypgmread(x): #Prints first and secont pixel value
    image = open(x,"r")
    liste = image.readlines()
    print(ord(liste[4][0]),ord(liste[4][1]))
    image.close()
mypgmread("test.pgm")