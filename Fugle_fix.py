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
    "Blå",
    "Gul",
    "Brun",
    "Grå"
]


def fugle_tjekker(att,t):
    if att == fødder:
        for i in attributes:
            if attributes[0] == att:
                pass
            if attributes[1] == att:
                pass
            if attributes[2] == att:
                pass
            if attributes[3] == att:
                pass
            if attributes[4] == att:
                pass
def fugle_counter(att, t):
    c.execute("SELECT * FROM Fugl WHERE "+str(t)+"=")
    if  == att:
        

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

def fugle_score(att, t):
    pass

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

for i in farver():
    print(farver)
    farver = input("")
    if farver == "Blå, Gul, Sort, Hvid, Rød, Blå, Gul, Brun, Grå":
        continue
    if farver == "Det var det":
        break