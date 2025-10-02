media=float(input("média acadêmica do candidato, de uma escala de 0 a 10 ? "))
print("sua média é " ,media)
escrita=int(input( "qual seu grau de habilidade em escrita na escala de 1 a 5 ? "))
necessidade=input("passa necessidade financeira(sim ou não) ? ")
if media>=9 and escrita>=4:
    print(f"Parabéns! Você é elegível para a bolsa de mérito acadêmico.")
elif media>=8 and necessidade=='sim':
    print(f"Parabéns! Você é elegível para a bolsa de necessidade financeira.")
elif media>=7 and escrita>=3 and necessidade=='sim':
    print(f"Parabéns! Você é elegível para a bolsa combinada de mérito e necessidade.")
elif media>=7 and escrita>=3:
    print(f"Você é elegível para a bolsa de necessidade, mas sua média e habilidade em escrita são requisitos.")
else:
    print(f"Infelizmente, você não atende aos critérios de elegibilidade para bolsa.")
