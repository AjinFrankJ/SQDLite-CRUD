from tkinter import *
from tkinter import messagebox as Msg


import sqlite3
from sqlite3 import Error

db = sqlite3.connect('Test.db')

Window = Tk()

Window.title("SQLite CRUD")

# SupWdwVar.geometry("800x800")

Window.minsize(400, 300)

HeadLbl= Label(Window,
      text="SQLite CRUD Operations  ",
      font="Cambria 16 bold",
      fg="black",
      anchor=E, height=1).grid(row=0, column=0,columnspan=2)

NameLbl= Label(Window,
      text="Name: ",
      font="Cambria 16 bold",
      fg="black", height=1).grid(row=1, column=0)


Nament = Entry(Window,
             font="Times",
             bg="white", fg="grey")
Nament.insert(0,"Enter name here")

Nament.grid(row=1, column=1)

EmailLbl= Label(Window,
      text="Email:",
      font="Cambria 16 bold",
      fg="black", height=1).grid(row=2, column=0)


Emailent = Entry(Window,
             font="Times",
             bg="white", fg="grey")
Emailent.insert(0,"Ex: ajin@yahoo.com")

Emailent.grid(row=2, column=1)

MobLbl= Label(Window,
      text="Mobile Number: ",
      font="Cambria 16 bold",
      fg="black" ).grid(row=3, column=0)

Mobent = Entry(Window,fg="grey", font="Times")
Mobent.insert(0,"Ex:1234567890")
Mobent.grid(row=3, column=1,sticky=W)



PassLbl= Label(Window,
      text="Password: ",
      font="Cambria 16 bold",
      fg="black" ).grid(row=4, column=0)

Passent = Entry(Window,fg="grey", font="Times")
Passent.insert(0,"")
Passent.grid(row=4, column=1,sticky=W)

def create_table():
      Namsdb = sqlite3.connect('Test.db')

      try:
            Curvar = Namsdb.cursor()
            Curvar.execute('''CREATE TABLE STUDENT(
      					NamCol TEXT (30) NOT NULL,
      					MylCol TEXT (30) NOT NULL,
      					MblCol INTEGER,
      					PwdCol TEXT (30) NOT NULL); ''')
            print("Table created successfully")
            Msg.showinfo("Success","Table created succesfully")

      except Error as ErrVar:
            print("Error in operation", ErrVar)
            Namsdb.rollback()

      Namsdb.close()

def insert_records():
      Namsdb = sqlite3.connect('Test.db')


      try:
            Curvar = Namsdb.cursor()

            Curvar.execute('''INSERT INTO STUDENT (Nament, Mailent, Mobent, Passent)''')
            Namsdb.commit()
            print("Table created successfully")

      except Error as ErrVar:
            print("Error in operation", ErrVar)
            Namsdb.rollback()

      Namsdb.close()

def get_records():
      db = sqlite3.connect('Test.db')

      try:
            Curvar = db.cursor()
            Curvar.execute('''SELECT * FROM STUDENT''')
            while True:
                  record = Curvar.fetchone()
                  if record == None:
                        print("Print record none")
                        break
                  Msg.showinfo("User Record",record)
                  print(record)
      except Error as ErrVar:
            print("Error in operation", ErrVar)
            Msg.showinfo("User Record",ErrVar)
            db.rollback()

      db.close()

def update_records():
      Namsdb = sqlite3.connect('Test.db')
      regname = "Ajin"

      oldpass = "Test1234"
      regpass = "Ajnn1234"

      update = '''UPDATE STUDENT set PwdCol=? WHERE NameCol=? and PwdCol=?;'''

      try:
            Curvar = Namsdb.cursor()
            Curvar.execute(update, (regpass, regname, oldpass))
            Namsdb.commit()
            print("Record updated successfully")

      except Error as ErrVar:
            print("Error in operation", ErrVar)
            Namsdb.rollback()

      Namsdb.close()

Button(Window, text="Create Table",
    bg="white", fg="black", command=create_table,
    font="Times").grid(row=5, columnspan=2)

Button(Window, text="Insert Record",
    bg="white", fg="black", command=insert_records,
    font="Times").grid(row=6, columnspan=2)

Button(Window, text="Get Records",
    bg="white", fg="black", command=get_records,
    font="Times").grid(row=7, columnspan=2)

Button(Window, text="Update records",
    bg="white", fg="black", command=update_records,
    font="Times").grid(row=8, columnspan=2)

##Button(Window, text="Submit",
  ##  bg="white", fg="black",
 ##   width=10, command=,
  ###  font="arial 40 bold").grid(row=16, columnspan=2)


Window.mainloop()