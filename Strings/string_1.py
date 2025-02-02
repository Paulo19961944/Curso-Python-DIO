nome = "pAUlo"

print(nome.lower()) # Saída: paulo
print(nome.upper()) # Saída: PAULO
print(nome.title()) # Saída: Paulo


texto = "    Olá Mundo         "

print(texto + ".") # Texto Original
print(texto.strip() + ".") # Retira os Espaços de Ambos os Lados
print(texto.rstrip() + ".") # Retira os Espaços a Direita
print(texto.lstrip() + ".") # Retira os Espaços a Esquerda

menu = "Python"

print("####" + menu + "####") # Texto com Cerquilhas
print(menu.center(14)) # Alinha o Texto ao Centro
print(menu.center(14, "#")) # Alinha o Texto ao Centro com as Cerquilhas
print("P.y.t.h.o.n") # Texto com Pontos
print(".".join(menu)) # Une um Ponto a cada letra