idade=int(input("qual sua idade: "))
experiência=int(input("anos de experiência em programação: "))
disponibilidade=input("disponibilidade de horário(manhã ou tarde): ")
if idade>18 and experiência>1:
    if disponibilidade=='manhã' or disponibilidade=='tarde':
        print("Parabéns! você é elegível para a vaga! ")
    else:
        print("Não elegível: Disponibilidade não corresponde aos requisitos.")
else:
    print("Não elegível: Idade ou experiência insuficientes.")