import os 

## open a file in write mode by passing "w" as arg to open fn
file = open("../data-file-resource/textFile.txt" , 'w')
file.write("I love my life! ") ## overrides the content every time
##print(file.readlines())
file.close()


### open in write mode to write into the files , if file does not exist ..python will create the file first
with  open("../data-file-resource/example.txt" ,'w') as f:
    f.write("I love BTS")


with open ("../data-file-resource/textFile.txt" , 'a') as file_apend_mode:
    file_apend_mode.write("It is going to be a good year.\n")



with  open("../data-file-resource/textFile.txt") as f:
    for lines in f:
        print(lines)


### open in r+  mode to add additional content to an existing file
with  open("../data-file-resource/textFile.txt" , 'r+') as f:
        f.writelines("Opened the file in r+ mode\n")
        print(f.tell())
       ## f.write("r+ mode allows to read and write the files")
        print(f.readlines())


##in r+ mode cursor is at the begining of the file while in a+ mode cursor is at the end of the file
os.rename("../data-file-resource/example.txt" , "../data-file-resource/renamed.txt")
os.remove("../data-file-resource/example.txt")