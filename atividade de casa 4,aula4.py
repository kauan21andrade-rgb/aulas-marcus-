from re import A


nome=input("qual seu nome ? " )
print("seu nome é ", nome)
raio=float(input("qual valor do raio do cilindro ?"))
h=float(input("qual valor da altura do cilindro ?"))
print("valor do raio do ciindro  é ", raio)
print("valor da altura é ", h)
pi=3.14159
volume = pi * raio**2 * h
print(f"considerando o valor das medidas raio:{raio},altura:{h},pi:{pi}, valor do volume do cilindro  é igual a {volume}")