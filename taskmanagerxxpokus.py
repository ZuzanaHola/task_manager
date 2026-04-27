
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:37:04 2026

@author: zuzah
"""


ukoly=[]

spravce_ukolu = "Správce úkolů - Hlavní menu\n"
spravce_ukolu += "1. Přidat nový úkol\n"
spravce_ukolu +="2. Zobrazit všechny úkoly\n"
spravce_ukolu +="3. Odstranit úkol\n"
spravce_ukolu +="4. Konec programu\n"
spravce_ukolu +="Vyberte možnost (1-4):\n"

# print(spravce_ukolu)

def pridat_ukol():
    #print("Přidat nový úkol: \n\n")
    nazev=input("Zadejte název úkolu: ")
    popis=input("Zadejte popis úkolu: ")
    
    if nazev == "" or popis == "":
        print("Zadali jste prázdný vstup, zkuste to znovu.\n")
        return pridat_ukol()
    
    ukoly.append([nazev, popis])
    print("úkol \'" + nazev + "\' byl přidán")
    print()
        
    
def zobrazit_ukoly():
   # print("Zobrazit všchny úkoly: \n\n")
   print("seznam úkolů: ")
   for index, ukol in enumerate(ukoly):  
       print (str(index+1) + ". ",ukol[0] + " - " + ukol[1])
   print()
    
    
def odstranit_ukol():
    # print("Odstranit úkol: \n\n")
    
    while True:
        zobrazit_ukoly()
        odstranit_polozku=input("Zadej číslo úkolu, který chcete odstranit: ")
           
        try:
           odstranit_polozku=int(odstranit_polozku)
           break
        except ValueError:
            print("Nesprávná hodnota, zadej číslo")
    
    odstraneno=ukoly.pop(odstranit_polozku-1)
    print("úkol \'" +odstraneno[0]+"\' byl odstraněn.")
    print()


while True:

    volba = input(spravce_ukolu)
    
    if volba in ("1", "1."):
        pridat_ukol()
        continue
    
    elif volba in ("2", "2."):
        zobrazit_ukoly()
        continue
    
    elif volba in ("3", "3."):
       odstranit_ukol()
       continue
   
    elif volba in ("4", "4."):
       print ("Konec programu\n \n")
       break
   
    else:
       print ("Zadali jste nesprávný příkaz\n\n")
       continue
   
    
   
    print("\n\nTOTO BY SE NEMĚLO NIKDY VYPSAT\n\n")




