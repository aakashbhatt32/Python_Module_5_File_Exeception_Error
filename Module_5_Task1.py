

file_name=str(input('Enter the Filename including the extension'))

if file_name=='sample.txt':
    file_name1=open('sample.txt','r+')
    readfile=file_name1.readlines()
    print(readfile)

else:
    print('The file you enter',file_name,'was not found')





