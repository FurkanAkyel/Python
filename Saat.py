saat = int(input("Saati giriniz = "))
dakika = int(input("Dakikayı giriniz = "))

if dakika == 00:
    print(f"Saat {saat}.")
elif dakika == 15:
    print(f"Saat {saat}'i çeyrek geçiyor.")
elif dakika == 30:
    print(f"Saat {saat} buçuk.")
elif dakika == 45:
    if saat == 23:
        print(f"Saat 00'ye çeyrek var.")
    else:
        print(f"Saat {saat+1}'e çeyrek var.")
elif 00 < dakika < 30:
    print(f"Saat {saat}'i {dakika} geçiyor.")
elif 30 < dakika < 60:
    if saat == 23:
        print(f"Saat 00'ye {60-dakika} var.")
    else:
        print(f"Saat {saat+1}'e {60-dakika} var.")