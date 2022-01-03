# Cümle İçinde Geçen İlk Büyük Karakteri Bulma

def ilkBuyukKarakter(txt, indis = 0):
    if(len(txt) == indis):
        return ""
    elif(ord(txt[indis]) >= ord("A") and ord(txt[indis]) <= ord("Z") or txt[indis] in ["Ğ", "Ü", "Ş", "İ", "Ö", "Ç"]):
        return txt[indis]
    else:
        return ilkBuyukKarakter(txt, indis+1)

print(ilkBuyukKarakter("merhaba Dünya"))