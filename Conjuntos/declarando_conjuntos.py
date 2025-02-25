# FUNÇÃO PARA PULAR LINHA
def pular_linha ():
    print("\n")

pular_linha()
print("----------MÉTODO SET----------")
pular_linha()

# MÉTODO SET
lista_1 = set([1, 2, 3, 1, 3, 4])
lista_2 = set("abacaxi")
lista_3 = set(("palio", "gol", "celta", "palio"))

print(lista_1)
print(lista_2)
print(lista_3)
pular_linha()

# CONJUNTOS
linguagens = {"Python", "Java", "Python"}
pular_linha()

print("----------CONJUNTOS----------")
pular_linha()
print(linguagens)
pular_linha()

#  PARA ACESSAR UM CONJUNTO, É NECESSÁRIO CONVERTER-LÔ PARA UMA LISTA
numeros = {1, 2, 3, 2}
numeros = list(numeros)

print("----------CONVERSÃO CONJUNTOS PARA LISTA----------")
pular_linha()
print(numeros[0])
pular_linha()


# ITERAR CONJUNTOS
print("----------ITERAÇÃO DE CONJUNTOS----------")
pular_linha()
carros = {"gol", "celta", "palio"}
pular_linha()

for carro in carros:
    print(carro)

pular_linha()

# FUNÇÃO ENUMERATE
print("----------FUNÇÃO ENUMERATE----------")
pular_linha()

for indice, carro in enumerate(carros):
    print(f"Indice {indice}: {carro}")

pular_linha()

# UNIÃO DE CONJUNTOS
conjunto_a = {1,2}
conjunto_b = {3,4}

print("----------UNIÃO DE CONJUNTOS----------")
pular_linha()

print(conjunto_a.union(conjunto_b))
pular_linha()

print("----------INTERCESSÃO DE CONJUNTOS----------")
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
pular_linha()

print(conjunto_a.intersection(conjunto_b))
pular_linha()

print("----------DIFERENÇA DE CONJUNTOS----------")
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
pular_linha()

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
pular_linha()

print("----------DIFERENÇA DE SIMÉTRICA----------")
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
pular_linha()

print(conjunto_a.symmetric_difference(conjunto_b))
pular_linha()

print("----------SUBCONJUNTO PERTENCE AO CONJUNTO----------")
conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}
pular_linha()

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))
pular_linha()

print("----------SUBCONJUNTO NÃO PERTENCE AO CONJUNTO----------")
conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}
pular_linha()

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))
pular_linha()

print("----------OPERAÇÃO DE CONJUNTO DISJUNTO | CONJUNTOS QUE NÃO SE TOCAM----------")
conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1, 0}
pular_linha()

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))
pular_linha()

print("----------ADICIONA UM NUMERO NO CONJUNTO----------")
pular_linha()

sorteio = {1,23}
sorteio.add(25)
print(sorteio)
sorteio.add(42)
print(sorteio)
sorteio.add(25)
print(sorteio)

pular_linha()