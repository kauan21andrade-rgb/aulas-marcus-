print("Nome:Kauan Henry de Andrade")
print("RA 0220482523036")
p=float(input("qual o valor inicial de investimento em reais ? "))
print("valor inicial de investimento é " ,p)
t=int(input("qual o prazo de investimento em meses ? "))
print("prazo de investimento é " ,t)
if t<6:
    j=0.005
    Rendimentot = p * j * t
    print(f"o juros é de 0,5% ao mês,e o rendimento total é equivalente a {Rendimentot} reais")
elif t>6 and t<=12:
    j=0.008
    Rendimentot=p * j * t
    print(f"o juros é de 0,8% ao mês, com rendimento total de {Rendimentot} reais")
elif t>12:
    j=0.012
    Rendimentot=p * j * t
    print(f"o juros é de 1,2% ao mês, com rendimento total de {Rendimentot}")
else:
    print("só é permitido valores positivos!")

