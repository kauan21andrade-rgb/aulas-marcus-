nome=input("qual seu nome ?")
print("seu nome é" ,nome)
cateto1=float(input("qual o valor do cateto 1 ? "))
print("o valor do cateto 1 é " ,cateto1)
cateto2=float(input("qual valor do cateto 2 ? "))
print("o valor do cateto 2 é " ,cateto2)
hipotenusa = (cateto1**2 + cateto2**2)**0.5
if hipotenusa>180:
    print(f"valor de hipotenusa é {hipotenusa},triângulo deve ser refeito para ser compatível com proposta")
else:
    print(f"valor de hipotenusa é {hipotenusa},triângulo aceito deve ser incluído na proposta")