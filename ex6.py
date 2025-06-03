import random

# Configuração e "regras" do jogo (1 a 50)
numero_certo = random.randint(1, 50)
tentativas = 0

# painel inicial do jogo / layout
print("=== Jogo de Adivinhação ===") 
print("Tente adivinhar o número entre 1 e 50!")

# Loop 
while True:
    chance = int(input("\nSeu palpite: "))
    tentativas += 1
    
#condições de acerto/erro
    if chance == numero_certo:
        print(f"Parabéns! Você acertou em {tentativas} tentativas!")
        break
    elif chance < numero_certo:
        print("Dica: O número é MAIOR que esse!")
    else:
        print("Dica: O número é MENOR que esse!")