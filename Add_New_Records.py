from tkinter import *
import pymysql
from tkinter import messagebox
import Menu_window

""""""""""""""""""""" DATABASE CONNECTION  """""""""""""""""

conn=pymysql.connect(host="localhost",user="root",password="qwerty",db="test")
aa=conn.cursor()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



def addnew():
    def gobackto_menu():
        root.destroy()
        Menu_window.view()
        
    def insert():
          name=Name.get()
          mobile=Mobile.get()
          dob=DOB.get()
          marks=Marks.get()
          ET2.delete(0,END)
          ET3.delete(0,END)
          ET4.delete(0,END)
          ET5.delete(0,END)
          
          query="insert into pythonentry (name,mobile,dob,marks) values('"+name+"','"+mobile+"','"+dob+"','"+marks+"')"
          aa.execute(query)
          conn.commit()
          messagebox.showinfo("Success","Record Inserted")


    root=Tk()
    Marks=StringVar()
    Name=StringVar()
    DOB=StringVar()
    Mobile=StringVar()
    
    root.geometry('500x400')
    root.title('Add New Records')

    LB1=Label(root,text="Add New Records",font=('bold',18))
    LB1.place(x=200,y=50)

    LB2=Label(root,text="Enter Name :-",font=('bold',18))
    LB2.place(x=10,y=100)
    ET2=Entry(root,textvariable=Name,font=('bold',14))
    ET2.place(x=250,y=100)  
    LB3=Label(root,text="Enter Mobile no :-",font=('bold',18))
    LB3.place(x=10,y=150)
    ET3=Entry(root,textvariable=Mobile,font=('bold',14))
    ET3.place(x=250,y=150) 
    LB4=Label(root,text="Enter DOB :-",font=('bold',18))
    LB4.place(x=10,y=200)
    ET4=Entry(root,textvariable=DOB,font=('bold',14))
    ET4.place(x=250,y=200) 
    LB5=Label(root,text="Enter Marks",font=('bold',18))
    LB5.place(x=10,y=250)
    ET5=Entry(root,textvariable=Marks,font=('bold',14))
    ET5.place(x=250,y=250) 
    
    BT1=Button(root,text="   Add   ",bg="SteelBlue1",font=('bold',18),command=insert)
    BT1.place(x=200,y=300)
    
    BT2=Button(root,text="Goto Main Menu",bg="SteelBlue1",font=('bold',10),command=gobackto_menu)
    BT2.place(x=10,y=10)
    root.mainloop()
