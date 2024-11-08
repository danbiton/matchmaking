import pyodbc
import random
from datetime import datetime, timedelta

# פרטי החיבור ל-SQL Server
server = 'DESKTOP-9HC32H2\SQLEXPRESS'  # שם השרת שלך
database = 'matchmaking'  # שם בסיס הנתונים שלך

# שמות לדוגמה
female_first_names = ['Sarah', 'Rivka', 'Leah', 'Miriam', 'Rachel', 'Hannah', 'Esther', 'Naomi', 'Batya', 'Tzipora',
                      'Deborah', 'Chaya', 'Malkah', 'Yocheved', 'Osnat', 'Efrat', 'Tamar', 'Yona', 'Aliza', 'Yael']
last_names = ['Cohen', 'Levi', 'Mizrahi', 'Gabay', 'Ben David', 'Katz', 'Rosenberg', 'Goldstein', 'Peretz', 'Shapiro',
              'Friedman', 'Weinstein', 'Baruch', 'Shalom', 'Ezra', 'Malka', 'Shimon', 'Dahan', 'Biton', 'Ashkenazi']
father_names = ['David', 'Jacob', 'Aaron', 'Itzhak', 'Eliyahu', 'Shlomo', 'Benjamin', 'Mordechai', 'Natan', 'Asher',
                'Avraham', 'Yosef', 'Samuel', 'Haim', 'Zvi', 'Gabriel', 'Meir', 'Ovadia', 'Eitan', 'Reuven']
mother_names = ['Sarah', 'Rivka', 'Leah', 'Miriam', 'Rachel', 'Hannah', 'Esther', 'Naomi', 'Batya', 'Tzipora',
                'Deborah', 'Chaya', 'Malkah', 'Yocheved', 'Osnat', 'Efrat', 'Tamar', 'Yona', 'Aliza', 'Yael']
cities_israel = ['Jerusalem', 'Tel Aviv', 'Haifa', 'Ramat Gan', 'Beersheba', 'Ashdod', 'Netanya', 'Holon', 'Bnei Brak', 'Herzliya',
                 'Petah Tikva', 'Rishon LeZion', 'Ashkelon', 'Bat Yam', 'Eilat', 'Nazareth', 'Acre', 'Ra\'anana', 'Kfar Saba', 'Modiin']
countries_abroad = ['USA', 'France', 'Canada', 'Argentina', 'Russia', 'Germany', 'Australia', 'UK']
studying_working = ['studying', 'working']
sect = ['Hasidic', 'Ashkenazi', 'Sephardi']
skin_color = ['light', 'brown']
eye_color = ['light blue', 'brown', 'green']

# פונקציה ליצירת תאריך לידה רנדומלי
def random_date(start, end):
    return start + timedelta(days=random.randint(0, int((end - start).days)))

# פונקציה לחישוב הגיל על בסיס תאריך הלידה ותאריך היעד
def calculate_age(birth_date, target_date):
    return target_date.year - birth_date.year - ((target_date.month, target_date.day) < (birth_date.month, birth_date.day))

# חיבור ל-SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=' + server + ';'
    'DATABASE=' + database + ';'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

# מחיקת הטבלה הקיימת אם היא קיימת
cursor.execute('''
IF OBJECT_ID('ProfileFemale', 'U') IS NOT NULL
    DROP TABLE ProfileFemale;
''')
conn.commit()

# יצירת הטבלה מחדש
cursor.execute('''
CREATE TABLE ProfileFemale
(
    serial_number INT IDENTITY(1,1) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    father_name VARCHAR(50) NOT NULL,
    mother_name VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    israel_abroad VARCHAR(10) NOT NULL CHECK (israel_abroad IN ('Israel', 'abroad')),
    age INT NOT NULL,
    studying_working VARCHAR(10) NOT NULL CHECK (studying_working IN ('studying', 'working')),
    sect VARCHAR(10) NOT NULL CHECK (sect IN ('Hasidic', 'Ashkenazi', 'Sephardi')),
    skin_color VARCHAR(5) NOT NULL CHECK (skin_color IN ('light', 'brown')),
    height DECIMAL(5,2) NOT NULL,
    eye_color VARCHAR(10) NOT NULL CHECK (eye_color IN ('light blue', 'brown', 'green')),
    weight DECIMAL(5,2) NOT NULL,
    date_of_birth DATE NOT NULL
);
''')
conn.commit()

# תאריך היעד לחישוב הגיל
target_date = datetime(2024, 6, 24)

# יצירת 100 רשומות רנדומליות
for i in range(200):
    first_name = random.choice(female_first_names)
    last_name = random.choice(last_names)
    father_name = random.choice(father_names)
    mother_name = random.choice(mother_names)
    israel_abroad = random.choice(['Israel', 'abroad'])
    if israel_abroad == 'Israel':
        city = random.choice(cities_israel)
    else:
        city = random.choice(countries_abroad)
    date_of_birth = random_date(datetime(1982, 1, 1), datetime(2006, 12, 31))
    age = calculate_age(date_of_birth, target_date)
    studying_working_choice = random.choice(studying_working)
    sect_choice = random.choice(sect)
    skin_color_choice = random.choice(skin_color)
    height = round(random.uniform(150.0, 180.0), 2)
    eye_color_choice = random.choice(eye_color)
    weight = round(random.uniform(45.0, 75.0), 2)
    date_of_birth_str = date_of_birth.strftime('%Y-%m-%d')

    # הכנסה לבסיס הנתונים
    cursor.execute('''
        INSERT INTO ProfileFemale (first_name, last_name, father_name, mother_name, city, israel_abroad, age, studying_working, sect, skin_color, height, eye_color, weight, date_of_birth)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', first_name, last_name, father_name, mother_name, city, israel_abroad, age, studying_working_choice, sect_choice, skin_color_choice, height, eye_color_choice, weight, date_of_birth_str)

# ביצוע commit ושחרור המשאבים
conn.commit()
cursor.close()
conn.close()
