nome=input("qual seu nome ?")
print("seu nome é" ,nome)
salariof=float(input("qual o salário fixo do vendedor  ? "))
print("o salário do vendedor é", salariof)
comissaop=float(input("qual o valor da comissão por produto ?"))
print("valor da comissão é", comissaop)
quantidadep=float(input("qual a quantidade de produtos vendidos ?"))
print("quantidade de produto vendido é", quantidadep)
salariot = salariof + (comissaop * quantidadep)
if salariot<5000:
      imposto = salariot * 0.16
      desconto=salariot-imposto
      print(f"{nome}, seu salário fixo é {salariof}, comissão por produto é {comissaop}, sua quantidade de produto vendido é {quantidadep}, seu salário total é {salariot}, mas com descontos de imposto seu salário fica {desconto}")
else:
      imposto = salariot * 0.27
      desconto=salariot-imposto
      print(f"{nome}, seu salário fixo é {salariof}, comissão por produto é {comissaop}, sua quantidade de produto vendido é {quantidadep}, seu salário total é {salariot}, mas com descontos de imposto seu salário fica {desconto}")