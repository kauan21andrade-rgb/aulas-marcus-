
nome=input("qual seu nome ?")
print("seu nome é" ,nome)
nascimento=int(input("qual seu ano de nascência ?"))
print("nasceu ano " ,nascimento)
mes=int(input("qual mês você nasceu ? "))
print("seu mês de nascimento é " ,mes)
dia=int(input("qual dia voê nasceu ? "))
print("nasceu em " ,dia)
ano=2025-nascimento
mesob=12*ano
diaob=30*mesob
print(f"você tem {ano} anos, {mesob} mês e {diaob} dias")