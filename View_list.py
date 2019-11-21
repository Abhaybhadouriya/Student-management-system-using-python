import tkinter as tk
from tkinter import ttk
import pymysql
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Menu_window


""""""""""""""""""""" DATABASE CONNECTION  """""""""""""""""

conn=pymysql.connect(host="localhost",user="root",password="qwerty",db="test")
aa=conn.cursor()


    
def logout():
    def Go_backto_Menu():
           win.destroy()
           Menu_window.view()
    win=tk.Tk()
    win.geometry('1000x500')
    win.title("Student List")
    LB1=tk.Label(win,text='Student Record List',font=('bold',18))
    LB1.place(x=500,y=50)

    
    BT1=tk.Button(win,bg="SteelBlue1",text='Goto Menu',command=Go_backto_Menu,font=('bold',16))
    BT1.place(x=10,y=10)

#################### TREEVIEW DEFINE #######################

    cols=('ID','Name', 'Mobile no','DOB','Marks')

    tv=ttk.Treeview(win,columns=cols, show='headings')
    tv.place(x=100,y=100)
    for col in cols:
        tv.heading(col, text=col)   
    xx=[]
    tv.delete(*tv.get_children())
    query="select * from pythonentry"
    aa.execute(query)
    res=aa.fetchall()

    for r in res:       
       tv.insert('','end',values=(r))
       xx.append(int(r[4]))

######################  PLOT    ############################
    a=plt.figure(1)
    ax=a.add_subplot(1,1,1)
    xx=np.linspace(1,550,55)
    yy=np.linspace(1,500,50)
    plt.hist(xx,yy,histtype='bar',rwidth=0.8)
    canvas=FigureCanvasTkAgg(a,master=win)
    plot_widget=canvas.get_tk_widget()
    plot_widget.place(x=100,y=350,height=350,width=1000)

    for s in xx:
       print(s)
    print(yy)
    win.mainloop()


#def viewlist():
logout()


