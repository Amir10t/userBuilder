import mysql.connector

# connect database
conn = mysql.connector.connect(host = '127.0.0.1',
                   user = 'root',
                   passwd = '',
                   database = 'user')

# print(conn)

# Space
mycursor = conn.cursor()

# create database
# mycursor.execute("CREATE DATABASE user")

# create table
# mycursor.execute("CREATE TABLE person(id VARCHAR(255),name VARCHAR(255),family VARCHAR(255))")

