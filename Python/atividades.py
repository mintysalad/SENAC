idade = 0

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print ("Você é maior de idade! :D")
elif idade < 18 and idade > 12:
    print("Você é adolescente! :D")
else:
    print("Você é criança.")