import tkinter as ttk
import Menu_window

win=ttk.Tk()
userid=ttk.StringVar()

password=ttk.StringVar()


class Frame(object):
    def main_frame(self,root):
      win.geometry('400x400')

      TA1=ttk.Entry(win,textvariable=userid,font=('bold',14))
      TA1.place(x=150,y=150)

      TA2=ttk.Entry(win,textvariable=password,font=('bold',14),show='*')
      TA2.place(x=150,y=200)

      LB1=ttk.Label(win,text='Login Panel',font=('bold',20))
      LB1.place(x=150,y=50)
       
      LB2=ttk.Label(win,text='User ID',font=('bold',14))
      LB2.place(x=10,y=150)
      
      LB3=ttk.Label(win,text='Password',font=('bold',14))
      LB3.place(x=10,y=200)

      BT1=ttk.Button(win,text='LOGIN',command=self.Login_Check,font=('bold',14))
      BT1.place(x=150,y=300)
    def Login_Check(self):

        if userid.get()=='Admin' and password.get()=='123':
           win.destroy()
           Menu_window.view()
        else:
            LB4=ttk.Label(win,text="Wrong User Id or Password",font=('italic',10), fg = "red")
            LB4.place(x=150,y=250)
         

      
app=Frame()
app.main_frame(win)
win.mainloop()
