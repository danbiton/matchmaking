
import pyodbc
from sql_key import SQL

def get_user_preferences():
    user_prefs = {
        "serial_number": int(input("Enter serial number: ")),
        "mother_name_diff": int(input("How important is the bride's name similarity to your mother's name? (0-10): ")),
        "age_diff": int(input("How important is the age similarity? (0-10): ")),
        "sect_diff": int(input("How important is the sect? (0-10): ")),
        "eye_color_diff": int(input("How important is the eye color? (0-10): ")),
        "skin_color_diff": int(input("How important is the skin color? (0-10): ")),
        "israel_abroad_diff": int(input("How important is it if the bride is from Israel or abroad? (0-10): ")),
        "studying_working_diff": int(input("How important is it if the bride is studying or working? (0-10): ")),
        "height_diff": int(input("How important is the height? (0-10): ")),
        "weight_diff": int(input("How important is the weight? (0-10): ")),
        "my_mother_name": input("Enter your mother's name: "),
        "age_value": int(input("Enter preferred age: ")),
        "sect_value": input("Enter preferred sect (Hasidic, Ashkenazi, Sephardi): "),
        "studying_working_value": input("Enter preferred studying/working status (studying, working): "),
        "eye_color_value": input("Enter preferred eye color (light blue, brown, green): "),
        "skin_color_value": input("Enter preferred skin color (light, brown): "),
        "israel_abroad_value": input("Enter preferred location (Israel, abroad): "),
        "height_value": int(input("Enter preferred height: ")),
        "weight_value": int(input("Enter preferred weight: "))
    }
    return user_prefs

def insert_user_preferences(sql, prefs):
    print(f"Inserting: {prefs}")  # Debug print to check input values
    sql.execute('''
        INSERT INTO user_preferences (
            serial_number, mother_name_diff, age_diff, sect_diff, eye_color_diff, skin_color_diff, israel_abroad_diff, 
            studying_working_diff, height_diff, weight_diff, my_mother_name, age_value, sect_value, studying_working_value, 
            eye_color_value, skin_color_value, israel_abroad_value, height_value, weight_value
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        prefs['serial_number'], prefs['mother_name_diff'], prefs['age_diff'], prefs['sect_diff'], prefs['eye_color_diff'], 
        prefs['skin_color_diff'], prefs['israel_abroad_diff'], prefs['studying_working_diff'], prefs['height_diff'], 
        prefs['weight_diff'], prefs['my_mother_name'], prefs['age_value'], prefs['sect_value'], prefs['studying_working_value'], 
        prefs['eye_color_value'], prefs['skin_color_value'], prefs['israel_abroad_value'], prefs['height_value'], 
        prefs['weight_value']
    ))

def create_table_if_not_exists(sql):
    create_table_query = '''
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='user_preferences' AND xtype='U')
    CREATE TABLE user_preferences (
        user_id INT IDENTITY (1,1) PRIMARY KEY,
        serial_number INT,
        mother_name_diff INT,
        age_diff INT,
        sect_diff INT,
        eye_color_diff INT,
        skin_color_diff INT,
        israel_abroad_diff INT,
        studying_working_diff INT,
        height_diff INT,
        weight_diff INT,
        my_mother_name VARCHAR(20),
        age_value INT,
        sect_value VARCHAR(20) NOT NULL CHECK (sect_value IN ('Hasidic', 'Ashkenazi', 'Sephardi')),
        studying_working_value VARCHAR(10) NOT NULL CHECK (studying_working_value IN ('studying', 'working')),
        eye_color_value VARCHAR(20) NOT NULL CHECK (eye_color_value IN ('light blue', 'brown', 'green')),
        skin_color_value VARCHAR(20) NOT NULL CHECK (skin_color_value IN ('light', 'brown')),
        israel_abroad_value VARCHAR(20) NOT NULL CHECK (israel_abroad_value IN ('Israel', 'abroad')),
        height_value INT,
        weight_value INT
    );
    '''
    sql.execute(create_table_query)

sql = SQL()  # יצירת חיבור לבסיס הנתונים

create_table_if_not_exists(sql)  # יצירת הטבלה אם היא לא קיימת

prefs = get_user_preferences()  # קבלת פרטי המשתמש

try:
    insert_user_preferences(sql, prefs)  # Insert the data into the table
    sql.commit()  # Commit the transaction
    print("User preferences have been successfully inserted into the database.")
except pyodbc.IntegrityError as e:
    print("Error inserting data:", e)
finally:
    sql.close()



