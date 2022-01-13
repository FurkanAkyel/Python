from tkinter import *
import os

def Kayit():
    global kayit_ekrani
    kayit_ekrani = Toplevel(ana_ekran)
    kayit_ekrani.title("Kayıt Ol")
    kayit_ekrani.geometry("300x250")
 
    global kullanici_adi
    global sifre
    global kullanici_adi_giris
    global sifre_giris
    kullanici_adi = StringVar()
    sifre = StringVar()
 
    Label(kayit_ekrani, text="Kayıt Olmak İçin Detayları Giriniz", bg="cyan").pack()
    Label(kayit_ekrani, text="").pack()
    username_lable = Label(kayit_ekrani, text="Kullanıcı Adı * ")
    username_lable.pack()
    username_entry = Entry(kayit_ekrani, textvariable=kullanici_adi)
    username_entry.pack()
    password_lable = Label(kayit_ekrani, text="Şifre * ")
    password_lable.pack()
    password_entry = Entry(kayit_ekrani, textvariable=sifre, show='*')
    password_entry.pack()
    Label(kayit_ekrani, text="").pack()
    Button(kayit_ekrani, text="Kayıt Ol", width=10, height=1, bg="cyan", command = kayit_kullanici).pack()
 
def Giris():
    global giris_ekrani
    giris_ekrani = Toplevel(ana_ekran)
    giris_ekrani.title("Giriş Yap")
    giris_ekrani.geometry("300x250")
    Label(giris_ekrani, text="Giriş Yapmak İçin Detayları Giriniz").pack()
    Label(giris_ekrani, text="").pack()
 
    global kullanici_dogrulama
    global sifre_dogrulama
 
    kullanici_dogrulama = StringVar()
    sifre_dogrulama = StringVar()
 
    global kullanici_adi_giris_girisi
    global sifre_giris_girisi
 
    Label(giris_ekrani, text="Kullanıcı Adı * ").pack()
    kullanici_giris_girisi = Entry(giris_ekrani, textvariable=kullanici_dogrulama)
    kullanici_giris_girisi.pack()
    Label(giris_ekrani, text="").pack()
    Label(giris_ekrani, text="Password * ").pack()
    sifre_giris_girisi = Entry(giris_ekrani), textvariable=sifre_dogrulama, show= '*')
    sifre_giris_girisi.pack()
    Label(giris_ekrani, text="").pack()
    Button(giris_ekrani, text="Giriş Yap", width=10, height=1, command = giris_dogrulama).pack()
 
# Implementing event on register button
 
def register_user():
 
    kullanici_adi_dogrulama = kullanici_adi.get()
    sifre_bilgi = sifre.get()
 
    file = open(kullanici_adi_dogrulama, "w")
    file.write(kullanici_adi_dogrulama + "\n")
    file.write(sifre_dogrulama)
    file.close()
 
    kullanici_adi_girisi.delete(0, END)
    sifre_girisi.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
def HesapEkran():
    global ana_ekran
    ana_ekran = Tk()
    ana_ekran.geometry("300x250")
    ana_ekran.title("Account Login")
    Label(text="Hesabınıza Giriş Yapın veya Oluşturun", bg="cyan", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Giriş Yap", height = "2", width = "30", command = login).pack()
    Label(text = "").pack()
    Button(text = "Kayıt Ol", height = "2", width = "30", command = register).pack()
 
    ana_ekran.mainloop()
 
HesapEkran()