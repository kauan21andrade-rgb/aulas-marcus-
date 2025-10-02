orçamento=float(input("qual o orçamento: "))
equipe=int(input("membros da equipe: "))
áreadepesquisa=input("qual área de pesquisa(inovação ou sustentabilidade): ")
if orçamento>50.000 and equipe>3:
    if áreadepesquisa=='inovação' or áreadepesquisa=='sustentabilidade':
        print("Projeto qualificado para o financiamento!")
    else:
        print("Projeto não qualificado: A área de pesquisa não é prioritária.")
else:
    print( "Projeto não qualificado: Orçamento ou tamanho da equipe insuficientes.")