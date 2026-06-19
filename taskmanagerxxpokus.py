
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:37:04 2026

@author: zuzah
"""

ukoly={}

spravce_ukolu = "Správce úkolů - Hlavní menu\n"
spravce_ukolu += "1. Přidat nový úkol\n"
spravce_ukolu +="2. Zobrazit všechny úkoly\n"
spravce_ukolu +="3. Odstranit úkol\n"
spravce_ukolu +="4. Konec programu\n"
spravce_ukolu +="Vyberte možnost (1-4):\n"

# print(spravce_ukolu)

def pridat_ukol():
    
    while True: 
        nazev=input("Zadejte název úkolu(max 40 znaků): ")
        if len(nazev)>40:
            print("zadali jste moc dlouhý název")
            continue 
        
        popis=input("Zadejte popis úkolu: ")
    
        if nazev == "" or popis == "":
            print("Zadali jste prázdný vstup, zkuste to znovu.\n")
            continue
        break
    
    while True:
        print("Chcete opravdu přidat úkol: \'" + nazev + "\'")
        print()
        
        volba=input("přidat úkol=ano,\n nechci přidat a zpět do hlavního menu=ne:\n ")
        print()
        
        if volba == "ne":
            return 
        if volba =="ano":
            ukoly[nazev]= popis #ulozeni, popisu do promenné ukoly pod kličem nazev - [klič]=hodnota
            print("úkol \'" + nazev + "\' byl přidán")
            print()
            break 
        else: 
            print("zadali jste neplatnou hodnotu, zkusteto znovu")
        
    
def zobrazit_ukoly():
   # print("Zobrazit všchny úkoly: \n\n")
   print("seznam úkolů: ")
   cislovany_seznam = {}
   i = 1
   # projde pary nazev - popis ve slovniku ukoly .items --> bere dvojice klic hodnota
   for nazev, popis in ukoly.items():
       print(f"{i}. {nazev} - {popis}")
       cislovany_seznam[i] = nazev #ulození, nazvu ukolu do cislovaneho seznamu pod klicem i
       i += 1
       
   if len(cislovany_seznam) == 0:
       print("Žádné úkoly")
           
        
   print() #prazdny radek
   
   return cislovany_seznam
   
    
def odstranit_ukol():
    # print("Odstranit úkol: \n\n")
    
    while True:
        #vysat seznan ukolu {cislo - nazev}
        seznam_ukolu = zobrazit_ukoly()
        
        #rekne si o cislo, ktere chceme odstranit
        odstranit_polozku = input("Zadejte číslo úkolu, který chcete odstranit(0=zpět): ")
        
        #odstraneni ukolu
        try:
           odstranit_polozku = int(odstranit_polozku)
           
       #zadaní neplatné hodnoty
        except ValueError:
            print("Nesprávná hodnota, zadej číslo")
            continue 
        if odstranit_polozku not in seznam_ukolu:
            print("Zadané číslo neexistuje v seznamu, zvolte jiné")
            continue
        break
        
    #zadani nula bude zpet
    if odstranit_polozku == 0: 
        return 
      
    
   #cislo se zmeni zpet na odpoviajici nazev ukolu
    nazev_ukolu = seznam_ukolu[odstranit_polozku]
    ukoly.pop(nazev_ukolu)
    print("úkol \'" +nazev_ukolu+"\' byl odstraněn.")
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




