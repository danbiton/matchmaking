# אני מנסה לעשות ניסיונות לחיבור עם sql
from sql_key import SQL
# יצירת אובייקט מהמחלקה SQL
sql = SQL()
query_male = "SELECT * from ProfiLeMale WHERE serial_number = 8"

query_female = "SELECT * FROM ProfileFemale"



sql.execute(query_male)
male = sql.fetchall()

sql.execute(query_female)
female = sql.fetchall()
sql.commit()
sql.close()


# זה הפונקציה שמקבלת העדפות של אדם, פרטים שלו, ורשימה של כל הבנות אחד אחד כל ריצה מקבלת ציון
def calculate_match_score(male, female, preferences):
    score = 0
    if male.mother_name != female.first_name:
        score += preferences.mother_name_diff
    if abs(male.age - female.age) <= preferences.age_value:
        score += preferences.age_diff
    if female.eye_color in preferences.eye_color_value:
        score += preferences.eye_color_diff
    if female.sect in preferences.sect_value:
        score += preferences.sect_diff
    if female.skin_color in preferences.skin_color_value:
        score += preferences.skin_color_diff
    if female.israel_abroad == preferences.israel_abroad_value:
        score += preferences.israel_abroad_diff
    if preferences.studying_working_value == female.studying_working:
        score += preferences.studying_working_diff
    return score
# for i in females:height]
#       ,[eye_color]
#       ,[weight
#     print()

# print(females)
# print(males)

# אני רוצה לעשות טבלה שנכנס לה הגיל, ולפי גיל בודק את bmi האם רגיל או לא
def BMI(height,weight,age):
    bmi = weight / (height/100 * height/100)

    if 16 <= age <= 25:
        if bmi <= 17:
            return "very thin"
        elif 17 < bmi < 24:
            return "thin"
        elif 23 < bmi < 26:
            return "average"
        elif 25 < bmi < 30:
            return "full"
        elif bmi > 29:
            return "fat"
    if 26 <= age <= 35:
        if bmi <= 18:
            return "very thin"
        elif 18 < bmi < 25:
            return "thin"
        elif 24 < bmi < 27:
            return "average"
        elif 26 < bmi < 34:
            return "full"
        elif bmi > 33:
            return "fat"
    if age >= 36:
        if bmi <= 19:
            return "very thin"
        elif 19 < bmi <= 26:
            return "thin"
        elif 25 < bmi <= 29:
            return "average"
        elif 29 < bmi <= 34:
            return "full"
        elif bmi > 34:
            return "fat"


