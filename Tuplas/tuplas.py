# MÉTODO PARA PULAR LINHA
def pular_linha():
    print("\n")

# DECLARANDO TUPLAS
frutas = ("laranja", "pera", "uva",)
letras = tuple("python")
numeros = tuple([1, 2, 3, 4])
pais = ("Brasil",)


# IMPRIMINDO TUPLAS
frutas = ("maçã", "laranja", "uva", "pera",)
indice_0 = frutas[0]
indice_2 = frutas[2]

pular_linha()
print("----IMPRIMINDO TUPLAS----")
print(indice_0) # maçã
print(indice_2) # uva
pular_linha()

# INDICES NEGATIVOS
frutas = ("maçã", "laranja", "uva", "pera",)

print("----INDICES NEGATIVOS----")
print(frutas[-1]) # pera
print(frutas[-3]) # laranja
pular_linha()


# TUPLAS ANINHADAS
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

matriz_1 = matriz[0] 
matriz_2 = matriz[0][0] # 1
matriz_3 = matriz[0][-1] # 2
matriz_4 = matriz[-1][-1] # "c"

print("----TUPLAS ANINHADAS----")
print(matriz_1) # (1, "a", 2)
print(matriz_2) # 1
print(matriz_3) # 2
print(matriz_4) # "c"
pular_linha()

# FATIAMENTO
tupla = ("p" ,"y" ,"t" ,"h" ,"o" ,"n")

print("----FATIAMENTO----")
print(tupla[2:]) # ("t","h","o","n")
print(tupla [:2]) # ("p","y")
print(tupla [1:3]) # ("y","t")
print(tupla [0:3:2]) # ("p","t")
print(tupla [::]) # ("p" ,"y" ,"t" ,"h" ,"o" ,"n")
print(tupla[::-1]) #
pular_linha()

# ITERANDO TUPLAS
carros = ("gol", "celta", "palio",)
print("----ITERANDO TUPLAS----")

for carro in carros:
    print(carro)
pular_linha()

# ENUMERANDO TUPLAS
carros = ("gol", "celta", "palio",)
print("----ENUMERANDO TUPLAS----")

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
pular_linha()

# MÉTODO COUNT
cores = ("vermelho", "azul", "verde", "azul",)
cores_vermelho = cores.count("vermelho") # 1
cores_azul = cores.count("azul") # 2
cores_verde = cores.count("verde") #1

def numero_vezes(cor):
    vezes = "vezes" if cor > 1 else "vez"
    return vezes

print("----MÉTODO COUNT----")
print(f"A cor vermelha aparece {cores_vermelho} {numero_vezes(cores_vermelho)}")
print(f"A cor azul aparece {cores_azul} {numero_vezes(cores_azul)}")
print(f"A cor verde aparece {cores_verde} {numero_vezes(cores_verde)}")
pular_linha()


# MÉTODO INDEX
linguagens = ("python", "js", "c", "java", "csharp",)

indice_3 = linguagens.index("java") # 3
indice_0 = linguagens.index("python") # 0

print("----MÉTODO INDEX----")
print(indice_3)
print(indice_0)
pular_linha()

# MÉTODO LEN
tupla = ("banana", "maça", "uva")

print("----MÉTODO LEN----")
print(len(tupla)) # 3
pular_linha()
