# this is the comment
file_1 = input("Enter python file name whose code you want to copy : ")
file_2 = input("Enter file name which will be created containing the code of file_1 without comment : ")
with open(file_1) as file1:
 
    with open(file_2,"w") as file2:
        while True:
            text = file1.readline()
            if len(text) != 0 :
                if text[0] == "#":
                    continue
                else :
                    file2.write(text)
            else :
                break
# this is also a comment 
file1.close()
file2.close()
