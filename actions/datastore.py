import mysql.connector
import datetime as dt 

def DataUpdate(size,type,text):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="slots_store",auth_plugin='mysql_native_password'
    )
    if(type=='tweets' or type=='tweet' or type=='twitter'):
        type="Twitter"
    if(type=='videos' or type=='video' or type=='youtube'):
        type="Youtube"
    mycursor = mydb.cursor()
    sql =  'INSERT INTO slot_values(size,type,text,time) values("{0}","{1}","{2}","{3}");'.format(size,type,text,dt.datetime.now())
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount," row inserted.")
    mydb.close()
    mycursor.close()

def SearchHistory():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="slots_store",auth_plugin='mysql_native_password'
    )
    mycursor = mydb.cursor(buffered=True)
    sql =  'Select * from slot_values'
    mycursor.execute(sql)
    mydb.commit()
    records = mycursor.fetchall()
    print("Total number of rows in table: ", mycursor.rowcount)
    s="No.\t Type \t \t Text \t\t Size \t\t Time\n"
    c=1
    print("\nPrinting each row")
    if(len(records)!=0):
        for row in records:
            s+="{0}\t| {1}\t|\t {2}\t| {3}\t| {4}|\n".format(c,row[0],row[1],row[2],row[3])
            c+=1
        print(mycursor.rowcount," rows present.")
    else:
        s='Search History is empty'
    mydb.close()
    mycursor.close()
    return s

def DeleteHistory():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="slots_store",auth_plugin='mysql_native_password'
    )
    mycursor = mydb.cursor(buffered=True)
    sql =  'DELETE FROM slot_values'
    mycursor.execute(sql)
    mydb.commit()
    mydb.close()
    mycursor.close()
    s="Deleted Search History"
    return s