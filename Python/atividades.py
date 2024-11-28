idade = nome = 0

print("Qual teu nome??")
nome = (input("Digite seu nome: "))
print(f"Olá, {nome}!")

print("Qual a tua idade?")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print ("Você é maior de idade! :D")
elif idade < 18 and idade > 12:
    print("Você é adolescente! :D")
else:
    print("Você é criança.")