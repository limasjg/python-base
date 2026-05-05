# ESQUELETO DO CURSO

#1 - Saida de Dados
# nome = "Luke"
# print(f"O nome do gato é {nome}")

# num = 12.5263
# print(f"O valor do número é {num:.2f}")

#2 - Variaveis
# nome = "João"
# idade = 33
# peso = 65.23
# vivo = True

#3 Type casting
# idade = input("qual a sua idade? ")
# # idade = int(input("qual a sua idade? ")) -# Converte no input

# # idade = int(idade) # Converte depois
# print(type(idade))

# print(f"Sua idade é {idade}")

#4 Operações Aritimetricas
# div = 5 / 2 # Divisão Float 2.5
# div2 = 5 // 2 # Divisão int 2 

# resto = 5 % 2

# expo = 5 ** 2 # Int 

# print(type(resto))

# print(resto)

#5 struturas condicionais:
# num1 = 100
# num2 = 200

# Bloco condicional único, usamos o elif se queremos adicionar outras condições antes do else (condições gerais que não o if)
# if num1 > num2:
#     print(f"Numero 1 {num1} é maior que o número 2 {num2}")
# elif num1 < num2:
#     print(f"Numero 2 {num2} é maior que o número 1 {num1}")
# else:
#     print(f"Numero 2 {num2} éigual o número 1 {num1}")

#Usamos mais de um IF quando queremos testar mais de um bloco condicional:
# fruta = "maçã"
# cor = "vermelha"

# if fruta == "maçã":
#     print("A fruta é maça")
# if cor == "vermelha":
#     print("A cor é vermelha")
# else:
#     print("Não tem fruta")

#6 Loops de repetição while:
#Loop de repetição while, acontece enquando uma condição é verdadeira.
ligado = True

while ligado:
    for num in range(10):
        print(num)
    else:
        ligado = False

# Estrutura de dados
# Listas
# lista = [1, 2, 3]
