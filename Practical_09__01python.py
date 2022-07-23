import subprocess as sp 

print("Currently available *.py python scripts : ")
screen_output = sp.call("powershell ls -Filter *.py",shell=True)

file_name1 = input("Enter the file name : ")

with open(file_name1,"r") as FILE1 :
    content = FILE1.readlines()
    print(type(content))
    
    # print(content)
    SIZE = 0
    while SIZE != len(content):
        # print(content[SIZE],end='')
        if '#' in str(content[SIZE]) :
            pass
        else :
            print(str(content[SIZE]),end='')
        SIZE+=1
        