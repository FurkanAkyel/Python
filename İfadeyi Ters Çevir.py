# Girilen İfadeyi Terse Çeviren Program

def reverse(txt):
    if len(txt) == 0:
        return txt
    else:
        return reverse(txt[1:]) + txt[0]
        
print(reverse("Say Hello to Pyhton!"))