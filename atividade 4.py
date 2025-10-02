nome=input("qual seu nome ?")
print("seu nome é" ,nome)
valorf=float(input("qual o valor futuro ? "))
print("o valor futuro é " ,valorf)
taxaj=float(input("qual o valor da taxa de juros ? "))
print("o valor da taxa de juros é " ,taxaj)
anos=int(input("quantos anos ? "))
print(" são essa quantidade de anos " ,anos)
valorpresente = valorf / (1 + taxaj)**anos
if valorpresente<30000:
    print(f"{nome}, valor futuro é {valorf}, taxa de juros é {taxaj} e são {anos} anos, portanto valor presente é  {round(valorpresente,5)},")
    print(f"valor deve ser investido em bens não duráveis")
else:
     print(f"{nome}, valor futuro é {valorf}, taxa de juros é {taxaj} e são {anos} anos, portanto valor presente é  {round(valorpresente,5)},")
     print(f"valor deve ser investido em renda fixa superior a 24 meses")