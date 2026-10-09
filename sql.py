import pymysql
conn=pymysql.connect(
    host='localhost',
    user='root',
    password='Anoop@123',
    database='aug'
)

cursor=conn.cursor()
#sql="insert into employee values(1,'arun',20000,'cse')"
#sql="insert into employee values(2,'abin',30000,'hr')"
#sql="insert into employee values(4,'akash',45000,'dev')"
#sql="insert into employee values(5,'abin',40000,'dev')"
#sql="insert into employee values(5,'abin',40000,'dev')"
#sql="insert into employee values(6,'abin',50000,'it')"
sql="select * from employee"
cursor.execute(sql)
row=cursor.fetchall()
#row=cursor.fetchmany(3)
#row=cursor.fetchone()

for i in row:
   print(i[0],i[1],i[2],i[3])
#sql="create table employee(id int primary key,name varchar(30),salary int,dept varchar(20))"


conn.commit()
conn.close()
