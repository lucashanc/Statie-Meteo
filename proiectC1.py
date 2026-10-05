def Adaugare( db, id, tip, denumire, stare):
    if id in db:
        return "Id-ul exista deja in baza de date"
    db[id]={"tip":tip, "denumire":denumire, "stare":stare}
    return "Adaugare cu succes"

def Listare(db):
    if len(db)==0:
        return "Nu exista produse in baza de date"
    for id in db:
        print(f"Id: {id}, Tip: {db[id]['tip']}, Denumire: {db[id]['denumire']}, Stare: {db[id]['stare']}")

def Comanda(db, id, comanda):
    nrComenzi=0
    if id not in db:
        return "Id-ul nu exista in baza de date"
    if comanda[0] in ["on", "off"]:
            db[id]["stare"]["onoff"]=comanda[0]
            nrComenzi=1
    if len(comanda) > 1 or comanda[0] not in ["on", "off"]:
        print(1)
        print(comanda[nrComenzi:])
        db[id]["stare"]["parametrii"]=tuple(map(float, comanda[nrComenzi:]))
   
    return "Comanda a fost trimisa cu succes"

def CitireStare(db,id):
    if id not in db:
        return "Id-ul nu exista in baza de date"
    return db[id]["stare"]

def Agregare(db):
    echipamente_pornite = 0
    total_echipamente = len(db)
    
    suma_altitudine = 0
    suma_temperatura = 0
    nr_baloane = 0
    
    suma_raza = 0
    suma_unghi = 0
    nr_radare = 0
    
    total_precipitatii = 0
    nr_pluviometre = 0

    for id in db:
        # Suma echipamentelor pornite (la comun pentru toate)
        if db[id]["stare"]["onoff"] == "on":
            echipamente_pornite += 1
            
        match db[id]["tip"]:
            case "balon":
                suma_altitudine += db[id]["stare"]["parametrii"][0]
                suma_temperatura += db[id]["stare"]["parametrii"][1]
                nr_baloane += 1
            case "radar":
                suma_raza += db[id]["stare"]["parametrii"][0]
                suma_unghi += db[id]["stare"]["parametrii"][1]
                nr_radare += 1
            case "pluviometru":
                total_precipitatii += db[id]["stare"]["parametrii"][0]
                nr_pluviometre += 1

    rezultat = f"Din totalul de {total_echipamente} echipamente, sunt pornite: {echipamente_pornite}\n"
    
    if nr_baloane > 0:
        rezultat += f"Altitudine medie baloane: {suma_altitudine / nr_baloane:.2f} m\n"
        rezultat += f"Temperatură medie baloane: {suma_temperatura / nr_baloane:.2f} °C\n"
        
    if nr_radare > 0:
        rezultat += f"Rază medie scanare radare: {suma_raza / nr_radare:.2f} km\n"
        rezultat += f"Unghi mediu elevație radare: {suma_unghi / nr_radare:.2f} grade\n"
        
    if nr_pluviometre > 0:
        rezultat += f"Total precipitații acumulate: {total_precipitatii:.2f} mm\n"

    return rezultat

def adaugare_date_test(db):
    with open("date_test.txt", "r") as f:
        for line in f:
            id, tip, denumire, onoff, parametrii = line.strip().split(";")
            parametrii = tuple(map(float, parametrii.strip().split()))
            stare = {"onoff": onoff, "parametrii": parametrii}
            Adaugare(db, id, tip, denumire, stare)
db={}
adaugare_date_test(db)
while True:
    print("\n=== STAȚIE METEO - DEMO ===")
    print("1. Listează echipamente")
    print("2. Adaugă echipament")
    print("3. Trimite comandă")
    print("4. Citește stare")
    print("5. Agregare sistem")
    print("0. Ieșire")
    optiune = input("Alege o opțiune: ")
    match(int(optiune)):
        case 1:
            Listare(db)
        case 2:
            id = input("Introdu id-ul echipamentului: ")
            tip = input("Introdu tipul echipamentului: ")
            denumire = input("Introdu denumirea echipamentului: ")
            onoff = input("Introdu starea echipamentului (on/off): ")
            parametrii=tuple(map(float, input("Introdu parametrii echipamentului (separați prin spațiu): ").split()))
            stare={"onoff":onoff, "parametrii":parametrii}
            print(Adaugare(db, id, tip, denumire, stare))
        case 3:
            id = input("Introdu id-ul echipamentului dorit: ")
            comanda=tuple( input("Introduce-ti comanda: (on/off), schimbare parametrii (se vor introduce la fel ca la primul meniu)").split())
            print(Comanda(db, id, comanda))
        case 4:
            id = input("Introdu id-ul echipamentului dorit: ")
            print(CitireStare(db, id))
        case 5:
            print(Agregare(db))
