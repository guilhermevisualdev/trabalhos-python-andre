while True:
    try:
        numero = int(input("Digite um número inteiro: "))            #int para número inteiro, caso fosse usar números com vírgula -> float ou double
        break                                                        #caso a conversão seja/for bem-sucedida, sai do looping
    except ValueError:                                               #captura erro quando a conversão para inteiro falha (entrada de número e/ou caractere inválido(a))
        print(" - Erro ao digitar um número inteiro. Tente novamente, por favor - ")

print(f"Número digitado com sucesso: {numero}")