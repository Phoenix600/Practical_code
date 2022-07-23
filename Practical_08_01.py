#Import your modudles here
import subprocess as sp
from tkinter.filedialog import Open 

DIR_LIST    = sp.call("powershell ls -Filter *.py ",shell=True)
print(f"""---------------------------------------- 
Python Scripts in Current directory :
---------------------------------------- """)
filename_01 = input("[+]Enter the source file name  : ")
filename_02 = input("[+]Enter new file name to save : ")

#---------------- Opening the FILE1 for operations --------------------
FILE1       = open(filename_01,"r")
code        = FILE1.readlines()
code_len    = len(code)

# ------------- OPening the FILE2 to keep record of saved operations----
FILE2       = open(filename_02,"w")
# ------------ Removing the single lines comments ------------------------
INDEX = 0 
while INDEX != code_len :
    if '#' in str(code) :
        FILE2.write(str(code[:code.index('#')]))
    else :
        # print(str(code[:code.index('#')]))
        # print(FILE2)
        FILE2.write(str(code[INDEX]))
    INDEX+=1

# # content = FILE2.read()
# print(content)

FILE2.close()
FILE1.close()