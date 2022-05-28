# -*- coding: utf-8 -*-
"""ToDoList.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Glu8cDpklv6R0AYAzOcap70zW5UKOGpb
"""

#ToDo List
#import prettytable for creating our app
from prettytable import PrettyTable
from datetime import datetime as dt
import datetime
print("My to do list")

instructions='''1.enter A to add new ToDo
2.enter D to delete ToDo
3.enter U to update ToDo
4.enter E to add exit the programm
5.enter C to add check the programm'''
print (instructions)

#add all information in the to-do list
my_todo_list=[]
mytime = []

x=PrettyTable()

#function for updating the List

def my_list(my_todo_List, mytime):
    x.field_names=["items Names", "Due Date"]
    for i, t in zip(my_todo_List, mytime):
        #addition of new row to PrettyTable on each interation
        x.add_row([i,t])

        print(x.get_string(title= "To Do List"))
        x.clear_rows

runing=True
while runing:
    customer_input=input("What do are your plans to do? (A,D,U,E,C):")
    if customer_input=="A":
        new_todo= input("please enter a new ToDo:").lower()
        due = dt.strptime(input('please enter when its due: yyyy,mm,dd,h,m'), '%Y,%m,%d,%H,%M')
        print ("Your current ToDo is ", new_todo, ' its due on: ', due)
    #append the new todo in the list
        my_todo_list.append(new_todo)
        mytime.append(due)
    elif customer_input=="D":
  #customer to enter item name
            item_name=input("please enter a name of an item you want to delete.").lower()
            try:
                if item_name in my_todo_list:
            #confirmation
                    choice =input("are you going to delete{item_name} from your ToDo list? (y/n)").lower()
            except:
                print('please enter a valid name')
            if choice =="y":
            #remove item from list
                idx = my_todo_list.index(item_name)
                del my_todo_list[idx]
                del mytime[idx]
                
                print("your updated ToDo List:")
                x = PrettyTable()
                x.add_column('Tasks', my_todo_list)
                x.add_column('Due Date', mytime)
                print('Your task has been updated. Your new ToDo list is:')
                print(x)
                
                    
            

    elif customer_input=="U":
        new_task= input("please enter a new task:").lower()
        due_d = dt.strptime(input('please enter when its due: yyyy,mm,dd,h,m'), '%Y,%m,%d,%H,%M')
        print ("Your new task is ", new_task, ' its due on: ', due_d)
    #append the new todo in the list
        my_todo_list.append(new_task)
        mytime.append(due_d)
        x = PrettyTable()
        x.add_column('Tasks', my_todo_list)
        x.add_column('Due Date', mytime)
        print('Your task has been updated. Your new ToDo list is:')
        print(x)
         
                
    elif customer_input=="E":
        pass
    elif customer_input=="C":
            x = PrettyTable()
            x.add_column('Tasks', my_todo_list)
            x.add_column('Due Date', mytime)
            print(x)
    elif customer_input=="" or customer_input== " ":
        print("please enter something")
    else:
        print("please enter a vaid value")