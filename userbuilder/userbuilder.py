###TODO: This Program In Devolepment ! ###

from random import randint
import datetime
import mysql.connector

# connect database
conn = mysql.connector.connect(host = '127.0.0.1',
                   user = 'root',
                   passwd = '',
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
    # ID - Name - Family   -=> in Dictionary
    dic = {}
    dic['ID'] = createID(6)
    
    print("Please fill out the the below Subjects ->")
    dic['Name'] = input("Enter Your Name : ") #TODO: Conecct Name And Family --> FullName ; Then Print it
    dic['Family'] = input("Enter Your Family : ")



    sql = "INSERT INTO person (id,name,family) VALUES (%s, %s, %s)"
    val = (dic['ID'], dic['Name'], dic['Family'])
    mycursor.execute(sql, val)
    conn.commit()
    # print(mycursor.rowcount)

    return dic

# createUser()

def inforUser(id:str):
    mycursor.execute(f"SELECT * FROM person WHERE id = '{id}'")
    result = mycursor.fetchall()

    for x in result:
        print(x)
        
inforUser('Y2pWwh')
