temperatura=int(input("quantos graus celsius hoje:"))
chuva=input("está chovendo: ")
if temperatura>20 and chuva=='não':
    if temperatura>=15 and temperatura<=20 or chuva=='sim':
        print("o tempo está ideal para atividades ao lar livre!")
    else:
        print("o tempo não está ideal para atividades ao lar livre!")

else:
    print("O tempo não é propício para atividades ao ar livre!")  
       