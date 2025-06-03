nota = float(input("Digite a nota (0-100): "))        #entrada do usuário

if nota >= 90:
    print('Excelente!')
    
elif nota >= 70 and nota <= 89:
    print('Bom!')
    
elif nota >= 50 and nota <= 69:
    print('Regular...')
    
else:
    print('Reprovado!!!')