import random

duzina_sifre= int(input("Unesi duzinu sifre:"))

velika_slova = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
mala_slova = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
brojevi = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specijalni_karakteri = ['@', '#', '$', '=', ':', '?', '.', '/', '|', '~', '>', '*', '<']
kombinovana_lista = velika_slova + mala_slova + brojevi + specijalni_karakteri

sifra= "".join(random.sample(kombinovana_lista, duzina_sifre))

print(sifra)