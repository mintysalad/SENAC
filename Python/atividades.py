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

gastosHyuna = [500, 300, 200, 800]
gastosLuka = [200, 300, 500, 700]

totalHyuna = sum(gastosHyuna)
totalLuka = sum(gastosLuka)

if totalHyuna > totalLuka:
    print("Hyuna gastou mais este mês.")
elif totalHyuna < totalLuka:
    print("Luka gastou mais este mês.")
else:
    print("Eles gastaram o mesmo valor.")