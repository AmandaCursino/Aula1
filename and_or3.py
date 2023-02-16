idade = int(input("Digite a sua idade: "))
dinheiro = int(input("Digite a quantidade de dinheiro que vocce tem: "))
carteira = input("Voce tem carteira de motorista? (s/n)")

if (idade >= 18 and dinheiro >= 50) or carteira == "s":
    print("Voce pode alugar o carro.")
else:
    print("Voce nao pode alugar o carro.")
    