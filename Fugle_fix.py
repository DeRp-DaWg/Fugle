import sqlite3
conn = sqlite3.connect("Fugle_db.db")
c = conn.cursor()

attributes = [
    "fødder",
    "farver",
    "næb",
    "størrelse",
    "mad"
]
fugle_typer = [
    "blåmejse",
    "blishøne",
    "bogfinke",
    "fasan",
    "fiskehejre",
    "gråand",
    "grågås",
    "gråkrage",
    "hættemåge",
    "husskade",
    "hvid_vipstjert",
    "klippedue",
    "knopsvane",
    "musvit",
    "ringdue",
    "skarv",
    "skovspurv",
    "solsort",
    "sølvmåge"
]
farver = [
    "Blå",
    "Gul",
    "Sort",
    "Hvid",
    "Rød",
    "Brun",
    "Grå"
]
score = {
    "Blåmejse": 0,
    "Blishøne": 0,
    "Bogfinke": 0,
    "Fasan": 0,
    "Fiskehejre": 0,
    "Gråand": 0,
    "Grågås": 0,
    "Gråkrage": 0,
    "Hættemåge": 0,
    "Husskade": 0,
    "Hvid_vipstjert": 0,
    "Klippedue": 0,
    "Knopsvane": 0,
    "Musvit": 0,
    "Ringdue": 0,
    "Skarv": 0,
    "Skovspurv": 0,
    "Solsort": 0,
    "Sølvmåge": 0
}

def fugle_counter(att, t):
    order66 = ("SELECT Fugl FROM Fugle WHERE "+str(t)+"='"+str(att)+"'")
    var = c.execute(order66)
    for row in c:
        score[row[0]] = score.get(row[0], 0) + 1
def fugle_counter_special(att, t):
    order66 = ("SELECT Fugl FROM Fugle WHERE "+str(t)+" LIKE '%"+str(att)+"%'")
    var = c.execute(order66)
    for row in c:
        score[row[0]] = score.get(row[0], 0) + 1

while True:
    print("Hvordan ser fuglens fødder ud?")
    print("Svømmefødder, Kløer")
    fødder = input("")
    if fødder == "exit":
        break
    fugle_counter(fødder, "Fod")
    
    print("Hvordan ser fuglens næb ud?")
    print("Næb, Andenæb")
    næb = input("")
    if næb == "exit":
        break
    fugle_counter(næb, "Næb")
    
    print("Hvordan ser fuglens størrelse ud?")
    print("Stor, Mellem, Lille")
    størrelse = input("")
    if størrelse == "exit":
        break
    fugle_counter(størrelse, "Størrelse")
    
    while True:
        print("Hvilke farver har fuglen?")
        print("Blå, Gul, Sort, Hvid, Rød, Brun, Grå (Vælg en af gangen)")
        print("Hvis fuglen ikke har flere, så skriv nej")
        farve = input("")
        if farve == "exit":
            break
        elif farve == "nej":
            break
        fugle_counter_special(farve, "Farve")
    break
print(score)


#def fugle_counter(att, t):
#    blåmejse_c = 0
#    blishøne_c = 0
#    bogfinke_c = 0
#    fasan_c = 0
#    fiskehejre_c = 0
#    gråand_c = 0
#    grågås_c = 0
#    gråkrage_c = 0
#    hættemåge_c = 0
#    husskade_c = 0
#    hvid_vipstjert_c = 0
#    klippedue_c = 0
#    knopsvane_c = 0
#    musvit_c = 0
#    ringdue_c = 0
#    skarv_c = 0
#    skovspurv_c = 0
#    solsort_c = 0
#    sølvmåge_c = 0
#    count = 0
#    if blåmejse[t] == att:
#        count += 1
#        blåmejse_c += 1
#    if blishøne[t] == att:
#        count += 1
#        blishøne_c += 1
#    if bogfinke[t] == att:
#        count += 1
#        bogfinke_c += 1
#    if fasan[t] == att:
#        count += 1
#        fasan_c += 1
#    if fiskehejre[t] == att:
#        count += 1
#        fiskehejre_c += 1
#    if gråand[t] == att:
#        count += 1
#        gråand_c += 1
#    if grågås[t] == att:
#        count += 1
#        grågås_c += 1
#    if gråkrage[t] == att:
#        count += 1
#        gråkrage_c += 1
#    if hættemåge[t] == att:
#        count += 1
#        hættemåge_c += 1
#    if husskade[t] == att:
#        count += 1
#        husskade_c += 1
#    if hvid_vipstjert[t] == att:
#        count += 1
#        hvid_vipstjert_c += 1
#    if klippedue[t] == att:
#        count += 1
#        klippedue_c += 1
#    if knopsvane[t] == att:
#        count += 1
#        knopsvane_c += 1
#    if musvit[t] == att:
#        count += 1
#        musvit_c += 1
#    if ringdue[t] == att:
#        count += 1
#        ringdue_c += 1
#    if skarv[t] == att:
#        count += 1
#        skarv_c += 1
#    if skovspurv[t] == att:
#        count += 1
#        skovspurv_c += 1
#    if solsort[t] == att:
#        count += 1
#        solsort_c += 1
#    if sølvmåge[t] == att:
#        count += 1
#        sølvmåge_c += 1
#    return(count, blåmejse_c, blishøne_c, bogfinke_c, fasan_c, fiskehejre_c, gråand_c, grågås_c,
#           gråkrage_c, hættemåge_c, husskade_c, hvid_vipstjert_c, klippedue_c, knopsvane_c, musvit_c,
#           ringdue_c, skarv_c, skovspurv_c, solsort_c, sølvmåge_c)

#for i in range(1,2):
#    fugle_dict = {
#        "blåmejse_c": 0,
#        "blishøne_c": 0,
#        "bogfinke_c": 0,
#        "fasan_c": 0,
#        "fiskehejre_c": 0,
#        "gråand_c": 0,
#        "grågås_c": 0,
#        "gråkrage_c": 0,
#        "hættemåge_c": 0,
#        "husskade_c": 0,
#        "hvid_vipstjert_c": 0,
#        "klippedue_c": 0,
#        "knopsvane_c": 0,
#        "musvit_c": 0,
#        "ringdue_c": 0,
#        "skarv_c": 0,
#        "skovspurv_c": 0,
#        "solsort_c": 0,
#        "sølvmåge_c": 0,
#        "count": 0
#    }

#for i in farver():
#    print(farver)
#    farver = input("")
#    if farver == "Blå, Gul, Sort, Hvid, Rød, Blå, Gul, Brun, Grå":
#        continue
#    if farver == "Det var det":
#        break