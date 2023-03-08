from tkinter import *
import mysql.connector

#connection
conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Furqan',
    database = 'database_python')

#Add function
def Add():
    ID = txt.get()
    em_name=txt2.get()
    depart=txt3.get()
    date=txt4.get()
    sallary=txt5.get()
    sql = 'INSERT INTO emp_tbl (id,emp_name,Depart,Dateofjoining,sallary) VALUES (%s,%s,%s,%s,%s)'
    val=(ID,em_name,depart,date,sallary)
    cur = conn.cursor()
    cur.execute(sql,val)
    conn.commit()
    txt.delete(0,END)
    txt2.delete(0,END)
    txt3.delete(0,END)
    txt4.delete(0,END)
    txt5.delete(0,END)
    txt.focus_set()

#update function
def Update():
    ID = txt.get()
    em_name = txt2.get()
    depart = txt3.get()
    date = txt4.get()
    sallary = txt5.get()
    sql = "Update  emp_tbl set emp_name= %s,Depart= %s,Dateofjoining= %s, sallary= %s where id= %s"
    val=(em_name,depart,date,sallary,ID)
    cur = conn.cursor()
    cur.execute(sql,val)
    conn.commit()

#read function
def Readf():
    cur = conn.cursor()
    cur.execute("select * from emp_tbl")
    data = cur.fetchall()
    print(data[0])
    conn.commit()

#delete function
def Delete():
    ID=txt.get()
    sql = "delete from emp_tbl where id = %s"
    val = (ID,)
    cur = conn.cursor()
    cur.execute(sql, val)
    conn.commit()
    lastid = cur.lastrowid
    txt.delete(0, END)
    txt2.delete(0, END)
    txt3.delete(0, END)
    txt4.delete(0, END)
    txt.focus_set()


#GUI creation
win = Tk()
win.geometry ('800x700')
win.title('Employee Database management system')
lbl=Label(text_='Enter ID of Employee', foreground='blue', font=('Arial', 18))
lbl.place(x=10,y=10)
txt = Entry (font = ('Arial',20),foreground = 'black',background = 'skyblue',)
txt.place (x=350,y=12)
lbl=Label(text_='Enter Name of Employee', foreground='blue', font=('Arial', 18))
lbl.place(x=10,y=70)
txt2 = Entry (font = ('Arial',20),foreground = 'black',background = 'skyblue',)
txt2.place (x=350,y=70)
lbl=Label(text_='Enter Depart of Employee', foreground='blue', font=('Arial', 18))
lbl.place(x=10,y=130)
txt3 = Entry (font = ('Arial',20),foreground = 'black',background = 'skyblue',)
txt3.place (x=350,y=130)
lbl=Label(text_='Enter Date of Joining', foreground='blue', font=('Arial', 18))
lbl.place(x=10,y=190)
txt4 = Entry (font = ('Arial',20),foreground = 'black',background = 'skyblue',)
txt4.place (x=350,y=190)
lbl=Label(text_='Enter a Sallary', foreground='blue', font=('Arial', 18))
lbl.place(x=10,y=250)
txt5 = Entry (font = ('Arial',20),foreground = 'black',background = 'skyblue',)
txt5.place (x=350,y=250)


#buttns
btn = Button(text='Create',background='skyblue',width=(20),height=(3),borderwidth=(1),command = Add)
btn.place(x=10, y=300)
btn = Button(text='Read',background='skyblue',width=(20),height=(3),borderwidth=(1),command=Readf)
btn.place(x=200, y=300)
btn = Button(text='Update',background='skyblue',width=(20),height=(3),command=Update,borderwidth=(1))
btn.place(x=390, y=300)
btn = Button(text='Delete',background='skyblue',width=(20),height=(3),command=Delete,borderwidth=(1))
btn.place(x=580, y=300)




win.mainloop()
