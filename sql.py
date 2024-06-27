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


update_query = """
        UPDATE Male
        SET age = DATEDIFF(year, DateOfBirth, GETDATE())
        WHERE DateOfBirth IS NOT NULL
        """
cursor.execute(update_query)   
connection.commit()     

cursor.close()
connection.close()


query_male = "SELECT * from ProfiLeMale"
query_female = "SELECT * FROM ProfileFemale"

cursor.execute(query_male)


males = cursor.fetchall()


cursor.execute(query_female)

females = cursor.fetchall()


matches = []

for male in males:
     (serial_number,male_first_name,male_last_name,father_name,mother_name,male_city,israel_abroad,male_age,
     studying_working,sect,skin_color,height,eye_color,weight,date_of_birth) = male

     for female in females:
         
         (serial_number,female_first_name,female_last_name,father_name,mother_name,female_city,israel_abroad,female_age, 
         studying_working,sect,skin_color,height,eye_color,weight,date_of_birth) = female
        
         if abs(male_age - female_age) <= 3:
            
            if male_city == female_city:
                
                matches.append((male_first_name, male_last_name, female_first_name, female_last_name))


for match in matches:
    print(f"Match found: {match[0]} {match[1]} and {match[2]} {match[3]}")
    
connection.commit() 
print("ProfileMale data after insert:")
cursor.execute("SELECT * FROM ProfileMale")
males_after_insert = cursor.fetchall()
for male in males_after_insert:
    print(male)

print("ProfileFemale data after insert:")
cursor.execute("SELECT * FROM ProfileFemale")
females_after_insert = cursor.fetchall()
for female in females_after_insert:
    print(female)
cursor.close()
connection.close()   


