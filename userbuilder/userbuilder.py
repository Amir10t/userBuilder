###TODO: This Program In Devolepment ! ###
 
from random import randint
import datetime
import mysql.connector
from tkinter import *

# connect database
conn = mysql.connector.connect(host = '127.0.0.1',
                   user = 'root',
                   passwd = 'Amir10$$',
                   database = 'user')

mycursor = conn.cursor()


def createID(n): # Long of ID
    ID = ''
    for i in range(n):
        field = randint(0,3)
        if field == 0:
            ID += str((randint(0,10)))
        elif field == 1:
            ID += (chr(randint(65,90)))
        else:
            ID += (chr(randint(97,122)))
            
    return ID


def createUser():
    if first_name.get() != '' and last_name.get() != '':
        # ID - Name - Family   -=> in Dictionary
        dic = {}
        dic['ID'] = createID(6)


        dic['Name'] = str(first_name.get())
        dic['Family'] = str(last_name.get())


        sql = "INSERT INTO person (id,name,family) VALUES (%s, %s, %s)"
        val = (dic['ID'], dic['Name'], dic['Family'])
        mycursor.execute(sql, val)
        conn.commit()

        showStatus.config(text=f"Warning Copy Your ID...{dic['ID']}",fg="red")
        return dic
    else:
        showStatus.config(text=f"Please fill out!",fg="red")


def inforUser():
    id = workID.get()
    if id != '':
        mycursor.execute(f"SELECT * FROM person WHERE id = '{id}'")
        result = mycursor.fetchall()


        showStatus.config(text=result,fg='blue')
    else:
        showStatus.config(text=f"Please fill out!",fg="red")

def deleteUser():
    mycursor.execute(f"DELETE FROM person WHERE id='{workID.get()}'")
    conn.commit()

win = Tk()
win.minsize(300,250)
win.maxsize(400,350)
win.geometry("350x300")

Label(win,text ="Frist Name",font='20').pack()
first_name = Entry(win)
first_name.pack()

Label(win,text="Last Name",font='20').pack()
last_name = Entry(win)
last_name.pack()

Button(win,text="sign in",command=createUser).pack()
showStatus = Label(win,text='')
showStatus.pack()

Label(win,text="Log in with enter your ID",font='20').pack()
workID = Entry(win)
workID.pack()

Button(win,text="delete ID",command=deleteUser).pack()
Button(win,text="log in",command=inforUser).pack()

win.mainloop()