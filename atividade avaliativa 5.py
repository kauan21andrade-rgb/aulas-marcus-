print("Nome:Kauan Henry de Andrade")
print("RA 0220482523036")
C_inicial=float(input("qual o valor do custo inicial do material ? "))
print("valor do custo inicial é de " ,C_inicial)
Q=int(input("qual a quantidade de itens produzidos ? "))
print(" a quantidade de itens produzidos são " ,Q)
Dias=int(input("números de dias de atraso ? "))
print("números de dias de atrasos são " ,Dias)
Defeito=float(input("qual o percentual de defeitos ? "))
print("o percentual de defeitos é " ,Defeito)
if Q>1000 and C_inicial>5000:
    F_comp=1.15
    C_corrigido = C_inicial * F_comp
else:
    F_comp=1.05
    C_corrigido = C_inicial * F_comp
if Defeito>0.10 or Dias>5:
    print("Penalidade Alta: 20% de redução no lucro.")
    C_final = C_corrigido * 1.25
    print(f"custo base é de {C_corrigido} reais, e custo final é de {C_final} reais ")
elif Defeito>=0.05 and Defeito<=0.10 and Dias>0:
    print("Penalidade Média: 10% de redução no lucro.")
    C_final = C_corrigido * 1.10
    print(f"custo base é de {C_corrigido} reais, e custo final é de {C_final} reais ")
else:
    print(f"Sem penalidade. Custo final apenas com correção, sendo custo base com correção de {C_corrigido}")
