faturamento = 1200
custo = 700
lucro = faturamento - custo
margemLucro =lucro / faturamento

print(f"Faturamento da empresa: R${faturamento:.2f}Custo: R$ {custo:.2f} Lucro: R${lucro:.2f}")

emailCliente = "meowmeowmeow@gmail.com"

print(emailCliente)

#Maiusculas
emailCliente = emailCliente.upper()
print(emailCliente)

#Minusculas
emailCliente = emailCliente.lower()
print(emailCliente)

#Encontrar o @ ou outros caracteres quaisquer
print(emailCliente.find("@"))
