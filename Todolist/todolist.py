import time 
import os
tasks=[]
NUM = 0

class task:
    content =''
    def __init__(self) -> None:
        self.status =False

    def taskcompleted(self):
        self.status = True 

    def addTask(self ,content):
        self.content = content

    def content(self):
        return  self.content

    def __repr__(self):
        return self.content

    def taskdata(self):
        print(self.content ,end= "\t")
        if self.status == True :
            print('Status: Completed ')
        elif self.status == False:
            print('Status: Incomplete ')
    
def deleteTask(index):
    index-=1
    strForm=tasks[index]
    tasks.remove(strForm)

def taskCompleted(index):
    index-=1
    task1 = tasks[index]
    task1.taskcompleted()


if __name__ == '__main__':
    while True :
        os.system('cls')
        NUM =0 
        print('\t\tWelcome to the todolist app')
        print(' \t\t 1.Create the task \n\t\t 2.Update the task \n\t\t 3.Track the tasks \n\t\t 4.Exit')
        choice=input('Enter the number to perform the operation: ')
        if choice == '1':
            content = input('Enter the task: ')
            createdtask = task()
            createdtask.addTask(content)
            tasks.append(createdtask)
            print('Creating task......')
            time.sleep(4)

        elif choice == '2':
            while True:
                os.system('cls')
                print(f'Unfinished task list ( {len(tasks)} ) ')
                NUM = 0
                for i in tasks:
                    NUM+=1
                    index = NUM
                    print(f"\t\t{index}.",end=' ')
                    i.taskdata()
                print('\n','-'*70)
                print("\n\t\t 1.Delete task \n\t\t 2.Complete task \n\t\t 3.Go to main menu  ")
                choice2 = input('Enter the number to perform the operation: ')
                if choice2 == '1':
                    index=int(input('Enter the task number to remove it: '))
                    try :
                        deleteTask(index)
                    except Exception as e:
                        print(e)
                    print('Deleting the task.....')
                    time.sleep(3)
                elif choice2 == '2':
                    index = int(input('Enter the task number to mark the task completed :'))
                    try:
                        taskCompleted(index)
                    except Exception as e:
                        print(e)
                    print('Changing status......')
                    time.sleep(3)
                elif choice2 == '3':
                    print('Going to main menu....')
                    time.sleep(3)
                    break
                else:
                    print('Wrong choice, Try Again')
        elif choice == '3':
            os.system('cls')
            NUM = 0
            print(f'\t\t\tTasks and Status ( {len(tasks)} ) ')
            for i in tasks:
                    NUM+=1
                    index = NUM
                    print(f"\t\t{index}.",end=' ')
                    i.taskdata()            
            time.sleep(5)
        elif choice == '4':
            print('WE are EXITING..... ')
            time.sleep(3)
            break 
        else :
            print('Invalid choice please ,Try again!! ')
            time.sleep(3)
        

