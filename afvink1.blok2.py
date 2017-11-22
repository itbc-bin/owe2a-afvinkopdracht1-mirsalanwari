def main():
        try:
                bestandnaam = (input("wat is de naam van het bestand dat u wilt onderzoeken?: "))+".fa"
                bestand = open(bestandnaam)# Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
        except FileNotFoundError:
                print("Het bestand", bestandnaam, "staat niet in de map, kies een ander bestand of zet het bestand in de goede map")
                main()
        try:
                bestandnaam_2 = (input("wat is de naam van het bestand met de enzymen?: "))+".txt"
                bestand_2 = open(bestandnaam_2)
        except FileNotFoundError:
                print("Het bestand",bestandnaam_2, " staat niet in de map, kies een ander bestand of zet het bestand in de goede map")
                main()
       
        all_inlijst = lees_inhoud(bestand)

        index1,index2,totaalACGT_1,totaalACGT_2,lengte_index1,lengte_index2 = is_dna(all_inlijst,bestand_2)
        knipt(bestand_2,all_inlijst,index1,index2,totaalACGT_1,totaalACGT_2,lengte_index1,lengte_index2)


 
    

def lees_inhoud(bestand):

    seq_lijst = []
    header_lijst = []
    all_inlijst = []
    
    regel = bestand.readline()
    
    while(regel != ""):                         # als regel niet leeg is

        if regel[0] == ">":                     # als regel een > bevat is het een header
            header_lijst.append(regel)
            seq = ""                            # seq is leeg omdat er alleen headers worden toegevoegd
            regel = bestand.readline()
            
        while regel != "" and regel[0] != ">":  # als regel niet leeg is en geen > bevat is het een seq
            seq += regel.strip()                # seq wordt gevuld 
            regel = bestand.readline()

        seq_lijst.append(seq)                   # inhoud van seq wordt gekoppeld aan list
        
    all_inlijst.append(seq_lijst)               # inhoud wordt gekoppeld aan totale list
    all_inlijst.append(header_lijst)            # inhoud wordt gekoppeld aan totale list
   
    
    return all_inlijst
        
            
        

def is_dna(all_inlijst, bestand_2):
    index1 = ','.join(all_inlijst[0])           #list omzetten naar string
    print("index1:", index1)
    aantalA = index1.count('A')
    print(" aantal A:", aantalA)
    aantalC = index1.count('C')
    print(" aantal C:", aantalC)
    aantalG = index1.count('G')
    print(" aantal G:", aantalG)
    aantalT = index1.count('T')
    print(" aantal T:", aantalT)
    lengte_index1 = int(len(index1))
    print(" lengte index1:", lengte_index1)
    totaalACGT_1 = int(aantalA + aantalC + aantalG + aantalT)
    print(" totaal ACGT in element[0]:", totaalACGT_1)
    print(150*'-')

    index2 = '.'.join(all_inlijst[1])           # list omzetten naar string
    print("index 2:", index2)
    aantalA = index2.count('A')
    print(" aantal A:", aantalA)
    aantalC = index2.count('C')
    print(" aantal C:", aantalC)
    aantalG = index2.count('G')
    print(" aantal G:", aantalG)
    aantalT = index2.count('T')
    print(" aantal T:", aantalT)
    totaalACGT_2 = int(aantalA + aantalC + aantalG + aantalT)
    print(" totaal ACGT in element[1]:", totaalACGT_2)
    lengte_index2 = int(len(index2))
    print(" lengte index 2:", lengte_index2)
    print(150*'-')
    
    if totaalACGT_1 == lengte_index1:
            print("index 1 is de sequentie van een DNA")
            print("index 2 is een header")
             
    else:
            print("index 2 is de sequentie van een DNA")
            print("index 2 is een header")
    print(150*'-')
           
        


    return index1,index2,totaalACGT_1,totaalACGT_2,lengte_index1,lengte_index2



                
def knipt(bestand_2,all_inlijst,index1,index2,totaalACGT_1,totaalACGT_2,lengte_index1,lengte_index2):

        zoekwoord = input(" welk enzym wil je onderzoeken? ")

        
                
        while totaalACGT_1 == lengte_index1:
                
                for line in bestand_2:
                        naam, seq = line.split(" ")
                        seq = seq.strip().replace("^","")
                        enzym1= index1.find(seq)
                        enzym1_1 = index1.find(zoekwoord)
                        
                        if zoekwoord == naam:
                                if enzym1 >= 0:
                                        totaalACGT_1 = totaalACGT_1 + 1
                                        print(zoekwoord,"knipt in de sequentie")
                                        
                                else:
                                        totaalACGT_1 = totaalACGT_1 + 1
                                        print(zoekwoord, " knipt niet in de sequentie ")


                                        
        while totaalACGT_2 == lengte_index2:
                for line in bestand_2:
                        naam, seq = line.split(" ")
                        seq = seq.strip().replace("^","")
                        enzym2= index2.find(seq)
                        
                        if zoekwoord == naam:
                                if enzym2 >= 0:
                                        totaalACGT_2 = totaalACGT_2 + 1
                                        print(zoekwoord,"knipt in de sequentie")
                                        
                                else:
                                        totaalACGT_2 = totaalACGT_2 + 1
                                        print(zoekwoord, " knipt niet in de sequentie ")


      

            

                
    

main()
                
            



    




   
   




