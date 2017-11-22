def main():

    try:

        x = input(" wilt u uw bestand analyseren?(y/n)")
        print(80* "-")
        if x == "y":
            bestand = (input("Geef naam van het bestand van de sequenties: "))+".fa"
            headers, seqs = lees_inhoud(bestand)
            
            zoekwoord = input("Geef een zoekwoord op: ")

            for i in range(len(headers)):
                if zoekwoord in headers[i]:
                    print("Header:",headers[i])
                    check_is_dna = is_dna(seqs[i])
                    if check_is_dna:
                        print("Sequentie is DNA")
                        knipt(seqs[i])
                    else:
                        raise IndexError
                else:
                    raise NameError
                        
            print("Bedankt voor uw tijd!")
        else:
            raise TypeError
            
    except TypeError:
        print(" U heeft waarschijnlijk een typefout gemaakt of op ""n"" gedrukt voert u alstublieft een geldig teken in als u het programma toch door wilt laten draaien ")
        main()
    except NameError:
        print(" U heeft een ongedlig zoekwoord ingevoerd of het woord staat niet in het bestand" ,bestand, "voer alstublieft een nieuw zoekwoord in")
        main()
    except IndexError:
        print(" Het bestand", bestand, " is geen DNA voer een DNA sequentie in")
        main()
        
        
        
            
def lees_inhoud(bestand):
    
    try:
    
        bestand = open(bestand)   
    
    
        headers = []
        seqs = []
        seq = ""
        for line in bestand:
            line=line.strip()
            if ">" in line:
                if seq != "":
                    seqs.append(seq)
                    seq = ""
                headers.append(line)
            else:
                seq += line.strip()
        seqs.append(seq)

        if ">" in headers[0]:
            return headers, seqs
        else:
            raise IndexError

    except IndexError:
        print("het  bestand",bestand, " is geen fasta bestand begin opnieuw")
        main()
    except FileNotFoundError:
        print("Het", bestand," staat niet in de map of geef een andere naam op.")
        main
        
        
    

def is_dna(seq):
    dna = False
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a + t + c + g
    if total == len(seq):
        dna = True
    return dna

def knipt(alpaca_seq):
    try:
        bestand_1 = (input ("Geef naam van bestand met de knipenzymen op: ")) + ".txt"
        bestand = open(bestand_1)
        for line in bestand:
            naam, seq = line.split(" ")
            seq = seq.strip().replace("^","")
            if ">" in line:
                raise IndexError
            else:
                if seq in alpaca_seq:
                    print(naam, "knipt in sequentie")
            
            
    except FileNotFoundError:
        print("Het bestand",bestand_1," staat niet in de map of geef een andere naam op.")
        knipt(alpaca_seq)
    except IndexError:
        print(" het bestand is geen geldige geldig enzym bestand vooer een nieuw bestand in")
        knipt(alpaca_seq)
        
        
        
    

    
    


main()
