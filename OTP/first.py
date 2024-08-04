class Person:

    address = "no information"

    def __init__(self, name, surname, year):
        self.name = name
        self.surname = surname
        self.year = year
        print("init metodu çalıştı")

    def info(self):
        print(f"Kişi = İsim : {self.name}, Soyisim : {self.surname}, Doğum Yılı : {self.year}, Adresi : {self.address}")

p1 = Person(name = "Furkan", surname = "Akyel",year = 2003)
p2 = Person('Ali', 'Veli', 2000)
p1.address = "İstanbul"

p1.info()
p2.info()