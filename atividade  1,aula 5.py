quantidade=int(input("qual a quantidade ? "))
print(" a quantidade é", quantidade)
preço=float(input("qual o preço ? "))
print(" o preço é ", preço)
if quantidade>10:
    desconto=0.15
else: 
    desconto=0.08

valor=quantidade*preço
pagar=valor-(valor*desconto)
print(f"a quantidade é {round(quantidade,2)}, preço é equivalente a {round(preço,2)}, valor é {valor}, então, valor a pagar é o total de {round(pagar,2)}")        