import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

tamanho = int(input("Digite o comprimento da senha: "))

senha = ""  # variável onde a senha será armazenada

for _ in range(tamanho):
    senha += random.choice(caracteres)

print("Senha gerada:", senha)
