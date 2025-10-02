peso = float(input("Digite o peso do pacote em kg: ")) #pede ao usuário que coloque o peso em kg

destino = input("Digite o destino ('local' ou 'nacional'): ").lower() # pede que o usuário que coloque o destino, local ou nacional#função lower converte as letras para minúsculo 

custo_total = 0.0 #será usado mais pra frente e será um valor dado pela condição 

if destino == 'local': # condição se destino for equivalente a local
    
    custo_base = 5.00 #custo base se destino for local
    
    if peso > 10:  #condição se peso for maior que 10 kg
    
        excesso_peso = peso - 10  #cálculo de excesso de peso, peso-10
    
        custo_extra = excesso_peso * 2.00  #custo extra pelo excesso de peso 
    
        custo_total = custo_base + custo_extra#custo total, custo base(5)+ custo extra pelo excesso de peso
    
    else:#caso peso for menor que 10
        
        custo_total = custo_base#caso o peso não ultrapasse 10 kg
    
        print(f"O custo total do envio para o destino local é: R$ {custo_total:.2f}")#função que mostra custo total se for destinado a local#2f, como se fosse um round, mostra 2 números depois da vírgula

else:  # Se o destino não for 'local', entra neste bloco
    
        if destino == 'nacional':#condição de envio nacional
        
            custo_base = 15.00#custo base de 15
        
        if peso > 10:# condição se peso ultrapassar 10 kg
            
            excesso_peso = peso - 10#conta do excesso de peso
            
            custo_extra = excesso_peso * 5.00#cálculo do custo extra
            
            custo_total = custo_base + custo_extra#cálculo do custo total
        
        else:#condição se peso for menor que 10 e for nacional  
            
            custo_total = custo_base#custo total
        
            print(f"O custo total do envio para o destino nacional é: R$ {custo_total:.2f}")#mostra o custo total de envio para destino nacional, novamente com a função :.2f
    
        else:#se destino for diferente de local ou nacional
        
            print("Erro: Destino inválido. Por favor, digite 'local' ou 'nacional'.")#mensagem se for diferente que local ou nacional o destino