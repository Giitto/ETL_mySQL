#!/usr/bin/env python
import mysql.connector 

def main():
    db = mysql.connector.connect(host='localhost',port=3308,  user='root', password='root', db='idqms')
    #cursor.execute("""SET SESSION wait_timeout=80;""")
    mycursor = db.cursor() 
    mycursor.execute("DROP TABLE IF EXISTS matable")
    mycursor.execute("CREATE TABLE matable (NAME VARCHAR(10))")
    print('#######Heloooo#####')
    db.close()
main()








