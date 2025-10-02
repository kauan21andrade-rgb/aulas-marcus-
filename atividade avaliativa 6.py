print("Nome:Kauan Henry de Andrade")
print("RA 0220482523036")
R_investimento=float(input("qual o retorno do investimento ? "))
print("retorno do investimento é de " ,R_investimento)
R_livre=float(input("qual a taxa livre de risco ? "))
print("taxa livre de risco é " ,R_livre)
Sigma=float(input("qual o desvio-padrão da volatilidade ? "))
print("valor do desvio padrão de volatilidade é " ,Sigma)
Spread = R_investimento - R_livre
if Sigma==0:
    Sharp = (R_investimento - R_livre) / Sigma
else:
    Sharp = (R_investimento - R_livre)
if Sharp>1.5 and Spread>0.05:
    print("Investimento Excelente: Alta performance ajustada ao risco.")
elif Sharp>=0.5 and Sharp<=1.5 or Spread>0.02:
    print("Investimento Bom: Risco e retorno moderados.")
elif Sharp<0.5 and  R_investimento>0:
    print("Investimento Aceitável: Retorno positivo, mas risco alto para o ganho.")
else:
    print("Investimento Ruim: Não recomendado.")
