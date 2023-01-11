import random
import time
#Importando bibliotecas.

print("Olá, jogador(a)!")
time.sleep(1.6)
print("Bem vindo(a) ao jogo da adivinhação.")
time.sleep(1.6)
print ('Neste jogo, você terá que adivinhar um número de 0 a 100.')
time.sleep(2.3)
print("Vamos começar?!")
time.sleep(1.6)
#Introdução ao game.

recom = 0
#Váriavel de loop que será utilizadas com o while.

while (recom == 0): #Loop em caso de recomeço do jogo.
    num_alea = random.randrange(0, 100) #Função randrange apresenta um número pseudoaleatório entre 0 e 100.
    a = 0
    quant = 0
    while (a == 0): #Loop de iniciação.
        i = int(input("Advinhe um número: ")) 
        if (i < 0 or i > 100): #Em caso do input ser maior ou menor que os parâmetros.
            print("Coloque um número de 0 a 100!")
            time.sleep(1.6)
        else:
            if (i < num_alea): #Caso seja menor que o num_alea
                if (i >= (num_alea - 5)): #Se estiver 5% próximo do numero aleatório.
                    pri_frn = ("Muito próximo, ") #Escreve "Muito próximo".
                    quant += 1 #Váriavel que guarda a quantidade de tentativas.
                else:
                    pri_frn = ("Não está muito próximo, ") #Se for menor e não tiver a 5 números de num_alea.
                    quant += 1
                print (pri_frn + "tente um maior.") #Printa se estiver próximo ou não.
            elif (i > num_alea): #Caso o número dito for maior ele faz a mesma coisa só que a saída será para tentar um menor.
                if (i <= (num_alea + 5)):
                    pri_frn = ("Muito próximo, ")
                    quant += 1
                else:
                    pri_frn = ("Não está muito próximo, ")
                    quant += 1
                print(pri_frn + "tente um menor.")
            else: #Caso seja o número certo.
                quant += 1
                print ("Parabéns, vôce acertou!")
                time.sleep(1.6)
                print ("O número era " + str(num_alea) + ".")
                time.sleep(1.6)
                b = 0
                if quant == 1 :
                    print ("De primeira!!") #Easter egg, haha.
                    time.sleep(1.6)
                else:
                    print ("E vôce tentou " + str(quant) + " vezes.")
                    time.sleep(1.6)
                while (b == 0): #Novo loop.
                    contin = str(input("Quer jogar de novo? "))
                    if (contin in ["s", "Sim", "sim", "s", "yes", "Yes", "yeah", "Yeah"]): #Lista de strings que são aceitas se positivo.
                        print ("Então, vamos jogar!")
                        time.sleep(1.4)
                        a = 1
                        b = 1 #Recomeça o jogo. 
                    elif (contin in ["Não", "não", "Nao", "nao", "n", "N", "no", "nop", "No", "Nop"]):
                        a = 1
                        b = 1
                        recom = 1
                        time.sleep(0.7) #Acaba o jogo
                    else:
                        print ("Não entendi :/")
                        time.sleep(1.2)
                        print ("Escreva sim ou não, eu não entendo mais que isso haha.")
                        time.sleep(1.6) #Caso seja diferente de sim ou não.
print ("Obrigado por jogar!")