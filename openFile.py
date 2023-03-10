
##open a file in python and print different file attributes
file = open("data-file-resource/textFile.txt")
print("File mode :" ,file.mode)
#file.close()
print("File is closed :" , file.closed)
print("File name :" , file.name)
print("File encoding" , file.encoding)
print(file.read())
print(file.tell()) ## tells the location of cursor
file.seek(20) ## moves the cursor to the passed seek argument

with open("data-file-resource/textFile.txt") as f:
    print(f.readlines())
print(f.closed) ## opening a file in with block makes sure that file is closed after operation is performed