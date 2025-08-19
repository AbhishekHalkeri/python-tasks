import psycopg2 as pc
def createtable():
    conn=pc.connect(dbname='school',user='postgres',password='Abhi@2003shek',host='localhost',port=5432)
    cursor=conn.cursor()
    cursor.execute('''create table class10(Name text,SID int,marks int);''')
    print("Table created successfully!")
    conn.commit()
    conn.close()
def insert():
    conn=pc.connect(dbname='school',user='postgres',password='Abhi@2003shek',host='localhost',port=5432)
    cursor=conn.cursor()
    cursor.execute('''insert into class10(Name,SID,marks) values ('abhay',04,89);''')
    print("record has been inserted.")
    conn.commit()
    conn.close()
def dyn_insert():
    conn=pc.connect(dbname='school',user='postgres',password='Abhi@2003shek',host='localhost',port=5432)
    cursor=conn.cursor()
    name=input("Enter Name: ")
    sid=int(input('Enter Roll No: '))
    marks=int(input("Enter Marks: "))
    query='''insert into class8(Name,SID,marks) values (%s,%s,%s);'''
    cursor.execute(query,(name,sid,marks))
    print("record added successfully!")
    conn.commit()
    conn.close()
def extractOneRecord():
    conn=pc.connect(dbname='school',user='postgres',password='Abhi@2003shek',host='localhost',port=5432)
    cursor=conn.cursor()
    cursor.execute('''select * from class10''')
    show=cursor.fetchone()
    print(show)
    conn.commit()
    conn.close()
def extractManyRecord():
    conn=pc.connect(dbname='school',user='postgres',password='Abhi@2003shek',host='localhost',port=5432)
    cursor=conn.cursor()
    cursor.execute('''select * from class8''')
    show=cursor.fetchall()
    for data in show:
        print(data)
    conn.commit()
    conn.close()
extractManyRecord()