import random, sqlite3

def create_name(dlzka:int)->str:
    temp = ""
    samo = "aeiouy"
    spolu = "bcdfghjklmnpqrstvwxyz"
    for i in range(dlzka):
        if i % 2 == 0:
            temp += random.choice(samo)
        else :
            temp += random.choice(spolu)
        temp = temp.capitalize()
    return temp
oci = ["modra","hneda","zelene"]
con = sqlite3.connect("D:\škola\Anton\pokusna.db")
cur = con.cursor()

for i in range(1):
    print("INSERT INTO studenti (meno,priezvisko,vek,noha,oci) VAlURS('"+create_name(random.randint(3,6)+"','"+create_name(random.randint(3,6)+"','"+random.randint(16,19)+"','"+random.randint(31,45)+"','"+random.choice(oci)"')")