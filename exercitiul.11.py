"""Mariuca tine evidenta iepurilor din crescatorie.Ea isi noteaza cati iepuri sunt la inceputul fiecarei luni, citi su murit si citi s-au ascut in cursul fiecarei uni.Puteti sa realizati un program care, primind aceste date,sa afiseze la sfirsitul fiecarei luni citi iepuri sunt in crescatoare."""
l=int(input("Numarul de iepurilor initiali: "))
m=int(input("Numarul iepurilor morti:"))
n=int(input("Numaru; iepurilor nascuti:"))
tot=l-m+n
print("La sfirsitul acestei luni increscatoare sunt",tot,"iepuri")