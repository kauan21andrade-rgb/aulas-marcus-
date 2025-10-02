print("Nome:Kauan Henry de Andrade")
print("RA 0220482523036")
precoc=float(input("qual o preço de custo ? "))
print("preço de custo é " ,precoc)
precov=float(input("preço de venda é ?"))
print("preço de venda é " ,precov)
lucro=precov-precoc
margem=(lucro/precoc)*100
if margem>30:
    print("Margem excelente!")
elif margem>=10 and margem<=30:
    print("Margem Satisfatória.")
elif margem<10:
    print("Margem Baixa:Avaliar preço de venda.")
else:
    print("só pode números positivos!")
