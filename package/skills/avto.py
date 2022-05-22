from package.skills.core import speak
import package.skills.greet
from main import Main
import sqlite3
import cowsay

connect = sqlite3.connect('db/baza.db')
cursor = connect.cursor()
connect2=sqlite3.connect('db/count.db')
cursor2 = connect2.cursor()
#
def Plus():
    cursor2.execute(""" CREATE TABLE IF NOT EXISTS expenses(id INTEGER) """)
    connect2.commit()
    main_list=[0]
    cursor2.execute("INSERT INTO expenses VALUES(?);",main_list)
    connect2.commit()

def DB_plus():
    cursor2.execute(""" CREATE TABLE IF NOT EXISTS expenses(id INTEGER) """)
    connect2.commit()
    
def DB_list():
    result=cursor2.execute("SELECT * FROM expenses").fetchall()
    for row in result:
        count=row[0]
    n=count+1
    main_list=[n]
    #print(n)
    cursor2.execute("INSERT INTO expenses VALUES(?);",main_list)
    connect2.commit()

def delete_db():
    cursor2.execute("DROP TABLE expenses")
    connect2.commit()
#    
def db_Plus():
    cursor.execute(""" CREATE TABLE IF NOT EXISTS expenses(name TEXT, password INTEGER) """)
    connect.commit()

def db_List():
    a=input("Введіть ім'я:")
    b=input("Введіть пароль:")
    main_list=[a, b]
    cursor.execute("INSERT INTO expenses VALUES(?,?);",main_list)
    connect.commit()
#    
def Avto():
    print('Авторизуйтесь, будь ласка')
    name=input("Введіть ім'я:")
    pas=int(input("Введіть пароль:"))
    result=cursor.execute("SELECT * FROM expenses").fetchall()
    for row in result:
        names=row[0]
        pasw=row[1]
    if name==names and pas==pasw:
        package.skills.greet.Greeting()
        print('Чим сьогодні займемся?')
        speak.Speak('Чим сьогодні займемся?')
        Main()
    else:
        cowsay.cow('Ви хто?')
        speak.Speak('Ви хто?')
        cowsay.cow ('Хоча, бувайте')
        speak.Speak('Хоча, бувайте')
    
def auto():
    result=cursor2.execute("SELECT * FROM expenses").fetchall()
    for row in result:
        count=row[0]
    connect2.commit()
    if count==20:
        delete_db()
        Plus()
        print("Ви зареєстровані? т/н")
        c = input("Введіть відповідь:")
        if c == 'т':
            Avto()
        if c == 'н':
            db_Plus()
            db_List()
    else:
        DB_plus()
        DB_list()
        package.skills.greet.Greeting()
        print('Чим сьогодні займемся?')
        speak.Speak('Чим сьогодні займемся?')
        Main()
