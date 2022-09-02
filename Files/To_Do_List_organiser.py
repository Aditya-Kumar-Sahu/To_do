"""
Program for To-do List Organiser.
"""
from pickle import dump, load
from os import rename, remove

class todo_list:
    def __init__(self, ndate="", ntasks=list()):
        """
        Constructor function.
        
        """
        self.date=ndate
        self.tasks=ntasks
        
        
    def new_date(self):
        """
        To take new date input.
        
        """
        self.tasks=[]
        self.date=input("Enter date(dd/mm/yy): ")
        while True:
            task=input("Enter new task: ")
            if task not in self.tasks:
                self.tasks.append(task)
            ans=input("Add more tasks([y]/n)? ")
            if ans == "n":
                break
        print("Tasks added successfully.")
        
    def modify_tasks(self, date):
        """
        To add/delete task of perticular date.
        
        """
        if date == self.date:
            rec=todo_list()
            with open("todo.dat","rb") as file1:
                try:
                    while True:
                        rec=load(file1)
                        rec.display_tasks(date)
                except EOFError:
                    file1.close()
                    
            print()
            ans=input("Add or delete task(a/d): ").lower()
            if ans=="a":
                task=input("Enter new task: ")
                if task not in self.tasks:
                    self.tasks.append(task)
                print("New task added successfully.")
                
            elif ans=="d":
                num=int(input("Enter serial number of task to delete: "))
                task=self.tasks.pop(num-1)
                print("Task '"+task+"' deleted successfully.")
                
            else:
                print("Invalid input !!!")
        
    def display_tasks(self, date):
        """
        To display tasks of perticular date.
        
        """
        if date == self.date:
            print("\n\n")
            print("{:^42s}".format("Tasks of date "+self.date))
            print("-"*42)
            print("| {:^5s} | {:^30s} |".format("S.No.", "Tasks"))
            print("-"*42)
            s_no=1
            for task in self.tasks:
                print("| {:>4d}. | {:<30s} |".format(s_no, task))
                s_no+=1
            print("-"*42)
    
    def task_complete(self, date):
        """
        To mark task as completed.
    
        """
        if date == self.date:
            rec=todo_list()
            with open("todo.dat","rb") as file1:
                try:
                    while True:
                        rec=load(file1)
                        rec.display_tasks(date)
                except EOFError:
                    file1.close()
                    
            print()
            num=int(input("Enter serial number of task: "))
            task=self.tasks.pop(num-1)
            print(task, "marked as completed.")
            print("Good job !!")
            
def create_datafile():
    """
    To create/reset datafile.
    
    """
    open("todo.dat","wb").close()
    
#-----------------------------------main--------------------------------------
menu='''
----------------------------------
| {:^30s} |
----------------------------------
| {:<30s} |
| {:<30s} |
| {:<30s} |
| {:<30s} |
| {:<30s} |
----------------------------------
'''.format( "MENU", "1. Create/Reset Datafile.", "2. Add New Date.",
            "3. Modify Tasks.", "4. View tasks.", "5. Mark as Complete.")

rec=todo_list()    
while True:
    print(menu)
    act=input("Enter serial number: ")
    
    if act == "1":
        create_datafile()
        print("Datafile created/reset successfully.")
        
    elif act == "2":
        with open("todo.dat", "ab") as file1:
            rec.new_date()
            dump(rec, file1)
            file1.flush()
            file1.close()
            
    elif act == "3":
        # to display dates
        print("-"*16)
        print("| Dates Stored |")
        print("-"*16)
        with open("todo.dat", "rb") as file1:
            try:
                while True:
                    rec=load(file1)
                    print("| {:>12s} |".format(rec.date))
            except:
                file1.close()
        print("-"*16)
        
        # to modify tasks
        date=input("Enter date(dd/mm/yy): ")
        with open("todo.dat","rb") as file1:
            with open("new.dat","wb") as file2:
                try:
                    while True:
                        rec=load(file1)
                        rec.modify_tasks(date)
                        dump(rec, file2)
                except EOFError:
                    file1.close()
        remove("todo.dat")
        rename("new.dat", "todo.dat")
                    
    elif act == "4":
        # to display dates
        print("-"*16)
        print("| Dates Stored |")
        print("-"*16)
        with open("todo.dat", "rb") as file1:
            try:
                while True:
                    rec=load(file1)
                    print("| {:>12s} |".format(rec.date))
            except:
                file1.close()
        print("-"*16)
        
        date=input("Enter date(dd/mm/yy): ")
        with open("todo.dat", "rb") as file1:
            try:
                while True:
                    rec=load(file1)
                    rec.display_tasks(date)
            except EOFError:
                file1.close()
                
    elif act == "5":
        # to display dates
        print("-"*16)
        print("| Dates Stored |")
        print("-"*16)
        with open("todo.dat", "rb") as file1:
            try:
                while True:
                    rec=load(file1)
                    print("| {:>12s} |".format(rec.date))
            except:
                file1.close()
        print("-"*16)
        
        date=input("Enter date(dd/mm/yy): ")
        with open("todo.dat","rb") as file1:
            with open("new.dat","wb") as file2:
                try:
                    while True:
                        rec=load(file1)
                        rec.task_complete(date)
                        dump(rec, file2)
                except EOFError:
                    file1.close()
        remove("todo.dat")
        rename("new.dat", "todo.dat")
        
    else:
        print("Invalid input !!!")
    
    ans=input("Do you want to continue([y]/n): ")
    if ans == "n":
        print("Thank you for using this program.")
        break
