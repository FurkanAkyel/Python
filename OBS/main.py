import mysql.connector

connection = mysql.connector.connect(

)
cursor = connection.cursor()

"""
Dur-Sistem Durdur
1-Öğrenci Kayıt
2-Öğrenci Bilgisi
3-Öğretmen Kayıt
4-Öğretmen Bilgisi
"""

while True:
    islem = input("Yapmak istediğiniz işlem = ")

    if islem == "Dur":
        break
    elif islem == "1":
        add_name=input("Öğrenci Ad = ")
        add_surName=input("Öğrenci SoyAd = ")
        add_tc=input("Öğrenci TC = ")
        add_birthdate=input("Doğum Tarihi = ")
        add_phoneNumber=input("Telefon Numarası = ")
        add_momName=input("Anne Ad = ")
        add_fatherName=input("Baba Ad = ")
        student_dict = {"name":add_name, "surName":add_surName, "tc":add_tc, "birthday":add_birthdate, "phoneNumber":add_phoneNumber, "momName":add_momName, "fatherName":add_fatherName}

    elif islem == 2:
        continue
    elif islem == 3:
        continue
    elif islem == 4:
        continue