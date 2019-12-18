#Diccionario de palabras de Ingles a Español
# John Alvarez

Dicc_espanol_ingles = { "ciudad" : "city", "hermano" : "brother","arbol" : "tree", "avion" : "airplane", "zapatos" : "shoes", "nariz" : "nose", "navidad" : "christmas", "playa" : "beach", "paraiso" : "paradise", "serpiente" : "snake"}

print("\n Elige una de las palabras en la lista a traducir a ingles:")
Palabras = ["ciudad","hermano","arbol","avion","zapatos","nariz","navidad","playa","paraiso","serpiente"]
print(Palabras)

entrada = input ("\n Ingrese la palabra que desea traducir a ingles:")

if   entrada == Palabras [0]: print ("\n  ciudad traducido a ingles es:", Dicc_espanol_ingles.get("ciudad"))
elif entrada == Palabras [1]: print ("\n  hermano traducido a ingles es:", Dicc_espanol_ingles.get("hermano"))
elif entrada == Palabras [2]: print ("\n  arbol traducido a ingles es:", Dicc_espanol_ingles.get("arbol"))
elif entrada == Palabras [3]: print ("\n  avion traducido a ingles es:", Dicc_espanol_ingles.get("avion"))
elif entrada == Palabras [4]: print ("\n  zapatos traducido a ingles es:", Dicc_espanol_ingles.get("zapatos"))
elif entrada == Palabras [5]: print ("\n  nariz traducido a ingles es:", Dicc_espanol_ingles.get("nariz"))
elif entrada == Palabras [6]: print ("\n  navidad traducido a ingles es:", Dicc_espanol_ingles.get("navidad"))
elif entrada == Palabras [7]: print ("\n  playa traducido a ingles es:", Dicc_espanol_ingles.get("playa"))
elif entrada == Palabras [8]: print ("\n  paraiso traducido a ingles es:", Dicc_espanol_ingles.get("paraiso"))
elif entrada == Palabras [9]: print ("\n  serpiente traducido a ingles es:", Dicc_espanol_ingles.get("serpiente"))


else: print("\n Esta palabra aun no esta disponible")
