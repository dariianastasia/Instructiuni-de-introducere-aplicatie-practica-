"""Se introduc de la tastatura trei cifre.Afisati pe sceeasi linie 5 numere cu aceste cifre luate o singura data."""
a=int(input("Introdu primul numar:"))
b=int(input("Introdu al doilea numar:"))
c=int(input("Introdu al treilea numar"))
print(str(a)+str(b)+str(c),str(a)+str(c)+str(b), str(b)+str(a)+str(c),str(b)+str(c)+str(a),str(c)+str(a)+str(b))