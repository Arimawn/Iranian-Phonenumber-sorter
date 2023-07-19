
#! File directory
readerFile = "B:/Programming Projects/Iran Phone Number/1 milion.txt"
i = 0
#! Open file and read it
with open(readerFile,'r',errors='ignore') as reader:

    for read in reader:
        
        #? Read & write (Mazandaran, Gilan, Golestan) phone number
        if read.startswith('0911'):
            with open('0911.txt','a') as Writer:
                Writer.write(read)
                print(i)
                i += 1
        if read.startswith('0910'):
            with open('0910.txt','a') as Writer:
                Writer.write(read)
                print(i)
                i += 1
        if read.startswith('0912'):
            with open('0912.txt','a') as Writer:
                Writer.write(read)
                print(i)
                i += 1
        if read.startswith('0913'):
            with open('0913.txt','a') as Writer:
                Writer.write(read)
                print(i)
                i += 1
        if read.startswith('0914'):
            with open('0914.txt','a') as Writer:
                Writer.write(read)
                print(i)
                i += 1
        if read.startswith('0915'):
            with open('0915.txt','a') as Writer:
                Writer.write(read)
                print(i)
                i += 1
        if read.startswith('0916'):
            with open('0916.txt','a') as Writer:
                Writer.write(read)
                print(i)
                i += 1
        if read.startswith('0917'):
            with open('0917.txt','a') as Writer:
                Writer.write(read)
                print(i)
                i += 1
        if read.startswith('0918'):
            with open('0918.txt','a') as Writer:
                Writer.write(read)
                print(i)
                i += 1
        if read.startswith('0919'):
            with open('0919.txt','a') as Writer:
                Writer.write(read)
                print(i)
                i += 1
        else:
            with open('Other.txt','a') as Writer:
                Writer.write(read)
                print(i)
                i += 1

