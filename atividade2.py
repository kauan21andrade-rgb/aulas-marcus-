import math 
a=int(input("qual o valor de lado a ? "))
print("valor de a é " ,a)
b=int(input("qual o valor de lado b ? "))
print("valor de b é " ,b)
c=int(input("qual o valor de lado c ? "))
print("valor de c é " ,c)
cossenogama = (a**2 + b**2 - c**2) / (2 * a * b)
cossenogama = math.degrees(math.acos(cossenogama))
soma=a+b
soma2=a+c
soma3=c+b
if soma<c or soma2<b or soma3<a:
    print(f"ERRO!")
elif cossenogama==90:
    print(f"Triângulo Retângulo")
elif cossenogama<90:
    print(f"Triângulo Acutângulo")
elif cossenogama>90:
    print(f"Triângulo Obtusângulo")
else:
    print(f"Não é um triângulo")