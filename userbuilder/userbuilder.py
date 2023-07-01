###TODO: This Program In Devolepment ! ###

from random import randint
import datetime
import mysql.connector

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


# ID - Time Create Acount - Name - Family - Age - City - Nationality - PhoneNumber   -=> in Dictionary
dic = {}
dic['ID'] = createID(8)

# This Lines of Date {
now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
# hour = str(now.hour)
# mi = str(now.minute)
# ss = str(now.second)

# dic['Date'] =  mm + "/" + dd + "/" + yyyy
# }

print("Please fill out the the below Subjects ->")
dic['Name'] = input("Enter Your Name : ") #TODO: Conecct Name And Family --> FullName ; Then Print it
dic['Family'] = input("Enter Your Family : ")
# dic['Age'] = input("Enter Your Age : ") #TODO: Print Permissible Age
# dic['City'] = input("Enter Your City : ")
# dic['Nationality'] = input("Enter Your Nationality : ")
# dic['PhoneNumber'] = int(input("Enter Your PhoneNumber : ")) #TODO: Sent Message For Number



sql = "INSERT INTO person (id,name,family) VALUES (%s, %s, %s)"
val = (dic['ID'], dic['Name'], dic['Family'])
mycursor.execute(sql, val)
conn.commit()
print(mycursor.rowcount)

print(dic)


mycursor.execute("SELECT id,name,family FROM person")
result = mycursor.fetchall()

for x in result:
    print(x)