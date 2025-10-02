distancia=float(input("qual a distância ? "))
velocidade=float(input("qual a velocidade ? "))
tempo = distancia / velocidade
if tempo>4:
    print(f"viagem demorada, utilizar veículo sedan")
else:
    print(f"viagem rápida, utilizar veículo hatch")    
