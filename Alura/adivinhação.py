import random

def joga():

    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    pontos = 150


    print("\nQual o nivel de dificuldade?")
    print("(1) Facil (2) Medio (3) Dificil")

    nivel = int(input("Defina seu nivel: "))

    if nivel == 1:
        tentativas = 10
        dificuldade = 20
        aleatorio = random.randint(1, 20)

    elif nivel == 2:
        tentativas = 10
        dificuldade = 60
        aleatorio = random.randint(1, 60)

    else:
        tentativas = 6
        dificuldade = 100
        aleatorio = random.randint(1, 100)

    rodada = 1

    while rodada <= tentativas:

        print(f"O numero vai de 1 a {dificuldade}")
        print(f"Tentativa {rodada} de {tentativas}")

        chute = int(input(f"\nDigite um numero: "))

        pontos_perdidos = abs(aleatorio - chute)
        pontos -= pontos_perdidos

        if chute < 1 or chute > 100:
            print(f"Valor invalido (1 a {dificuldade})")
            continue

        if chute == aleatorio:
            print(f"Parabens, você acertou \nVoce fez {pontos} pontos")
            break

        elif chute > aleatorio:
            print("Voce errou! O seu chute foi maior que o numero secreto")

        elif chute < aleatorio:
            print("Voce errou! O seu chute foi menor que o numero secreto")

        rodada +=1
        
    print("\nFim do jogo")  

