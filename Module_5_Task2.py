from random import choice

from File_Appending import appending_file

y=int(input('Enter the Number 25 to write multiple lines inside output.txt '))

if y==25:
    x=str(input('Enter text to write to the file:'))
    file1=open('output.txt','w')
    writing_file=file1.write(x)
    print(writing_file)
    print('Data Successfully written to output.txt .')

    a=int(input('Enter the Number of lines you want to append:'))

    choice = True
    for i in range(0,a):
        z=str(input('Enter Additional text to append:'))
        file1 = open('output.txt', 'a')
        file1.write('\n')
        appending_file=file1.write(z)
        print(appending_file)
        choice = input('Enter True/False to proceed further:')
        if choice == False:
            break

    file1 = open('output.txt', 'r')
    readingfile = file1.readlines()
    print('Final Content of the Output File:')
    print(readingfile)
    file1.close()




else:
    print('InValid Number Entered')











