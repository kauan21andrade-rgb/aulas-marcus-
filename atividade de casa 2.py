salario=float(input("qual seu salário ? "))
print(" salário é " ,salario )
horas=int(input("quantas horas de  trabalho ? "))
print("as horas trabalhadas são " ,horas)
if salario > 5000 and horas < 40:
    adicional=0.15
else:
   adicional=0.18

adicionals=horas*adicional 
salariot=salario+adicionals
print(f"salário é {salario}, adicional é {adicional}, então salário é {salariot} ")