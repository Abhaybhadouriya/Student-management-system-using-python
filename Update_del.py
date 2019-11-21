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
    def update():
          
          name=Name.get()
          mobile=Mobile.get()
          dob=DOB.get()
          marks=Marks.get()
          uid=ID.get()
          query="update pythonentry set name='"+name+"',mobile='"+mobile+"',dob='"+dob+"', marks='"+marks+"' where id='"+uid+"'"
          aa.execute(query)
          conn.commit()
          messagebox.showinfo("Success","Record Updated")

    def delete():
            uid=ID.get()
            query="delete from pythonentry where id='"+uid+"'"
            aa.execute(query)
            conn.commit()
            ET6.delete(0,END)
            ET2.delete(0,END)
            ET3.delete(0,END)
            ET4.delete(0,END)
            ET5.delete(0,END)
            messagebox.showinfo("Success","Record Deleted")

    def find():
    
        ET2.delete(0,END)
        ET3.delete(0,END)
        ET4.delete(0,END)
        ET5.delete(0,END)
        uid=ID.get()
        query="select * from pythonentry where id='"+uid+"'"
        aa.execute(query)
        res=aa.fetchall()
        for a in res:
            ET2.insert(0,a[1])
            ET3.insert(0,a[2])
            ET4.insert(0,a[3])
            ET5.insert(0,a[4])

  
        
    root=Tk()
    ID=StringVar()
    Marks=StringVar()
    Name=StringVar()
    DOB=StringVar()
    Mobile=StringVar()
    
    root.geometry('500x400')
    root.title('Add New Records')

    LB1=Label(root,text="Add New Records",font=('bold',18))
    LB1.place(x=200,y=50)

    LB6=Label(root,text="Enter USER ID :-",font=('bold',18))
    LB6.place(x=10,y=100)
    ET6=Entry(root,textvariable=ID,font=('bold',14))
    ET6.place(x=250,y=100)  
    
    LB2=Label(root,text="Name :-",font=('bold',18))
    LB2.place(x=10,y=150)
    ET2=Entry(root,textvariable=Name,font=('bold',14))
    ET2.place(x=250,y=150)  
    LB3=Label(root,text="Mobile no :-",font=('bold',18))
    LB3.place(x=10,y=200)
    ET3=Entry(root,textvariable=Mobile,font=('bold',14))
    ET3.place(x=250,y=200) 
    LB4=Label(root,text="DOB :-",font=('bold',18))
    LB4.place(x=10,y=250)
    ET4=Entry(root,textvariable=DOB,font=('bold',14))
    ET4.place(x=250,y=250) 
    LB5=Label(root,text="Marks :-",font=('bold',18))
    LB5.place(x=10,y=300)
    ET5=Entry(root,textvariable=Marks,font=('bold',14))
    ET5.place(x=250,y=300) 
    
    BT1=Button(root,text="   Find  ",bg="SteelBlue1",font=('bold',18),command=find)
    BT1.place(x=50,y=350)


    BT3=Button(root,text="   Delete   ",bg="SteelBlue1",font=('bold',18),command=delete)
    BT3.place(x=155,y=350)

    BT4=Button(root,text="   Update  ",bg="SteelBlue1",font=('bold',18),command=update)
    BT4.place(x=300,y=350)
    
    BT2=Button(root,text="Goto Main Menu",bg="SteelBlue1",font=('bold',10),command=gobackto_menu)
    BT2.place(x=10,y=10)
    root.mainloop()

