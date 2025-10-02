experiencia=int(input(" quantos anos de experiência em vendas ? "))
print("anos de experiência em anos: " ,experiencia)
comunicação=int(input("em uma escala de 1 a 10, quanto é sua habilidade de comunicação ? "))
print("habilidade de comunicação equivalente a " ,comunicação )
horário=input("disponibilidade de horário integral ou meio período ? ")
print("disponibilidade de horário " ,horário)
if experiencia>2 and comunicação>8:
    print(f"Candidato classificado como Sênior. Entra na próxima etapa para vaga integral.")
elif experiencia>2 and comunicação>6:
    print(f"Candidato classificado como Sênior. Entra na próxima etapa para vaga de meio período.")
elif experiencia>1 and comunicação>8 and horário=='meio período':
    print(f"Candidato classificado como Pleno. Entra na próxima etapa para vaga de meio período.")
elif experiencia>1 and comunicação>8 and horário=='integral':
    print(f"Candidato classificado como Pleno. Entra na próxima etapa para vaga integral.")
elif comunicação>7 and horário=='meio período':
    print(f"Candidato classificado como Júnior. Entra na próxima etapa para vaga de meio período.")
elif comunicação>7 and horário=='integral':
    print(f"Candidato classificado como Júnior. Entra na próxima etapa para vaga integral.")
else:
    print(f"Candidato não classificado. Não atende aos requisitos mínimos.")