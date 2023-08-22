import mysql.connector


#connecting with database
mydb = mysql.connector.connect(
  user='root',
  host='localhost',
  database='testdb'
)
myCursor=mydb.cursor()

#creating table in database
myCursor.execute("CREATE TABLE student(name VARCHAR(255),age INTEGER(10))")


#getiting all table
myCursor.execute("SHOW TABLES")

#showing all table in through iterator
for tb in myCursor:
  print(tb)

#creating insertion formula
sqlInsertionFormula='INSERT INTO student(name,age) VALUES(%s,%s)'
# listOfTupples=[('zarar',27),('saram',27),('khan',27),('goshi',27)]
#
# # myCursor.execute(sqlInsertionFormula,listOfTupples)
# myCursor.executemany(sqlInsertionFormula,listOfTupples)

myCursor.execute('select * from student where name like "%sohail%"')
studentagelist=myCursor.fetchall()

for student in studentagelist:
  print(student)
def be_friend(name,ddd='dddddd'):
  pass


name='cccccc'
be_friend(name,'ddd')



mydb.commit()




