# Obtenha o nome do usuario
# Obteenha a idade do usuario
# Registre de forma automatica a data que a conta foi criada
# Para cada funcionario novo que é registrado na empresa ele recebe um dos seguintes cartões, que é sorteado de forma aleatória / cartoes = ['R$ 50,00', 'R$ 250,00', 'R$ 120,00']

import random
from datetime import datetime

# Aqui é o nome
print("Sejá bem vindo a Jeff Corporation")
nome_inteiro = str(input("Digite seu nome inteiro: "))


# Aqui é a idade
idade = int(input("Digite a sua idade: "))

dia_de_niver = int(input('Qual é o dia do seu aniversario: '))

mes_de_niver = int(input('Qual é o mês de aniversario: '))

ano_de_niver = int(input('Qual é o ano de aniversario: '))

# Marcar hora que foi feita o cadastro
data = datetime.now()

horario = data.strftime("%H:%M:%S")

diario = data.strftime("%d/%m/%Y")


# Cartões
lista_cartoes = ["R$ 50,00", "R$ 250,00", "R$ 120,00"]

card = random.choice(lista_cartoes)


# Data de aniversario

diario2 = data.strftime("%Y")
diario2 = int(diario2)
niver = diario2 - idade

diario3 = data.strftime("%d")

print(card)

print(f'{dia_de_niver}/{mes_de_niver}/{ano_de_niver}')

print(niver)


print(diario)

print("Hora ", horario)
print(" ")



# # Módulo 2
print(f'Olá {nome_inteiro} seu registro foi concluído com sucesso no dia {diario3}. parabéns, houve um sorteio e você ganhou o cartão de compras no valor de {card}')