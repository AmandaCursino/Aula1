x = int(input("Digite o primeiro numero: "))
y = int(input("Digite o segundo numero: "))
z = int(input("Digite o terceiro numero: "))

if x > y and x > z:
    result = "x é o maior numero"
elif y > x and y > z:
    result = "y é o maior numero"
elif z > x and z > y: 
    result = "z é o maior numero"
else:
    result = "há numeros iguais"
    
print(result)
