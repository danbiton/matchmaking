import pyodbc
import random

class SQL:
    def __init__(self):
        self.server = 'DESKTOP-QCOJ24N\\SQLEXPRESS'
        self.database = 'matchmaking'
        self.driver = '{ODBC Driver 17 for SQL Server}'
        self.connection = pyodbc.connect(
            f'DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes;')
        self.cursor = self.connection.cursor()

    def execute(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            
            self.cursor.execute(query)

    def fetchall(self):
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()


def create_table_if_not_exists(sql):
    sql.execute('''
    IF OBJECT_ID('user_preferences', 'U') IS NOT NULL
        DROP TABLE user_preferences;
    ''')
    sql.commit()

    create_table_query = '''
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
        age_value INT,
        sect_value VARCHAR(20) NOT NULL CHECK (sect_value IN ('Hasidic', 'Ashkenazi', 'Sephardi')),
        studying_working_value VARCHAR(10) NOT NULL CHECK (studying_working_value IN ('studying', 'working')),
        eye_color_value VARCHAR(20) NOT NULL CHECK (eye_color_value IN ('light blue', 'brown', 'green')),
        skin_color_value VARCHAR(20) NOT NULL CHECK (skin_color_value IN ('light', 'brown')),
        israel_abroad_value VARCHAR(20) NOT NULL CHECK (israel_abroad_value IN ('Israel', 'abroad')),
        height_value INT,
        appearance_value VARCHAR(20) NOT NULL CHECK (appearance_value IN ('Very thin', 'thin', 'average', 'full', 'Fat'))
    );
    '''
    sql.execute(create_table_query)
    sql.commit()


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
        "age_value": int(input("Enter preferred age: ")),
        "sect_value": input("Enter preferred sect (Hasidic, Ashkenazi, Sephardi): "),
        "studying_working_value": input("Enter preferred studying/working status (studying, working): "),
        "eye_color_value": input("Enter preferred eye color (light blue, brown, green): "),
        "skin_color_value": input("Enter preferred skin color (light, brown): "),
        "israel_abroad_value": input("Enter preferred location (Israel, abroad): "),
        "height_value": int(input("Enter preferred height: ")),
        "appearance_value": input("Enter appearance (Very thin, thin, average, full, Fat): ")
    }
    return user_prefs


def insert_user_preferences(sql, prefs):
    print(f"Inserting: {prefs}")  # Debug print to check input values
    sql.execute('''
        INSERT INTO user_preferences (
            serial_number, mother_name_diff, age_diff, sect_diff, eye_color_diff, skin_color_diff, israel_abroad_diff, 
            studying_working_diff, height_diff,  age_value, sect_value, studying_working_value, 
            eye_color_value, skin_color_value, israel_abroad_value, height_value, appearance_value
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,  ?, ?, ?, ?, ?, ?, ?)
    ''', (
        prefs['serial_number'], prefs['mother_name_diff'], prefs['age_diff'], prefs['sect_diff'],
        prefs['eye_color_diff'],
        prefs['skin_color_diff'], prefs['israel_abroad_diff'], prefs['studying_working_diff'], prefs['height_diff'],
        prefs['age_value'], prefs['sect_value'], prefs['studying_working_value'],
        prefs['eye_color_value'], prefs['skin_color_value'], prefs['israel_abroad_value'], prefs['height_value'],
        prefs['appearance_value']
    ))
    sql.commit()


# הרצת הסקריפט
# if __name__ == "__main__":
    # sql = SQL()
    # create_table_if_not_exists(sql)

    # for i in range(200):
    #     user_prefs = {
    #         "serial_number": i + 1,
    #         "mother_name_diff": random.randint(0, 10),
    #         "age_diff": random.randint(0, 10),
    #         "sect_diff": random.randint(0, 10),
    #         "eye_color_diff": random.randint(0, 10),
    #         "skin_color_diff": random.randint(0, 10),
    #         "israel_abroad_diff": random.randint(0, 10),
    #         "studying_working_diff": random.randint(0, 10),
    #         "height_diff": random.randint(0, 10),
    #         "age_value": random.randint(1, 10),
    #         "sect_value": random.choice(["Hasidic", "Ashkenazi", "Sephardi"]),
    #         "studying_working_value": random.choice(["studying", "working"]),
    #         "eye_color_value": random.choice(['light blue', 'brown', 'green']),
    #         "skin_color_value": random.choice(['light', 'brown']),
    #         "israel_abroad_value": random.choice(["Israel", 'abroad']),
    #         "height_value": random.randint(150, 185),
    #         "appearance_value": random.choice(['Very thin', 'thin', 'average', 'full', 'Fat']),
    #     }
    #     insert_user_preferences(sql, user_prefs)
    # sql.commit()
    sql.close()


