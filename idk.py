#Vytvořte funkci, která dokáže seřadit čísla od 
#nejmenšiho k největšímu v poli
#následně výsledek printnite

pole1 = [3,2,1,5,4]

def seradit(pole1):
    x = sorted(pole1)
    print(x)
print(seradit(pole1))