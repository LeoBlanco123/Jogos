import adivinhação
import forca

print("********************************")
print("********Escolha seu jogo********")
print("********************************")

print ("(1) Forca \n(2) Adivinhação")

jogo = int(input("Qual o jogo ?\nR: "))

if jogo == 1:
    print("Jogando Forca")
    forca.joga()

elif jogo == 2:
    print("Jogando Adivinhação")
    adivinhação.joga()
    