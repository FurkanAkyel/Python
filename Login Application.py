#Giriş veya Kayıt Sistemi

from tkinter import *
import os

def Ekran():

    anaEkran = Tk()
    anaEkran.geometry("300x250")
    anaEkran.title("Sistem Giriş Ekranı")

Label(text="Kayıt Ol veya Giriş Yap", bg="green", width="300", height="2", font=("Calibri", 13)).pack()
Label(text="").pack()

Button(text="Giriş Yap", width="30", height="2").pack()
Label(text="").pack()

Button(text="Kayıt Ol", width="30", height="2").pack()

anaEkran.mainloop()

Ekran()