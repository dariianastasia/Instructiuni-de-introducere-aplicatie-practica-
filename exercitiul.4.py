"""Un brad este inpodobit cu globulete albe, rosii si albastre.Numarul globuletelor albe se citeste de la tastatura.Cite globulete are bradutul, stiind ca numarul deglobulete rosii este cu 3 mai mare decit numarul globuletelor albe, iar globuletele albastre sunt cu 2 mai putini decit totalul celor albe si rosii."""
ga=int(input("Introduce numarul globuletelor albe:"))
gr=3+ga
gal=(ga+gr)-2
tot=ga+gr+gal
print("In total sunt",tot,"dlobulete")