idade=int(input("qual sua idade: "))
peso=float(input("qual seu peso:"))
condiçãosaúde=input("qual sua condição de saúde(boa ou ruim): ")
if idade>18 and peso>=50:
    if condiçãosaúde=='boa':
        print("Você está elegível para doar sangue!")
    else:
       print("Você não pode doar sangue devido à sua condição de saúde.")
else:
    print("Você não está elegível para doar sangue. Verifique os requisitos de idade e peso.")