# Função para pular linha
def pular_linha():
    print("\n")

# CRIANDO LISTAS
frutas = ["Laranja", "Maçã", "Uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("Python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

# ACESSANDO INDICES DAS LISTAS
frutas = ["Laranja", "Maçã", "Uva", "Pera"]
pular_linha();

print(frutas[0]) # Saída: Laranja
print(frutas[2]) # Saída: Uva
print(frutas[-1]) # Saída: Pera
print(frutas[-3]) # Saída: Maça
pular_linha()

# MATRIZES
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0]) # Saída: [1, "a", 2]
print(matriz[0][0]) #Saída: 1
print(matriz[0][1]) #Saída: 2
print(matriz[-1][-1]) #Saída: c
pular_linha()

# FATIAMENTO
lista = ["p", "y","t","h","o","n"]
print(lista[2:]) #["t","h","o","n"]
print(lista[:2]) # ["p", "y"]
print(lista[1:3]) # ["y","t"]
print(lista[0:3:2]) # ["p", "t"]
print(lista[::]) # ["p", "y","t","h","o","n"]
print(lista[::-1]) # ['n', 'o', 'h', 't', 'y', 'p']
pular_linha()

# ITERAR LISTAS
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)
pular_linha()

# ENUMERATE
carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: carro")
pular_linha()

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

# COMPREENSÃO DE LISTAS - CAPTURANDO LISTA DE NUMEROS PARES

# EXEMPLO 1
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero) # Adiciona os numeros na lista pares
print(pares)

# EXEMPLO 2
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
pular_linha()

## MODIFICANDO VALORES
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
print(quadrado)

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)
