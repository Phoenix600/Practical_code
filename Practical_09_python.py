class Employee :
    def __init__(self,name,age) :
        self.name = name
        self.age  = age

    def Display(self):
        print(f"""
        [+] Name    :   {self.name}
        [+] Age     :   {self.age}
        """)

class Manager(Employee):
    def __init__(self,name,age,sal,addr):
        self.sal    =   sal
        self.addr   =   addr

        Employee.__init__(self,name,age)

    def Display(self):
#        Employee.Display(self)
        print(f"""
        +------------------------------------------------------
        | Employee Details 
        +------------------------------------------------------
        |[+]Name     :   {self.name}
        +------------------------------------------------------
        |[+]Age      :   {self.age}
        +------------------------------------------------------
        |[+]Salary   :   {self.sal}
        +------------------------------------------------------
        |[+]Address  :   {self.addr}
        +------------------------------------------------------
        """)


def createEmployeeDataBase(Enum,EM_DataBase) :
    for INDEX in range(0,Enum):
        print(f"Enter the Details of employee[{INDEX+1}]")
        name    =   input("Enter your name  : ")
        age     =   input("Enter your age   : ")
        sal     =   input("Enter your sal   : ")
        addr    =   input("Enter your addr  : ")
        manager_object = Manager(name,age,sal,addr)
        EM_DataBase.append(manager_object)
def printDataBase(EM_DataBase):
    for OBJECT in EM_DataBase :
        OBJECT.Display()

# driver Code 
if __name__ == "__main__":
    EM_DataBase = []
    createEmployeeDataBase(2,EM_DataBase)
    printDataBase(EM_DataBase)
