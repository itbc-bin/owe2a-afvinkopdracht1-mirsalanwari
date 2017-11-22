def main():


   
    x = input(" wilt u uw bestand analyseren?(y/n)")
    print(80* ":),")
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
                    print("Sequentie is geen DNA. Er is iets fout gegaan.")
                    
        print("Bedankt voor uw tijd!")
    else:
        print(" het programma wordt gestopt, fijne dag/avond ")
        
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
        print("het  bestand is geen fasta bestand begin opnieuw")
        main()
    except FileNotFoundError:
        print("Het bestand staat niet in de map of geef een andere naam op.")
        main()
        
        
    

def is_dna(seq):
    try:
        dna = False
        a = seq.count("A")
        t = seq.count("T")
        c = seq.count("C")
        g = seq.count("G")
        total = a + t + c + g
        if total == len(seq):
            dna = True
        else:
            raise IndexError
            
        return dna
    except IndexError:
        print("het bestand is geen DNA voor een bestand in dat DNA is")
    

def knipt(alpaca_seq):
        bestand_1 = (input ("Geef naam van bestand met de knipenzymen op: ")) + ".txt"
        bestand = open(bestand_1)
        for line in bestand:
            naam, seq = line.split(" ")
            seq = seq.strip().replace("^","")
            if seq in alpaca_seq:
                print(naam, "knipt in sequentie")

    
    


main()
