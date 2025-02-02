# Operadores de Identidade verificam se uma variavel ocupa o mesmo espaço na memoria
# e retorna True se a variável tem o mesmo espaço

curso = "Curso de Python"
nome_curso = curso;
saldo, limite = 200, 200

print(curso is nome_curso) # Retorna True
print(curso is not nome_curso) # Retorna False
print(saldo is limite) # Retorna True