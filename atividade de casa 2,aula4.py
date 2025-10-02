from re import A


nome=input("qual seu nome ? " )
print("seu nome é ", nome)
basemaior=float(input("qual valor da base maior ?"))
basemenor=float(input("qual valor da base menor ?"))
h=float(input("qual valor da altura ?"))
print("valor da base maior é ", basemaior)
print("valor da base menor é ", basemenor)
print("valor da altura ", h)
area = (basemaior + basemenor) * h / 2 
print(f"conside rando o valor das medidas base maior:{basemaior},base menor:{basemenor},altura:{h}, valor da área é igual é igual a {area}")