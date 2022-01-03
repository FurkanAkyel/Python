# Dosyadaki Elemanı Değiştirme

def replaceTxtInFile(filepath, old, new):
    with open(filepath, "r+") as f:
        txt = f.read()
        txt = txt.replace(old, new)
        f.seek(0)
        f.truncate()
        f.write(txt)
        print(txt)
replaceTxtInFile("dosya.txt", "55", "Samsun")