texto = input("Informe um Texto: ")
VOGAIS =  "AEIOU"

for letra in texto:
    if(letra.upper() in VOGAIS):
        print(letra, end="")

print()