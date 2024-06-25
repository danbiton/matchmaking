# אני עושה קוד שמקבל את המשתמש ומבקש ממנו את הפרטים האישים שלו
# print("hello dear user!\nIf you have not registered yet, please enter your personal details: ")
def starts(start):
    if start == 0:
        x =2
        # נעשה כאן פונקציה שמקבלת נתונים ומוסיפה אותם לטבלה ומחזירה True
    if start == 1:
        x = 1
        # נעשה כאן פונקציה ששאולת אותו על שמו ו id שלו, ומחזירה True

def main():
    print("hello dear user!")
    start = int(input("If you are registered press 1\n If you are not registered press 0"))
    if starts(start):
        x =3

