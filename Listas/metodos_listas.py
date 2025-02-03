# MÉTODO PARA PULAR UMA LINHA
def pular_linha():
    print("\n")


# ADICIONA ITENS NA LISTA
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])
print("Adicionando items na lista")
print(lista) # [1, "Python", [40, 30, 20]]
pular_linha()

# LIMPA A LISTA
print("Valor da Lista Original")
lista = [1, "Python", [40,30,20]]
print(lista) # [1, "Python", [40,30,20]]
lista.clear()
pular_linha()
print("Limpando a Lista")
print(lista) # []
pular_linha()

# COPIA A LISTA SEM MODIFICAR-LÁ
lista = [1, "Python", [40,30,20]]
lista_2 = lista.copy()
print("Copiando a lista em outra instância")
print(lista)
lista_2[0] = 2 
pular_linha()

print("Lista Original - lista")
print(lista)
pular_linha()

print("Lista Modificada - lista_2")
print(lista_2)
pular_linha()

# CONTAR QUANTAS VEZES UM OBJETO APARECE NA LISTA

cores = ["vermelho", "azul", "verde", "azul"]

contagem_vermelho = cores.count("vermelho") # 1
contagem_azul = cores.count("azul") # 2
contagem_verde = cores.count("verde") # 1

vermelho_vezes = "vezes" if contagem_vermelho > 1 else "vez"
azul_vezes = "vezes" if contagem_azul > 1 else "vez"
verde_vezes = "vezes" if contagem_verde > 1 else "vez"

print(f"Vermelho: {contagem_vermelho} {vermelho_vezes}. \nAzul: {contagem_azul} {azul_vezes}. \nVerde: {contagem_verde} {verde_vezes}.")
pular_linha()

# EXTENDER UMA LISTA
linguagens = ["python", "js", "c"]
print("Lista Anterior")
print(linguagens)
pular_linha()

linguagens.extend(["java", "csharp"])
print("Lista Extendida")
print(linguagens) # ["python", "js", "c", "java", "csharp"]
pular_linha()

# RETORNA O INDICE DA PRIMEIRA OCORRÊNCIA DE UM OBJETO
linguagens = ["python", "js", "c", "java", "csharp"]

index_java = linguagens.index("java") # 3
index_python = linguagens.index("python") # 0

print(f"Indice Java: {index_java} \nIndice Python: {index_python}")
pular_linha()


# REMOVE O ULTIMO ITEM DA LISTA (OU O INDICE SE FOR PASSADO COMO PARÂMETRO)
linguagens = ["python", "js", "c", "java", "csharp"]

print("Lista Completa")
print(linguagens)
pular_linha()

linguagens.pop() # csharp
print("csharp removido!")
print(linguagens)
pular_linha()

linguagens.pop() # java
print("java removido!")
print(linguagens)
pular_linha()

linguagens.pop() # c
print("c removido!")
print(linguagens)
pular_linha()

linguagens.pop(0) # csharp
print("python removido!")
print(linguagens)
pular_linha()

# REMOVE UM OBJETO PASSANDO ELE COMO PARÂMETRO
linguagens = ["python", "js", "c", "java","csharp"]
print("Lista Completa!")
print(linguagens)
pular_linha()

linguagens.remove("c")
print("Removendo c...")
print(linguagens)
pular_linha()

# REVERTER LISTA
linguagens = ["python", "js", "c", "java", "csharp"]
print("Lista Completa!")
print(linguagens)
pular_linha()

linguagens.reverse()
print("Revertendo Lista")
print(linguagens) # ['csharp', 'java', 'c', 'js', 'python']
pular_linha()


# ORDENANDO LISTAS
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()
print("Ordenando Lista") # ['c', 'csharp', 'java', 'js', 'python']
print(linguagens)
pular_linha()

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)
print("Ordenando Lista em ordem reversa")
print(linguagens) # ['python', 'js', 'java', 'csharp', 'c']
pular_linha()

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))
print("Ordenando Lista por Tamanho da Palavra")
print(linguagens) # ['c', 'js', 'java', 'python', 'csharp']
pular_linha()

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)
print("Ordenando Lista em ordem reversa por Tamanho da Palavra")
print(linguagens) # ['python', 'csharp', 'java', 'js', 'c']
pular_linha()

# CAPTURA O TAMANHO DE UM OBJETO
linguagens = ["python", "js", "c", "java", "csharp"]
tamanho_linguagens = len(linguagens)
print(f"O tamanho do objeto é: {tamanho_linguagens}") # O tamanho do objeto é: 5
pular_linha()

# METODO BUILT-IN PARA ORDENAR LISTAS
linguagens = ["python", "js", "c", "java", "csharp"]
lista_crescente = sorted(linguagens, key=lambda x: len(x))
print("Lista ordenada em ordem crescente");
print(lista_crescente)
pular_linha()

lista_decrescente = sorted(linguagens, key=lambda x: len(x), reverse=True)
print("Lista ordenada em ordem decrescente")
print(lista_decrescente)
pular_linha()

lista_ordem_alfabetica = sorted(linguagens)
print("Ordena por ordem alfabética")
print(lista_ordem_alfabetica)
pular_linha()
