<<<<<<< HEAD
import sqlite3

attributes = ["fødder","farver","næb","størrelse", "mad"]
fugle_typer = ["blåmejse", "blishøne", "bogfinke",  "fasan", "fiskehejre", "gråand", "grågås", "gråkrage", "hættemåge", "husskade", "hvid_vipstjert", "klippedue",  "knopsvane","musvit", "ringdue", "skarv", "skovspurv", "solsort", "sølvmåge"]
farver = ["Blå", "Gul", "Sort", "Hvid", "Rød", "Blå", "Gul", "Brun", "Grå"]

blåmejse = {
    "fødder": "Kløer",
    "farver": "Blå, Gul, Sort",
    "næb": "Næb",
    "størrelse": "Lille",
    "mad": "Insekter, Edderkopper, Frø"
}
blishøne = {
    "fødder": "Kløer",
    "farver": "Sort, Hvid",
    "næb": "Næb",
    "størrelse": "Mellem",
    "mad": "Vandplanter"
}
bogfinke = {
    "fødder": "Kløer",
    "hannens farver": "Rød, Blå, Sort, Gul",
    "hunnens farver": "Brun, Hvid, Sort",
    "næb": "Næb",
    "størrelse": "Lille",
    "mad": "Frø, Insekter, Bog"
}
fasan = {
    "fødder": "Kløer",
    "farver": "Brun, Rød, Blå",
    "næb": "Næb",
    "størrelse": "Stor",
    "mad": "Insekter, Smådyr, Plantefrø"
}
fiskehejre = {
    "fødder": "Kløer",
    "farver": "Grå, Sort, Hvid",
    "næb": "Næb",
    "størrelse": "Stor",
    "mad": "Fisk"
}
gråand = {
    "fødder": "Svømmefødder",
    "hannens farver": "Grøn, Brun, Hvid, Blå",
    "hunnens farver": "Lysebrun, Mørkebrun, Sort, Hvid",
    "næb": "Andenæb",
    "størrelse": "Mellem",
    "mad": "Planter, Smådyr, Frø, Muslinger, Snegle, Insekter, Krebsdyr"
}
grågås = {
    "fødder": "Svømmefødder",
    "farver": "Grå, Hvid, Sort",
    "næb": "Andenæb",
    "størrelse": "Stor",
    "mad": "Korn, Blade, Rødder, Vandplanter"
}
gråkrage = {
    "fødder": "Kløer",
    "farver": "Grå, Sort",
    "næb": "Næb",
    "størrelse": "Mellem",
    "mad": "Insekter, Orme, Ådsler, Fugleunger"
}
hættemåge = {
    "fødder": "Kløer",
    "farver": "Hvid, Sort",
    "næb": "Næb",
    "størrelse": "Mellem",
    "mad": "Insekter, Småfisk, Ådsler, Orme, Snegle, Muslinger, Affald"
}
husskade = {
    "fødder": "Kløer",
    "farver": "Sort, Hvid",
    "næb": "Næb",
    "størrelse": "Lille",
    "mad": "Korn, Orme, Affald, Æg, Fugleunger"
}
hvid_vipstjert = {
    "fødder": "Kløer",
    "farver": "Hvid, Grå, Sort",
    "næb": "Næb",
    "størrelse": "Lille",
    "mad": "Insekter"
}
klippedue = {
    "fødder": "Kløer",
    "farver": "Hvid, Grå, Sort",
    "næb": "Næb",
    "størrelse": "Lille",
    "mad": "Insekter"
}
knopsvane = {
    "fødder": "Svømmefødder",
    "farver": "Hvid, Sort",
    "næb": "Andenæb",
    "størrelse": "Stor",
    "mad": "Vandplanter, Græs, Korn"
}
musvit = {
    "fødder": "Kløer",
    "farver": "Gul, Sort, Blå, Hvid",
    "næb": "Næb",
    "størrelse": "Lille",
    "mad": "Insekter"
}
ringdue = {
    "fødder": "Kløer",
    "farver": "Grå, Blå, Hvid",
    "næb": "Næb",
    "størrelse": "Mellem",
    "mad": "Frø, Korn"
}
skarv = {
    "fødder": "Svømmefødder",
    "farver": "Sort, Brun, Gul",
    "næb": "Næb",
    "størrelse": "Mellem",
    "mad": "Fisk"
}
skovspurv = {
    "fødder": "Kløer",
    "farver": "Brun, Hvid, Sort",
    "næb": "Næb",
    "størrelse": "Lille",
    "mad": "Korn, Insekter, Frø"
}
solsort = {
    "fødder": "Kløer",
    "farver": "Sort",
    "næb": "Næb",
    "størrelse": "Mellem",
    "mad": "Insekter, Snegle, Orme, Bær, Frugt"
}
sølvmåge = {
    "fødder": "Svømmefædder",
    "farver": "Sort, Grå, Hvid",
    "næb": "Næb",
    "størrelse": "Mellem",
    "mad": "Altædende, Fisk, Smådyr, Plantedele, Fugle"
}


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
    blåmejse_c = 0
    blishøne_c = 0
    bogfinke_c = 0
    fasan_c = 0
    fiskehejre_c = 0
    gråand_c = 0
    grågås_c = 0
    gråkrage_c = 0
    hættemåge_c = 0
    husskade_c = 0
    hvid_vipstjert_c = 0
    klippedue_c = 0
    knopsvane_c = 0
    musvit_c = 0
    ringdue_c = 0
    skarv_c = 0
    skovspurv_c = 0
    solsort_c = 0
    sølvmåge_c = 0
    count = 0
    if blåmejse[t] == att:
        count += 1
        blåmejse_c += 1
    if blishøne[t] == att:
        count += 1
        blishøne_c += 1
    if bogfinke[t] == att:
        count += 1
        bogfinke_c += 1
    if fasan[t] == att:
        count += 1
        fasan_c += 1
    if fiskehejre[t] == att:
        count += 1
        fiskehejre_c += 1
    if gråand[t] == att:
        count += 1
        gråand_c += 1
    if grågås[t] == att:
        count += 1
        grågås_c += 1
    if gråkrage[t] == att:
        count += 1
        gråkrage_c += 1
    if hættemåge[t] == att:
        count += 1
        hættemåge_c += 1
    if husskade[t] == att:
        count += 1
        husskade_c += 1
    if hvid_vipstjert[t] == att:
        count += 1
        hvid_vipstjert_c += 1
    if klippedue[t] == att:
        count += 1
        klippedue_c += 1
    if knopsvane[t] == att:
        count += 1
        knopsvane_c += 1
    if musvit[t] == att:
        count += 1
        musvit_c += 1
    if ringdue[t] == att:
        count += 1
        ringdue_c += 1
    if skarv[t] == att:
        count += 1
        skarv_c += 1
    if skovspurv[t] == att:
        count += 1
        skovspurv_c += 1
    if solsort[t] == att:
        count += 1
        solsort_c += 1
    if sølvmåge[t] == att:
        count += 1
        sølvmåge_c += 1
    return(count, blåmejse_c, blishøne_c, bogfinke_c, fasan_c, fiskehejre_c, gråand_c, grågås_c,
           gråkrage_c, hættemåge_c, husskade_c, hvid_vipstjert_c, klippedue_c, knopsvane_c, musvit_c,
           ringdue_c, skarv_c, skovspurv_c, solsort_c, sølvmåge_c)

def fugle_score(att, t):
    pass

while True:
    blåmejse_count = 0
    blishøne_count = 0
    bogfinke_count = 0
    fasan_count = 0
    fiskehejre_count = 0
    gråand_count = 0
    grågås_count = 0
    gråkrage_count = 0
    hættemåge_count = 0
    husskade_count = 0
    hvid_vipstjert_count = 0
    klippedue_count = 0
    knopsvane_count = 0
    musvit_count = 0
    ringdue_count = 0
    skarv_count = 0
    skovspurv_count = 0
    solsort_count = 0
    sølvmåge_count = 0
    
    
    print("Hvordan ser fuglens fødder ud?")
    print("svømmeføder, kløer. ")
    fødder = input("")
    if fødder == "exit":
        break
    count, blåmejse_fod, blishøne_fod, bogfinke_fod, fasan_fod, fiskehejre_fod, gråand_fod, grågås_fod, gråkrage_fod, hættemåge_fod, husskade_fod, hvid_vipstjert_fod, klippedue_fod, knopsvane_fod, musvit_fod, ringdue_fod, skarv_fod, skovspurv_fod, solsort_fod, sølvmåge_fod = fugle_counter(fødder, "fødder")
    
    print(blåmejse_fod)
    print(blishøne_fod)
    print(bogfinke_fod)
    print(fasan_fod)
    print(fiskehejre_fod)
    print(gråand_fod)
    print(grågås_fod)
    print(gråkrage_fod)
    print(hættemåge_fod)
    print(husskade_fod)
    print(hvid_vipstjert_fod)
    print(klippedue_fod)
    print(knopsvane_fod)
    print(musvit_fod)
    print(ringdue_fod)
    print(skarv_fod)
    print(skovspurv_fod)
    print(solsort_fod)
    print(sølvmåge_fod)
    
    blåmejse_count += blåmejse_fod
    blishøne_count += blishøne_fod
    bogfinke_count += bogfinke_fod
    fasan_count += fasan_fod
    fiskehejre_count += fiskehejre_fod
    gråand_count += gråand_fod
    grågås_count += grågås_fod
    gråkrage_count += gråkrage_fod
    hættemåge_count += hættemåge_fod
    husskade_count += husskade_fod
    hvid_vipstjert_count += hvid_vipstjert_fod
    klippedue_count += klippedue_fod
    knopsvane_count += knopsvane_fod
    musvit_count += musvit_fod
    ringdue_count += ringdue_fod
    skarv_count += skarv_fod
    skovspurv_count += skovspurv_fod
    solsort_count += solsort_fod
    sølvmåge_count += sølvmåge_fod
    
    
    print("Hvordan ser fuglens næb ud?")
    print("andenæb, næb. ")
    næb = input("")
    if næb == "exit":
        break
    count, blåmejse_næb, blishøne_næb, bogfinke_næb, fasan_næb, fiskehejre_næb, gråand_næb, grågås_næb, gråkrage_næb, hættemåge_næb, husskade_næb, hvid_vipstjert_næb, klippedue_næb, knopsvane_næb, musvit_næb, ringdue_næb, skarv_næb, skovspurv_næb, solsort_næb, sølvmåge_næb = fugle_counter(næb, "næb")
    blåmejse_count += blåmejse_næb
    blishøne_count += blishøne_næb
    bogfinke_count += bogfinke_næb
    fasan_count += fasan_næb
    fiskehejre_count += fiskehejre_næb
    gråand_count += gråand_næb
    grågås_count += grågås_næb
    gråkrage_count += gråkrage_næb
    hættemåge_count += hættemåge_næb
    husskade_count += husskade_næb
    hvid_vipstjert_count += hvid_vipstjert_næb
    klippedue_count += klippedue_næb
    knopsvane_count += knopsvane_næb
    musvit_count += musvit_næb
    ringdue_count += ringdue_næb
    skarv_count += skarv_næb
    skovspurv_count += skovspurv_næb
    solsort_count += solsort_næb
    sølvmåge_count += sølvmåge_næb
    
    print(blåmejse_count)
    print(blishøne_count)
    print(bogfinke_count)
    print(fasan_count)
    print(fiskehejre_count)
    print(gråand_count)
    print(grågås_count)
    print(gråkrage_count)
    print(hættemåge_count)
    print(husskade_count)
    print(hvid_vipstjert_count)
    print(klippedue_count)
    print(knopsvane_count)
    print(musvit_count)
    print(ringdue_count)
    print(skarv_count)
    print(skovspurv_count)
    print(solsort_count)
    print(sølvmåge_count)
    

    print("Hvor stor er fuglen?")
    print("Lille, Mellem, Stor.")
    størrelse = input("")
    if størrelse == "exit":
        break
    count, blåmejse_størrelse, blishøne_størrelse, bogfinke_størrelse, fasan_størrelse, fiskehejre_størrelse, gråand_størrelse, grågås_størrelse, gråkrage_størrelse, hættemåge_størrelse, husskade_størrelse, hvid_vipstjert_størrelse, klippedue_størrelse, knopsvane_størrelse, musvit_størrelse, ringdue_størrelse, skarv_størrelse, skovspurv_størrelse, solsort_størrelse, sølvmåge_størrelse = fugle_counter(størrelse, "størrelse")
    blåmejse_count += blåmejse_størrelse
    blishøne_count += blishøne_størrelse
    bogfinke_count += bogfinke_størrelse
    fasan_count += fasan_størrelse
    fiskehejre_count += fiskehejre_størrelse
    gråand_count += gråand_størrelse
    grågås_count += grågås_størrelse
    gråkrage_count += gråkrage_størrelse
    hættemåge_count += hættemåge_størrelse
    husskade_count += husskade_størrelse
    hvid_vipstjert_count += hvid_vipstjert_størrelse
    klippedue_count += klippedue_størrelse
    knopsvane_count += knopsvane_størrelse
    musvit_count += musvit_størrelse
    ringdue_count += ringdue_størrelse
    skarv_count += skarv_størrelse
    skovspurv_count += skovspurv_størrelse
    solsort_count += solsort_størrelse
    sølvmåge_count += sølvmåge_størrelse
    
    print(blåmejse_count)
    print(blishøne_count)
    print(bogfinke_count)
    print(fasan_count)
    print(fiskehejre_count)
    print(gråand_count)
    print(grågås_count)
    print(gråkrage_count)
    print(hættemåge_count)
    print(husskade_count)
    print(hvid_vipstjert_count)
    print(klippedue_count)
    print(knopsvane_count)
    print(musvit_count)
    print(ringdue_count)
    print(skarv_count)
    print(skovspurv_count)
    print(solsort_count)
    print(sølvmåge_count)


    print("Hvilken farver har den?")
    print("Blå, Gul, Sort, Hvid, Rød, Blå, Gul, Brun, Grå")
    for i in farver:
        print(farver)
        farve = input("")
        if farve == farver:
            continue
        elif farve == "Det var det":
            break

    

    #while True:
    #    print("Hvilke farver har fuglen?")
    #    print("Blå, Gul, Sort, Hvid, Rød, Blå, Gul, Brun, Grå")
    #    farve = input("")
    #    for i in farver():
    #        if i == farve:


=======
import sqlite3

attributes = ["fødder","farver","næb","størrelse", "mad"]
fugle_typer = ["blåmejse", "blishøne", "bogfinke",  "fasan", "fiskehejre", "gråand", "grågås", "gråkrage", "hættemåge", "husskade", "hvid_vipstjert", "klippedue",  "knopsvane","musvit", "ringdue", "skarv", "skovspurv", "solsort", "sølvmåge"]
farver = ["Blå", "Gul", "Sort", "Hvid", "Rød", "Blå", "Gul", "Brun", "Grå"]

blåmejse = {
    "fødder": "Kløer",
    "farver": "Blå, Gul, Sort",
    "næb": "Næb",
    "størrelse": "Lille",
    "mad": "Insekter, Edderkopper, Frø"
}
blishøne = {
    "fødder": "Kløer",
    "farver": "Sort, Hvid",
    "næb": "Næb",
    "størrelse": "Mellem",
    "mad": "Vandplanter"
}
bogfinke = {
    "fødder": "Kløer",
    "hannens farver": "Rød, Blå, Sort, Gul",
    "hunnens farver": "Brun, Hvid, Sort",
    "næb": "Næb",
    "størrelse": "Lille",
    "mad": "Frø, Insekter, Bog"
}
fasan = {
    "fødder": "Kløer",
    "farver": "Brun, Rød, Blå",
    "næb": "Næb",
    "størrelse": "Stor",
    "mad": "Insekter, Smådyr, Plantefrø"
}
fiskehejre = {
    "fødder": "Kløer",
    "farver": "Grå, Sort, Hvid",
    "næb": "Næb",
    "størrelse": "Stor",
    "mad": "Fisk"
}
gråand = {
    "fødder": "Svømmefødder",
    "hannens farver": "Grøn, Brun, Hvid, Blå",
    "hunnens farver": "Lysebrun, Mørkebrun, Sort, Hvid",
    "næb": "Andenæb",
    "størrelse": "Mellem",
    "mad": "Planter, Smådyr, Frø, Muslinger, Snegle, Insekter, Krebsdyr"
}
grågås = {
    "fødder": "Svømmefødder",
    "farver": "Grå, Hvid, Sort",
    "næb": "Andenæb",
    "størrelse": "Stor",
    "mad": "Korn, Blade, Rødder, Vandplanter"
}
gråkrage = {
    "fødder": "Kløer",
    "farver": "Grå, Sort",
    "næb": "Næb",
    "størrelse": "Mellem",
    "mad": "Insekter, Orme, Ådsler, Fugleunger"
}
hættemåge = {
    "fødder": "Kløer",
    "farver": "Hvid, Sort",
    "næb": "Næb",
    "størrelse": "Mellem",
    "mad": "Insekter, Småfisk, Ådsler, Orme, Snegle, Muslinger, Affald"
}
husskade = {
    "fødder": "Kløer",
    "farver": "Sort, Hvid",
    "næb": "Næb",
    "størrelse": "Lille",
    "mad": "Korn, Orme, Affald, Æg, Fugleunger"
}
hvid_vipstjert = {
    "fødder": "Kløer",
    "farver": "Hvid, Grå, Sort",
    "næb": "Næb",
    "størrelse": "Lille",
    "mad": "Insekter"
}
klippedue = {
    "fødder": "Kløer",
    "farver": "Hvid, Grå, Sort",
    "næb": "Næb",
    "størrelse": "Lille",
    "mad": "Insekter"
}
knopsvane = {
    "fødder": "Svømmefødder",
    "farver": "Hvid, Sort",
    "næb": "Andenæb",
    "størrelse": "Stor",
    "mad": "Vandplanter, Græs, Korn"
}
musvit = {
    "fødder": "Kløer",
    "farver": "Gul, Sort, Blå, Hvid",
    "næb": "Næb",
    "størrelse": "Lille",
    "mad": "Insekter"
}
ringdue = {
    "fødder": "Kløer",
    "farver": "Grå, Blå, Hvid",
    "næb": "Næb",
    "størrelse": "Mellem",
    "mad": "Frø, Korn"
}
skarv = {
    "fødder": "Svømmefødder",
    "farver": "Sort, Brun, Gul",
    "næb": "Næb",
    "størrelse": "Mellem",
    "mad": "Fisk"
}
skovspurv = {
    "fødder": "Kløer",
    "farver": "Brun, Hvid, Sort",
    "næb": "Næb",
    "størrelse": "Lille",
    "mad": "Korn, Insekter, Frø"
}
solsort = {
    "fødder": "Kløer",
    "farver": "Sort",
    "næb": "Næb",
    "størrelse": "Mellem",
    "mad": "Insekter, Snegle, Orme, Bær, Frugt"
}
sølvmåge = {
    "fødder": "Svømmefædder",
    "farver": "Sort, Grå, Hvid",
    "næb": "Næb",
    "størrelse": "Mellem",
    "mad": "Altædende, Fisk, Smådyr, Plantedele, Fugle"
}


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
    blåmejse_c = 0
    blishøne_c = 0
    bogfinke_c = 0
    fasan_c = 0
    fiskehejre_c = 0
    gråand_c = 0
    grågås_c = 0
    gråkrage_c = 0
    hættemåge_c = 0
    husskade_c = 0
    hvid_vipstjert_c = 0
    klippedue_c = 0
    knopsvane_c = 0
    musvit_c = 0
    ringdue_c = 0
    skarv_c = 0
    skovspurv_c = 0
    solsort_c = 0
    sølvmåge_c = 0
    count = 0
    if blåmejse[t] == att:
        count += 1
        blåmejse_c += 1
    if blishøne[t] == att:
        count += 1
        blishøne_c += 1
    if bogfinke[t] == att:
        count += 1
        bogfinke_c += 1
    if fasan[t] == att:
        count += 1
        fasan_c += 1
    if fiskehejre[t] == att:
        count += 1
        fiskehejre_c += 1
    if gråand[t] == att:
        count += 1
        gråand_c += 1
    if grågås[t] == att:
        count += 1
        grågås_c += 1
    if gråkrage[t] == att:
        count += 1
        gråkrage_c += 1
    if hættemåge[t] == att:
        count += 1
        hættemåge_c += 1
    if husskade[t] == att:
        count += 1
        husskade_c += 1
    if hvid_vipstjert[t] == att:
        count += 1
        hvid_vipstjert_c += 1
    if klippedue[t] == att:
        count += 1
        klippedue_c += 1
    if knopsvane[t] == att:
        count += 1
        knopsvane_c += 1
    if musvit[t] == att:
        count += 1
        musvit_c += 1
    if ringdue[t] == att:
        count += 1
        ringdue_c += 1
    if skarv[t] == att:
        count += 1
        skarv_c += 1
    if skovspurv[t] == att:
        count += 1
        skovspurv_c += 1
    if solsort[t] == att:
        count += 1
        solsort_c += 1
    if sølvmåge[t] == att:
        count += 1
        sølvmåge_c += 1
    return(count, blåmejse_c, blishøne_c, bogfinke_c, fasan_c, fiskehejre_c, gråand_c, grågås_c,
           gråkrage_c, hættemåge_c, husskade_c, hvid_vipstjert_c, klippedue_c, knopsvane_c, musvit_c,
           ringdue_c, skarv_c, skovspurv_c, solsort_c, sølvmåge_c)

def fugle_score(att, t):
    pass

while True:
    blåmejse_count = 0
    blishøne_count = 0
    bogfinke_count = 0
    fasan_count = 0
    fiskehejre_count = 0
    gråand_count = 0
    grågås_count = 0
    gråkrage_count = 0
    hættemåge_count = 0
    husskade_count = 0
    hvid_vipstjert_count = 0
    klippedue_count = 0
    knopsvane_count = 0
    musvit_count = 0
    ringdue_count = 0
    skarv_count = 0
    skovspurv_count = 0
    solsort_count = 0
    sølvmåge_count = 0
    
    
    print("Hvordan ser fuglens fødder ud?")
    print("svømmeføder, kløer. ")
    fødder = input("")
    if fødder == "exit":
        break
    count, blåmejse_fod, blishøne_fod, bogfinke_fod, fasan_fod, fiskehejre_fod, gråand_fod, grågås_fod, gråkrage_fod, hættemåge_fod, husskade_fod, hvid_vipstjert_fod, klippedue_fod, knopsvane_fod, musvit_fod, ringdue_fod, skarv_fod, skovspurv_fod, solsort_fod, sølvmåge_fod = fugle_counter(fødder, "fødder")
    
    print(blåmejse_fod)
    print(blishøne_fod)
    print(bogfinke_fod)
    print(fasan_fod)
    print(fiskehejre_fod)
    print(gråand_fod)
    print(grågås_fod)
    print(gråkrage_fod)
    print(hættemåge_fod)
    print(husskade_fod)
    print(hvid_vipstjert_fod)
    print(klippedue_fod)
    print(knopsvane_fod)
    print(musvit_fod)
    print(ringdue_fod)
    print(skarv_fod)
    print(skovspurv_fod)
    print(solsort_fod)
    print(sølvmåge_fod)
    
    blåmejse_count += blåmejse_fod
    blishøne_count += blishøne_fod
    bogfinke_count += bogfinke_fod
    fasan_count += fasan_fod
    fiskehejre_count += fiskehejre_fod
    gråand_count += gråand_fod
    grågås_count += grågås_fod
    gråkrage_count += gråkrage_fod
    hættemåge_count += hættemåge_fod
    husskade_count += husskade_fod
    hvid_vipstjert_count += hvid_vipstjert_fod
    klippedue_count += klippedue_fod
    knopsvane_count += knopsvane_fod
    musvit_count += musvit_fod
    ringdue_count += ringdue_fod
    skarv_count += skarv_fod
    skovspurv_count += skovspurv_fod
    solsort_count += solsort_fod
    sølvmåge_count += sølvmåge_fod
    
    
    print("Hvordan ser fuglens næb ud?")
    print("andenæb, næb. ")
    næb = input("")
    if næb == "exit":
        break
    count, blåmejse_næb, blishøne_næb, bogfinke_næb, fasan_næb, fiskehejre_næb, gråand_næb, grågås_næb, gråkrage_næb, hættemåge_næb, husskade_næb, hvid_vipstjert_næb, klippedue_næb, knopsvane_næb, musvit_næb, ringdue_næb, skarv_næb, skovspurv_næb, solsort_næb, sølvmåge_næb = fugle_counter(næb, "næb")
    blåmejse_count += blåmejse_næb
    blishøne_count += blishøne_næb
    bogfinke_count += bogfinke_næb
    fasan_count += fasan_næb
    fiskehejre_count += fiskehejre_næb
    gråand_count += gråand_næb
    grågås_count += grågås_næb
    gråkrage_count += gråkrage_næb
    hættemåge_count += hættemåge_næb
    husskade_count += husskade_næb
    hvid_vipstjert_count += hvid_vipstjert_næb
    klippedue_count += klippedue_næb
    knopsvane_count += knopsvane_næb
    musvit_count += musvit_næb
    ringdue_count += ringdue_næb
    skarv_count += skarv_næb
    skovspurv_count += skovspurv_næb
    solsort_count += solsort_næb
    sølvmåge_count += sølvmåge_næb
    
    print(blåmejse_count)
    print(blishøne_count)
    print(bogfinke_count)
    print(fasan_count)
    print(fiskehejre_count)
    print(gråand_count)
    print(grågås_count)
    print(gråkrage_count)
    print(hættemåge_count)
    print(husskade_count)
    print(hvid_vipstjert_count)
    print(klippedue_count)
    print(knopsvane_count)
    print(musvit_count)
    print(ringdue_count)
    print(skarv_count)
    print(skovspurv_count)
    print(solsort_count)
    print(sølvmåge_count)
    

    print("Hvor stor er fuglen?")
    print("Lille, Mellem, Stor.")
    størrelse = input("")
    if størrelse == "exit":
        break
    count, blåmejse_størrelse, blishøne_størrelse, bogfinke_størrelse, fasan_størrelse, fiskehejre_størrelse, gråand_størrelse, grågås_størrelse, gråkrage_størrelse, hættemåge_størrelse, husskade_størrelse, hvid_vipstjert_størrelse, klippedue_størrelse, knopsvane_størrelse, musvit_størrelse, ringdue_størrelse, skarv_størrelse, skovspurv_størrelse, solsort_størrelse, sølvmåge_størrelse = fugle_counter(størrelse, "størrelse")
    blåmejse_count += blåmejse_størrelse
    blishøne_count += blishøne_størrelse
    bogfinke_count += bogfinke_størrelse
    fasan_count += fasan_størrelse
    fiskehejre_count += fiskehejre_størrelse
    gråand_count += gråand_størrelse
    grågås_count += grågås_størrelse
    gråkrage_count += gråkrage_størrelse
    hættemåge_count += hættemåge_størrelse
    husskade_count += husskade_størrelse
    hvid_vipstjert_count += hvid_vipstjert_størrelse
    klippedue_count += klippedue_størrelse
    knopsvane_count += knopsvane_størrelse
    musvit_count += musvit_størrelse
    ringdue_count += ringdue_størrelse
    skarv_count += skarv_størrelse
    skovspurv_count += skovspurv_størrelse
    solsort_count += solsort_størrelse
    sølvmåge_count += sølvmåge_størrelse
    
    print(blåmejse_count)
    print(blishøne_count)
    print(bogfinke_count)
    print(fasan_count)
    print(fiskehejre_count)
    print(gråand_count)
    print(grågås_count)
    print(gråkrage_count)
    print(hættemåge_count)
    print(husskade_count)
    print(hvid_vipstjert_count)
    print(klippedue_count)
    print(knopsvane_count)
    print(musvit_count)
    print(ringdue_count)
    print(skarv_count)
    print(skovspurv_count)
    print(solsort_count)
    print(sølvmåge_count)


    print("Hvilken farver har den?")
    print("Blå, Gul, Sort, Hvid, Rød, Blå, Gul, Brun, Grå")
    for i in farver:
        print(farver)
        farve = input("")
        if farve == farver:
            continue
        elif farve == "Det var det":
            break

    

    #while True:
    #    print("Hvilke farver har fuglen?")
    #    print("Blå, Gul, Sort, Hvid, Rød, Blå, Gul, Brun, Grå")
    #    farve = input("")
    #    for i in farver():
    #        if i == farve:


>>>>>>> 6d300aa6c93325956925a694bf4f6bdd874974ae
