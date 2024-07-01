# אני מנסה לעשות ניסיונות לחיבור עם sql
class mach:
    my_mother_name = "Batya"
    my_israel_abroad ="Israel"
    # age
    # studying_working
    my_sect = ["Hasidic" ,"Ashkenazi"]
    # skin_color
    # height
    # eye_color
    # weight
    # date_of_birth


from sql_key import SQL
# יצירת אובייקט מהמחלקה SQL
sql = SQL()
query_male = "SELECT * from ProfiLeMale"

query_female = "SELECT * FROM ProfileFemale"



sql.execute(query_male)
males = sql.fetchall()

sql.execute(query_female)
females = sql.fetchall()
sql.commit()
sql.close()

for i in females:
    collect = 0
    if mach.my_mother_name != i.first_name:
        collect += 10
    if mach.my_israel_abroad == i.israel_abroad:
        collect += 10
    if  i.sect in mach.my_sect:
        collect += 10
    if collect == 30:
        print(i.serial_number,i.city, collect)

# for i in females:
#     print()

# print(females)
# print(males)


