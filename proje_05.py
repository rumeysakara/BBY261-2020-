from tkinter import *
from datetime import datetime
import sqlite3

root=Tk()
root.geometry('600x320')
root.title("DataBase using Sqlite3 and Tkinter")
root.configure(background="powder blue")

yonetmen=StringVar()
film=StringVar()
tip=StringVar()
puan=IntVar()
menu=Menu(root)
root.config(menu=menu)

menu = Menu(root)
root.config(menu=menu)

def helpp():
   help(sqlite3)

subm = Menu(menu)
menu.add_cascade(label="Help",menu=subm)
subm.add_command(label="Sqlite3 Docs",command=helpp)


conn = sqlite3.connect('Movies.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS Movies (
            Director text,
            Name text PRIMARY KEY,
            Type text,
            Rating integer,
            RecordDate text
            )""")
conn.commit()
satir3 = Listbox(root, width=90, height=9)
satir3.pack(pady="10", side=BOTTOM)

def film_listele():
    satir3.delete(0, END)
    for kayitlar in c.execute('SELECT rowid,* FROM Movies'):
        satir3.insert(END, kayitlar)
film_listele()

lab=Label(root,text='Yönetmen:',font=('none 13 bold'))
lab.place(x=0,y=0)
entyonetmen=Entry(root,width=20,font=('none 13 bold'),textvar=yonetmen)
entyonetmen.place(x=95,y=0)

lab1=Label(root,text='Film:',font=('none 13 bold'))
lab1.place(x=0,y=40)
entfilm=Entry(root,width=20,font=('none 13 bold'),textvar=film)
entfilm.place(x=95,y=40)

lab2=Label(root,text='Tür:',font=('none 13 bold'))
lab2.place(x=0,y=80)
enttip=Entry(root,width=20,font=('none 13 bold'),textvar=tip)
enttip.place(x=95,y=80)

lab2=Label(root,text='Puan:',font=('none 13 bold'))
lab2.place(x=0,y=120)
entpuan=Entry(root,width=20,font=('none 13 bold'),textvar=puan)
entpuan.place(x=95,y=120)

def insert_Movie():
    director = yonetmen.get()
    filmName =  film.get()
    type = tip.get()
    rating = puan.get()
    with conn:
        c.execute("INSERT OR REPLACE INTO Movies VALUES (:Director, :Name, :Type, :Rating, :RecordDate)",
                  {'Director': director, 'Name': filmName, 'Type': type, 'Rating': rating, 'RecordDate': datetime.today().strftime("%d/%m/%Y %H:%M:%S")})
        film_listele()
    yonetmen.set("")
    film.set("")
    tip.set("")
    puan.set("")

def get_Movies_by_name():
    satir3.delete(0, END)
    c.execute("SELECT rowid,* FROM Movies WHERE Name=:Name", {'Name': film.get()})
    for kayitlar in c.fetchall():
        satir3.insert(END, kayitlar)
    yonetmen.set("")
    film.set("")
    tip.set("")
    puan.set("")

butbul=Button(root,padx=2,pady=2,text='Film İsmi Ara',command=get_Movies_by_name,font=('none 13 bold'))
butbul.place(x=400,y=0)

def update_imdbRating(mov, rating):
    with conn:
        c.execute("""UPDATE Movies SET Rating = :rating
                    WHERE Name = :name""",
                  {'name': mov.Name, 'rating': mov.Rating})
        conn.commit()

butinsert=Button(root,padx=2,pady=2,text='Ekle/Güncelle',command=insert_Movie,font=('none 13 bold'))
butinsert.place(x=400,y=40)
from tkinter import *
from datetime import datetime
import sqlite3

root=Tk()
root.geometry('600x320')
root.title("DataBase using Sqlite3 and Tkinter")
root.configure(background="powder blue")

yonetmen=StringVar()
film=StringVar()
tip=StringVar()
puan=IntVar()
menu=Menu(root)
root.config(menu=menu)

menu = Menu(root)
root.config(menu=menu)

def helpp():
   help(sqlite3)

subm = Menu(menu)
menu.add_cascade(label="Help",menu=subm)
subm.add_command(label="Sqlite3 Docs",command=helpp)


conn = sqlite3.connect('Movies.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS Movies (
            Director text,
            Name text PRIMARY KEY,
            Type text,
            Rating integer,
            RecordDate text
            )""")
conn.commit()
satir3 = Listbox(root, width=90, height=9)
satir3.pack(pady="10", side=BOTTOM)

def film_listele():
    satir3.delete(0, END)
    for kayitlar in c.execute('SELECT rowid,* FROM Movies'):
        satir3.insert(END, kayitlar)
film_listele()

lab=Label(root,text='Yönetmen:',font=('none 13 bold'))
lab.place(x=0,y=0)
entyonetmen=Entry(root,width=20,font=('none 13 bold'),textvar=yonetmen)
entyonetmen.place(x=95,y=0)

lab1=Label(root,text='Film:',font=('none 13 bold'))
lab1.place(x=0,y=40)
entfilm=Entry(root,width=20,font=('none 13 bold'),textvar=film)
entfilm.place(x=95,y=40)

lab2=Label(root,text='Tür:',font=('none 13 bold'))
lab2.place(x=0,y=80)
enttip=Entry(root,width=20,font=('none 13 bold'),textvar=tip)
enttip.place(x=95,y=80)

lab2=Label(root,text='Puan:',font=('none 13 bold'))
lab2.place(x=0,y=120)
entpuan=Entry(root,width=20,font=('none 13 bold'),textvar=puan)
entpuan.place(x=95,y=120)

def insert_Movie():
    director = yonetmen.get()
    filmName =  film.get()
    type = tip.get()
    rating = puan.get()
    with conn:
        c.execute("INSERT OR REPLACE INTO Movies VALUES (:Director, :Name, :Type, :Rating, :RecordDate)",
                  {'Director': director, 'Name': filmName, 'Type': type, 'Rating': rating, 'RecordDate': datetime.today().strftime("%d/%m/%Y %H:%M:%S")})
        film_listele()
    yonetmen.set("")
    film.set("")
    tip.set("")
    puan.set("")

def get_Movies_by_name():
    satir3.delete(0, END)
    c.execute("SELECT rowid,* FROM Movies WHERE Name=:Name", {'Name': film.get()})
    for kayitlar in c.fetchall():
        satir3.insert(END, kayitlar)
    yonetmen.set("")
    film.set("")
    tip.set("")
    puan.set("")

butbul=Button(root,padx=2,pady=2,text='Film İsmi Ara',command=get_Movies_by_name,font=('none 13 bold'))
butbul.place(x=400,y=0)

def update_imdbRating(mov, rating):
    with conn:
        c.execute("""UPDATE Movies SET Rating = :rating
                    WHERE Name = :name""",
                  {'name': mov.Name, 'rating': mov.Rating})
        conn.commit()

butinsert=Button(root,padx=2,pady=2,text='Ekle/Güncelle',command=insert_Movie,font=('none 13 bold'))
butinsert.place(x=400,y=40)


def remove_Movie():
    with conn:
        c.execute("DELETE from Movies WHERE Name = :name",
                  {'name': film.get()})
        conn.commit()
        yonetmen.set("")
        film.set("")
        tip.set("")
        puan.set("")
        film_listele()

butdel=Button(root,padx=2,pady=2,text='Filmi İsmi ile Sil',command=remove_Movie,font=('none 13 bold'))
butdel.place(x=400,y=80)

def drop():
   c.execute("DROP table Movies")
   conn.commit()

root.mainloop()


conn.close()
from tkinter import *
from datetime import datetime
import sqlite3

root=Tk()
root.geometry('600x320')
root.title("DataBase using Sqlite3 and Tkinter")
root.configure(background="powder blue")

yonetmen=StringVar()
film=StringVar()
tip=StringVar()
puan=IntVar()
menu=Menu(root)
root.config(menu=menu)

menu = Menu(root)
root.config(menu=menu)

def helpp():
   help(sqlite3)

subm = Menu(menu)
menu.add_cascade(label="Help",menu=subm)
subm.add_command(label="Sqlite3 Docs",command=helpp)


conn = sqlite3.connect('Movies.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS Movies (
            Director text,
            Name text PRIMARY KEY,
            Type text,
            Rating integer,
            RecordDate text
            )""")
conn.commit()
satir3 = Listbox(root, width=90, height=9)
satir3.pack(pady="10", side=BOTTOM)

def film_listele():
    satir3.delete(0, END)
    for kayitlar in c.execute('SELECT rowid,* FROM Movies'):
        satir3.insert(END, kayitlar)
film_listele()

lab=Label(root,text='Yönetmen:',font=('none 13 bold'))
lab.place(x=0,y=0)
entyonetmen=Entry(root,width=20,font=('none 13 bold'),textvar=yonetmen)
entyonetmen.place(x=95,y=0)

lab1=Label(root,text='Film:',font=('none 13 bold'))
lab1.place(x=0,y=40)
entfilm=Entry(root,width=20,font=('none 13 bold'),textvar=film)
entfilm.place(x=95,y=40)

lab2=Label(root,text='Tür:',font=('none 13 bold'))
lab2.place(x=0,y=80)
enttip=Entry(root,width=20,font=('none 13 bold'),textvar=tip)
enttip.place(x=95,y=80)

lab2=Label(root,text='Puan:',font=('none 13 bold'))
lab2.place(x=0,y=120)
entpuan=Entry(root,width=20,font=('none 13 bold'),textvar=puan)
entpuan.place(x=95,y=120)

def insert_Movie():
    director = yonetmen.get()
    filmName =  film.get()
    type = tip.get()
    rating = puan.get()
    with conn:
        c.execute("INSERT OR REPLACE INTO Movies VALUES (:Director, :Name, :Type, :Rating, :RecordDate)",
                  {'Director': director, 'Name': filmName, 'Type': type, 'Rating': rating, 'RecordDate': datetime.today().strftime("%d/%m/%Y %H:%M:%S")})
        film_listele()
    yonetmen.set("")
    film.set("")
    tip.set("")
    puan.set("")

def get_Movies_by_name():
    satir3.delete(0, END)
    c.execute("SELECT rowid,* FROM Movies WHERE Name=:Name", {'Name': film.get()})
    for kayitlar in c.fetchall():
        satir3.insert(END, kayitlar)
    yonetmen.set("")
    film.set("")
    tip.set("")
    puan.set("")

butbul=Button(root,padx=2,pady=2,text='Film İsmi Ara',command=get_Movies_by_name,font=('none 13 bold'))
butbul.place(x=400,y=0)

def update_imdbRating(mov, rating):
    with conn:
        c.execute("""UPDATE Movies SET Rating = :rating
                    WHERE Name = :name""",
                  {'name': mov.Name, 'rating': mov.Rating})
        conn.commit()

butinsert=Button(root,padx=2,pady=2,text='Ekle/Güncelle',command=insert_Movie,font=('none 13 bold'))
butinsert.place(x=400,y=40)


def remove_Movie():
    with conn:
        c.execute("DELETE from Movies WHERE Name = :name",
                  {'name': film.get()})
        conn.commit()
        yonetmen.set("")
        film.set("")
        tip.set("")
        puan.set("")
        film_listele()

butdel=Button(root,padx=2,pady=2,text='Filmi İsmi ile Sil',command=remove_Movie,font=('none 13 bold'))
butdel.place(x=400,y=80)

def drop():
   c.execute("DROP table Movies")
   conn.commit()

root.mainloop()


conn.close()
from tkinter import *
from datetime import datetime
import sqlite3

root=Tk()
root.geometry('600x320')
root.title("DataBase using Sqlite3 and Tkinter")
root.configure(background="powder blue")

yonetmen=StringVar()
film=StringVar()
tip=StringVar()
puan=IntVar()
menu=Menu(root)
root.config(menu=menu)

menu = Menu(root)
root.config(menu=menu)

def helpp():
   help(sqlite3)

subm = Menu(menu)
menu.add_cascade(label="Help",menu=subm)
subm.add_command(label="Sqlite3 Docs",command=helpp)


conn = sqlite3.connect('Movies.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS Movies (
            Director text,
            Name text PRIMARY KEY,
            Type text,
            Rating integer,
            RecordDate text
            )""")
conn.commit()
satir3 = Listbox(root, width=90, height=9)
satir3.pack(pady="10", side=BOTTOM)

def film_listele():
    satir3.delete(0, END)
    for kayitlar in c.execute('SELECT rowid,* FROM Movies'):
        satir3.insert(END, kayitlar)
film_listele()

lab=Label(root,text='Yönetmen:',font=('none 13 bold'))
lab.place(x=0,y=0)
entyonetmen=Entry(root,width=20,font=('none 13 bold'),textvar=yonetmen)
entyonetmen.place(x=95,y=0)

lab1=Label(root,text='Film:',font=('none 13 bold'))
lab1.place(x=0,y=40)
entfilm=Entry(root,width=20,font=('none 13 bold'),textvar=film)
entfilm.place(x=95,y=40)

lab2=Label(root,text='Tür:',font=('none 13 bold'))
lab2.place(x=0,y=80)
enttip=Entry(root,width=20,font=('none 13 bold'),textvar=tip)
enttip.place(x=95,y=80)

lab2=Label(root,text='Puan:',font=('none 13 bold'))
lab2.place(x=0,y=120)
entpuan=Entry(root,width=20,font=('none 13 bold'),textvar=puan)
entpuan.place(x=95,y=120)

def insert_Movie():
    director = yonetmen.get()
    filmName =  film.get()
    type = tip.get()
    rating = puan.get()
    with conn:
        c.execute("INSERT OR REPLACE INTO Movies VALUES (:Director, :Name, :Type, :Rating, :RecordDate)",
                  {'Director': director, 'Name': filmName, 'Type': type, 'Rating': rating, 'RecordDate': datetime.today().strftime("%d/%m/%Y %H:%M:%S")})
        film_listele()
    yonetmen.set("")
    film.set("")
    tip.set("")
    puan.set("")

def get_Movies_by_name():
    satir3.delete(0, END)
    c.execute("SELECT rowid,* FROM Movies WHERE Name=:Name", {'Name': film.get()})
    for kayitlar in c.fetchall():
        satir3.insert(END, kayitlar)
    yonetmen.set("")
    film.set("")
    tip.set("")
    puan.set("")

butbul=Button(root,padx=2,pady=2,text='Film İsmi Ara',command=get_Movies_by_name,font=('none 13 bold'))
butbul.place(x=400,y=0)

def update_imdbRating(mov, rating):
    with conn:
        c.execute("""UPDATE Movies SET Rating = :rating
                    WHERE Name = :name""",
                  {'name': mov.Name, 'rating': mov.Rating})
        conn.commit()

butinsert=Button(root,padx=2,pady=2,text='Ekle/Güncelle',command=insert_Movie,font=('none 13 bold'))
butinsert.place(x=400,y=40)


def remove_Movie():
    with conn:
        c.execute("DELETE from Movies WHERE Name = :name",
                  {'name': film.get()})
        conn.commit()
        yonetmen.set("")
        film.set("")
        tip.set("")
        puan.set("")
        film_listele()

butdel=Button(root,padx=2,pady=2,text='Filmi İsmi ile Sil',command=remove_Movie,font=('none 13 bold'))
butdel.place(x=400,y=80)

def drop():
   c.execute("DROP table Movies")
   conn.commit()

root.mainloop()


conn.close()
from tkinter import *
from datetime import datetime
import sqlite3

root=Tk()
root.geometry('600x320')
root.title("DataBase using Sqlite3 and Tkinter")
root.configure(background="powder blue")

yonetmen=StringVar()
film=StringVar()
tip=StringVar()
puan=IntVar()
menu=Menu(root)
root.config(menu=menu)

menu = Menu(root)
root.config(menu=menu)

def helpp():
   help(sqlite3)

subm = Menu(menu)
menu.add_cascade(label="Help",menu=subm)
subm.add_command(label="Sqlite3 Docs",command=helpp)


conn = sqlite3.connect('Movies.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS Movies (
            Director text,
            Name text PRIMARY KEY,
            Type text,
            Rating integer,
            RecordDate text
            )""")
conn.commit()
satir3 = Listbox(root, width=90, height=9)
satir3.pack(pady="10", side=BOTTOM)

def film_listele():
    satir3.delete(0, END)
    for kayitlar in c.execute('SELECT rowid,* FROM Movies'):
        satir3.insert(END, kayitlar)
film_listele()

lab=Label(root,text='Yönetmen:',font=('none 13 bold'))
lab.place(x=0,y=0)
entyonetmen=Entry(root,width=20,font=('none 13 bold'),textvar=yonetmen)
entyonetmen.place(x=95,y=0)

lab1=Label(root,text='Film:',font=('none 13 bold'))
lab1.place(x=0,y=40)
entfilm=Entry(root,width=20,font=('none 13 bold'),textvar=film)
entfilm.place(x=95,y=40)

lab2=Label(root,text='Tür:',font=('none 13 bold'))
lab2.place(x=0,y=80)
enttip=Entry(root,width=20,font=('none 13 bold'),textvar=tip)
enttip.place(x=95,y=80)

lab2=Label(root,text='Puan:',font=('none 13 bold'))
lab2.place(x=0,y=120)
entpuan=Entry(root,width=20,font=('none 13 bold'),textvar=puan)
entpuan.place(x=95,y=120)

def insert_Movie():
    director = yonetmen.get()
    filmName =  film.get()
    type = tip.get()
    rating = puan.get()
    with conn:
        c.execute("INSERT OR REPLACE INTO Movies VALUES (:Director, :Name, :Type, :Rating, :RecordDate)",
                  {'Director': director, 'Name': filmName, 'Type': type, 'Rating': rating, 'RecordDate': datetime.today().strftime("%d/%m/%Y %H:%M:%S")})
        film_listele()
    yonetmen.set("")
    film.set("")
    tip.set("")
    puan.set("")

def get_Movies_by_name():
    satir3.delete(0, END)
    c.execute("SELECT rowid,* FROM Movies WHERE Name=:Name", {'Name': film.get()})
    for kayitlar in c.fetchall():
        satir3.insert(END, kayitlar)
    yonetmen.set("")
    film.set("")
    tip.set("")
    puan.set("")

butbul=Button(root,padx=2,pady=2,text='Film İsmi Ara',command=get_Movies_by_name,font=('none 13 bold'))
butbul.place(x=400,y=0)

def update_imdbRating(mov, rating):
    with conn:
        c.execute("""UPDATE Movies SET Rating = :rating
                    WHERE Name = :name""",
                  {'name': mov.Name, 'rating': mov.Rating})
        conn.commit()

butinsert=Button(root,padx=2,pady=2,text='Ekle/Güncelle',command=insert_Movie,font=('none 13 bold'))
butinsert.place(x=400,y=40)


def remove_Movie():
    with conn:
        c.execute("DELETE from Movies WHERE Name = :name",
                  {'name': film.get()})
        conn.commit()
        yonetmen.set("")
        film.set("")
        tip.set("")
        puan.set("")
        film_listele()

butdel=Button(root,padx=2,pady=2,text='Filmi İsmi ile Sil',command=remove_Movie,font=('none 13 bold'))
butdel.place(x=400,y=80)

def drop():
   c.execute("DROP table Movies")
   conn.commit()

root.mainloop()


conn.close()

def remove_Movie():
    with conn:
        c.execute("DELETE from Movies WHERE Name = :name",
                  {'name': film.get()})
        conn.commit()
        yonetmen.set("")
        film.set("")
        tip.set("")
        puan.set("")
        film_listele()

butdel=Button(root,padx=2,pady=2,text='Filmi İsmi ile Sil',command=remove_Movie,font=('none 13 bold'))
butdel.place(x=400,y=80)

def drop():
   c.execute("DROP table Movies")
   conn.commit()

root.mainloop()


conn.close()
