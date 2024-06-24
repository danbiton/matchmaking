import pyodbc

server = 'DESKTOP-QCOJ24N\\SQLEXPRESS'
database = 'matchmaking'
driver = '{ODBC Driver 17 for SQL Server}'


connection = pyodbc.connect(
    f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;')

cursor = connection.cursor()


exe1 = "DELETE FROM Male WHERE age = 34"
cursor.execute(exe1)


connection.commit()


show = "insert into Male(id,f_name,l_name,addres,age) values(10,'daniel','biton','22 sireni st',31)"
cursor.execute(show)
connection.commit()

s = "select * from Male"
cursor.execute(s)
for row in cursor:
    print(row)


# update_query = """
#         UPDATE Male
#         SET age = DATEDIFF(year, DateOfBirth, GETDATE())
#         WHERE DateOfBirth IS NOT NULL
#         """
# cursor.execute(update_query)   
# connection.commit()     

cursor.close()
connection.close()

print("test")

