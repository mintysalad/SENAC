vendas = 1500
meta = 1300

# > maior que
# < menor que
# >= maior ou igual a
# <= menor ou igual a 
# == igual a 
# != diferente de 

if vendas >= meta:
    print("Vendedor ganhou bônus")
    print("Bateu a meta de vendas!")
    bonus = 0.1 * vendas
    print("Bônus do vendedor: ", bonus)
else:
    print("Vendedor não ganhou o bônus")
    print("Não bateu a meta de vendas")

print("Acabou o programa")

# Segundo Cenário
vendass = 1500
meta1 = 1300 # Ganha 10%
meta2 = 2000 # Ganha 13%

if vendass >= 2000:
    bonus = 0.13 * vendass
else:
    if vendass >= 1300:
        bonus = 0.1 * vendass
    else:
        bonus = 0

print("Bonus: ", bonus)

# Terceiro Cenário

vendas3 = 2500
vendasEmpresa = 10000
meta1 = 1300 # Ganha 10%
meta2 = 2000 # Ganha 13%
metaEmpresa = 20000

if vendas3 >= 2000 and vendasEmpresa >= metaEmpresa:
    bonus = 0.13 * vendas3
elif vendas >= 1300 and vendasEmpresa >= metaEmpresa:
    bonus = 0.1 * vendas3
else:
    bonus = 0

print("Bonus: ", bonus)

listaProdutos = ["airpod", "ipad", "iphone", "macbook"]
produtoProcurado = input("Procure um produto: ")
produtoProcurado = produtoProcurado.lower()

if produtoProcurado in listaProdutos:
    print("Produto em estoque")
else:
    print("Não temos esse produto em estoque.")

