ingresso=input("qual o tipo de ingresso, padrão ou premium ? ")
print("seu ingresso é" ,ingresso)
idade=int(input("qual sua idade ?"))
print("sua idade é" ,idade)
vip=input("convidado vip(sim ou não) ?" )
print("você {vip} vip)")
if ingresso=='premium':
    print(f"Acesso total: todas as áreas e benefícios especiais.")
elif idade>=18 and vip=='sim':
    print(f"Acesso VIP: área exclusiva e entrada prioritária.")
elif idade>=18 or ingresso=='padrão':
    print(f"Acesso padrão: entrada para a área principal do evento.")
else:
    print(f"Acesso negado: verifique os critérios de entrada.")
