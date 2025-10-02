plano=input("tipo de plano(básico,padrão ou premium): ")
tempo=int(input("quanto tempo(meses): "))
if plano=='padrão' or plano=='premium':
    if tempo>=12 and tempo<=24:
         print( "Parabéns! Você tem direito a um desconto de 15%.")
    else:
        print("Seu plano é elegível, mas você não atende ao tempo de uso necessário para o desconto.")
else:
    print("Seu plano não é elegível para este desconto.")
