tamanho=input("tamanho da pizza é pequena, média ou grande ? ")
print("tamanho da pizza é " ,tamanho)
sabores=int(input("qual o números de sabores ? "))
print("números de sabores são" ,sabores)
cliente=input("cliente vip ou normal ?")
print("cliente é " ,cliente)
if tamanho=='grande' and sabores>2:
    print(f"Pedido especial: sujeito a taxa extra.")
elif tamanho=='grande' or cliente=='vip':
    print(f"Pedido prioritário: prepare para entrega rápida.")
elif tamanho=='média' and sabores==1:
    print(f"Pedido padrão: processamento normal.")
else:
    print(f"Pedido de baixo volume: pode ser processado a qualquer momento.")
