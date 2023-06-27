def calculateNote(line):
    line = line[:-1]
    noteList = line.split(":")
    name = noteList[0]
    notes = noteList[1].split(",")

    note1 = int(notes[0])
    note2 = int(notes[1])
    note3 = int(notes[2])

    average = (note1+note2+note3)/3

    if 95<=average<=100:
        harf ="A1"
    elif 90<=average<95:
        harf ="A2"
    elif 85<=average<90:
        harf ="A3"
    elif 80<=average<85:
        harf ="B1"
    elif 75<=average<80:
        harf ="B2"
    elif 70<=average<75:
        harf ="B3"
    elif 65<=average<70:
        harf ="C1"
    elif 60<=average<65:
        harf ="C2"
    elif 55<=average<60:
        harf ="C3"
    else:
        harf ="FF"
    
    return name + ": "+ harf + "\n"

def readNotes():
    with open("examNotes.txt","r",encoding="utf-8") as file:
        for line in file:
            print(calculateNote(line))

def inputNotes():
    name = input("Öğrenci Ad:")
    surname = input("Öğrenci SoyAd:")
    note1 = input("Not 1:")
    note2 = input("Not 2:")
    note3 = input("Not 3:")

    with open("examNotes.txt","a", encoding="utf-8") as file:
        file.write(name+ " "+ surname+ ":"+note1+","+note2+","+note3+"\n")
                   
def saveNotes():
    with open("examNotes.txt","r",encoding="utf-8") as file:
        saveList = []
        for i in file:
            saveList.append(calculateNote(i))
        
        with open("conclusion.txt","w",encoding="utf-8") as file2:
            for i in saveList:
                file2.write(i)
def exit():
    pass

while True:
    process = input("1 - Notları Oku\n2 - Not Gir\n3 - Notları Kaydet\n4 - Çıkış\n")
    if process == "1":
        readNotes()
    elif process == "2":
        inputNotes()
    elif process == "3":
        saveNotes()
    elif process == "4":
        break