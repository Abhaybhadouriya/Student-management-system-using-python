from tkinter import *
import View_list
import Add_New_Records
import Update_del
def main():
    def view_list():
            menu.destroy()
            View_list.viewlist()

    def add_new():
        menu.destroy()
        Add_New_Records.addnew()
   
    def update_del():
        menu.destroy()
        Update_del.addnew()

    menu=Tk()
    menu.geometry('900x500')

    menu.title("Admin Panel DashBoard")
   
    LB1=Label(menu,text="Admin Panel",font=('bold',24))
    LB1.place(x=400,y=100)

    LB2=Label(menu,text="Student Record Management System",font=('bold',18))
    LB2.place(x=300,y=200)

    BT1=Button(menu,bg="SteelBlue1",text='View Student List',command=view_list,font=('bold',16))
    BT1.place(x=350,y=300)



    menubar=Menu(menu)
    filemenu=Menu(menubar,tearoff=0)
    filemenu.add_command(label="Add New Record",command=add_new)
    filemenu.add_separator()
    filemenu.add_command(label="Update",command=update_del)
    filemenu.add_command(label="Delete",command=update_del)
    filemenu.add_separator()
    filemenu.add_command(label="Search by Id",command=update_del)
    menubar.add_cascade(label="Basic Operations",menu=filemenu)
    menu.config(menu=menubar)

    menu.mainloop()


           
def view():
     main()
    


