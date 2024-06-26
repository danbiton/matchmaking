# main.py (או כל שם קובץ אחר)

from sql_key import SQL

# יצירת אובייקט מהמחלקה SQL
sql = SQL()

# דוגמאות לשימוש במתודות המחלקה
try:
    exe1 = "DELETE FROM Male WHERE age = 34"
    show = "insert into Male(id,f_name,l_name,addres,age) values(10,'daniel','biton','22 sireni st',31)"
    sql.execute(show)
    sql.commit()

    s = "select * from Male"
    sql.execute(s)
    for row in sql.fetchall():
        print(row)

    update_query = """
        UPDATE Male
        SET age = DATEDIFF(year, DateOfBirth, GETDATE())
        WHERE DateOfBirth IS NOT NULL
    """
    sql.execute(update_query)
    sql.commit()

    query_male = "SELECT * from ProfiLeMale"
    query_female = "SELECT * FROM ProfileFemale"

    sql.execute(query_male)
    males = sql.fetchall()

    sql.execute(query_female)
    females = sql.fetchall()

    matches = []

    for male in males:
        (serial_number, male_first_name, male_last_name, father_name, mother_name, male_city, israel_abroad, male_age,
         studying_working, sect, skin_color, height, eye_color, weight, date_of_birth) = male

        for female in females:
            (serial_number, female_first_name, female_last_name, father_name, mother_name, female_city, israel_abroad, female_age,
             studying_working, sect, skin_color, height, eye_color, weight, date_of_birth) = female

            if abs(male_age - female_age) <= 3 and male_city == female_city:
                matches.append((male_first_name, male_last_name, female_first_name, female_last_name))

    for match in matches:
        print(f"Match found: {match[0]} {match[1]} and {match[2]} {match[3]}")

    sql.commit()
    print("ProfileMale data after insert:")
    sql.execute("SELECT * FROM ProfileMale")
    males_after_insert = sql.fetchall()
    for male in males_after_insert:
        print(male)

    print("ProfileFemale data after insert:")
    sql.execute("SELECT * FROM ProfileFemale")
    females_after_insert = sql.fetchall()
    for female in females_after_insert:
        print(female)

finally:
    sql.close()

