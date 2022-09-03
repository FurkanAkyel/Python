# Giriş veya Kayıt Sistemi

from tkinter import *
import os

def Kayit():
    global kayitEkran
    kayitEkran = Toplevel(anaEkran)
    kayitEkran.title("Kayıt Ol")
    kayitEkran.geometry("600x480")

    global kullaniciAd
    global sifre
    global kullaniciAdEntry
    global sifreEntry
    kullaniciAd = StringVar()
    sifre = StringVar()

    Label(kayitEkran, text="Lütfen Detayları Giriniz", bg="cyan").pack()
    Label(kayitEkran, text="").pack()
    kullaniciAdLabel = Label(kayitEkran, text=" Kullanıcı Adı * ")
    kullaniciAdLabel.pack()
    kullaniciAdEntry = Entry(kayitEkran, textvariable=kullaniciAd)
    kullaniciAdEntry.pack()
    sifreLabel = Label(kayitEkran, text="Şifre * ")
    sifreLabel.pack()
    sifreEntry = Entry(kayitEkran, textvariable=sifre, show="*")
    sifreEntry.pack()
    Label(kayitEkran, text="").pack()
    Button(kayitEkran, text="Kayıt Ol", width=20, height=2, bg="cyan", command = KullaniciKayit).pack()

def Giris():
    global girisEkran
    girisEkran = Toplevel(anaEkran)
    girisEkran.title("Giriş Yap")
    girisEkran.geometry("600x480")
    Label(girisEkran, text="Lütfen Detayları Giriniz").pack()
    Label(girisEkran, text="").pack()

    global kullaniciAdDogrulama
    global sifreDogrulama 

    kullaniciAdDogrulama = StringVar()
    sifreDogrulama = StringVar()

    global kullaniciAdGirisEntry
    global sifreGirisEntry

    Label(girisEkran, text="Kullanıcı Ad * ").pack()
    kullaniciAdGirisEntry = Entry(girisEkran, textvariable=kullaniciAdDogrulama)
    kullaniciAdGirisEntry.pack()
    Label(girisEkran, text="").pack()
    Label(girisEkran, text="Şifre * ").pack()
    sifreGirisEntry = Entry(girisEkran, textvariable=sifreDogrulama, show="*")
    sifreGirisEntry.pack()
    Label(girisEkran, text="").pack()
    Button(girisEkran, text="Giriş Yap", width=20, height=2, bg="cyan", command=GirisDogrulama).pack()
   
def KullaniciKayit():

    kullaniciAdBilgi = kullaniciAd.get()
    sifreBilgi = sifre.get()

    file = open(kullaniciAdBilgi, "w")
    file.write(kullaniciAdBilgi + "\n")
    file.write(sifreBilgi)
    file.close()

    kullaniciAdEntry.delete(0, END)
    sifreEntry.delete(0, END)

    Label(kayitEkran, text="Kayıt Başarılı", fg="cyan", font=("calibri", 11)).pack()

def GirisDogrulama():
    kullaniciAd1 = kullaniciAdDogrulama.get()
    sifre1 = sifreDogrulama.get()
    kullaniciAdGirisEntry.delete(0, END)
    sifreGirisEntry.delete(0, END)

    dosyaListe = os.listdir()
    if kullaniciAd1 in dosyaListe:
        dosya1 = open(kullaniciAd1, "r")
        dogrula = dosya1.read().splitlines()
        if sifre1 in dogrula:
            GirisBasarili()

        else:
            SifreEslesmiyor()

    else:
        KullaniciBulunamadi()

def GirisBasarili():
    global girisBasariliEkran
    girisBasariliEkran = Toplevel(girisEkran)
    girisBasariliEkran.title("Başarılı")
    girisBasariliEkran.geometry("150x100")
    Label(girisBasariliEkran, text="Giriş Başarılı").pack()
    Button(girisBasariliEkran, text="Tamam", command=SilGirisBasarili).pack()

def SifreEslesmiyor():
    global sifreEslesmiyorEkran
    sifreEslesmiyorEkran = Toplevel(girisEkran)
    sifreEslesmiyorEkran.title("Başarılı")
    sifreEslesmiyorEkran.geometry("300x200")
    Label(sifreEslesmiyorEkran, text="Şifre Yanlış").pack()
    Button(sifreEslesmiyorEkran, text="Tamam", command=SilSifreEslesmiyor).pack()

def KullaniciBulunamadi():
    global kullaniciBulunamadiEkran
    kullaniciBulunamadiEkran = Toplevel(girisEkran)
    kullaniciBulunamadiEkran.title("Başarılı")
    kullaniciBulunamadiEkran.geometry("300x200")
    Label(kullaniciBulunamadiEkran, text="Kullanıcı Bulunamadı").pack()
    Button(kullaniciBulunamadiEkran, text="Tamam", command=SilKullaniciBulunamadi).pack()

def SilGirisBasarili():
    girisBasariliEkran.destroy()

def SilSifreEslesmiyor():
    sifreEslesmiyorEkran.destroy()

def SilKullaniciBulunamadi():
    kullaniciBulunamadiEkran.destroy()

def Ekran():
    global anaEkran
    anaEkran = Tk()
    anaEkran.geometry("600x480")
    anaEkran.title("Sistem Giriş Ekranı")

    Label(text="Kayıt Ol veya Giriş Yap", bg="cyan", width="600", height="4", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Giriş Yap", width="60", height="4", command=Giris).pack()
    Label(text="").pack()
    Button(text="Kayıt Ol", width="60", height="4", command=Kayit).pack()
    
    anaEkran.mainloop()

Ekran()