from turtle import fd


print("Nome:Kauan Henry de Andrade")
print("RA 0220482523036")
pureza=float(input("qual o valor da pureza do lote ? "))
print("valor da pureza do lote é " ,pureza)
massat=int(input("qual o valor da massa total em quilos ? "))
print("valor da massa total em quilos é " ,massat)
taxac=float(input("qual a taxa de contaminação ? "))
print("a taxa de contaminação é de " ,taxac)
FD = (pureza * 100) - (taxac * 50)
if massat>1000:
    pbase=10
else:
    pbase=12.50
if FD>90 and pureza>0.98:
     P_final_kg= pbase * 1.50
     Preco_Total_Final = P_final_kg * massat
     print("Classificação: PREMIUM (Venda Imediata)")
     print(f"preço base é {pbase} e preço final total é de {P_final_kg},50% de bônus, preço total final de {Preco_Total_Final}")
elif FD>=70 and FD<=90 and taxac<0.05:
    print("Classificação: PADRÃO (Venda Normal)")
    P_final_kg = pbase * 1.10
    Preco_Total_Final = P_final_kg * massat
    print(f"preço base é {pbase} e preço final total é de {P_final_kg},10% de bônus, preço total final de {Preco_Total_Final}")
elif FD<70 or pureza<0.90:
    print("Classificação: REPROVADO (Descarte ou Re-processamento)")
    P_final_kg = pbase * 0.25
    Preco_Total_Final = P_final_kg * massat
    print(f"preço base é {pbase} e preço final total é de {P_final_kg}, 75% de desconto no custo,preço total final de {Preco_Total_Final}")
else:
    P_final_kg=pbase*0.90
    Preco_Total_Final = P_final_kg * massat
    print("Classificação: ACEITÁVEL (Margem Mínima)")
    print(f"preço base é {pbase} e preço final total é de {P_final_kg}, 10% de desconto no preço base, preço total final de {Preco_Total_Final}")