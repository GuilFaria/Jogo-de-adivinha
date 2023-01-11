import random
import time

print("Olá, jogador(a)!")
time.sleep(1.6)
print("Bem vindo(a) ao jogo da adivinhação.")
time.sleep(1.6)
print ('Neste jogo, você terá que adivinhar um número de 0 a 100.')
time.sleep(2.3)
print("Vamos começar?!")
time.sleep(1.6)


recom = 0
quant = 0

while (recom == 0):
    num_alea = random.randrange(0, 100)
    a = 0
    while (a == 0):
        i = int(input("Advinhe um número: "))
        if (i < 0 or i > 100):
            print("Coloque um número de 0 a 100!")
            time.sleep(1.6)
        else:
            if (i < num_alea):
                if (i >= (num_alea - 5)):
                    pri_frn = ("Muito próximo, ")
                    quant += 1
                else:
                    pri_frn = ("Não está muito próximo, ")
                    quant += 1
                print (pri_frn + "tente um maior.")
            elif (i > num_alea):
                if (i <= (num_alea + 5)):
                    pri_frn = ("Muito próximo, ")
                    quant += 1
                else:
                    pri_frn = ("Não está muito próximo, ")
                    quant += 1
                print(pri_frn + "tente um menor.")
            else:
                quant += 1
                print ("Parabéns, vôce acertou!")
                time.sleep(1.6)
                print ("O número era " + str(num_alea) + ".")
                time.sleep(1.6)
                b = 0
                if quant == 1 :
                    print ("De primeira!!")
                    time.sleep(1.6)
                else:
                    print ("E vôce tentou " + str(quant) + " vezes.")
                    time.sleep(1.6)
                while (b == 0):
                    contin = str(input("Quer jogar de novo? "))
                    if (contin in ["s", "Sim", "sim", "s", "yes", "Yes", "yeah", "Yeah"]):
                        print ("Então, vamos jogar!")
                        time.sleep(1.4)
                        a = 1
                        b = 1
                        quant = 0
                    elif (contin in ["Não", "não", "Nao", "nao", "n", "N", "no", "nop", "No", "Nop"]):
                        a = 1
                        b = 1
                        recom = 1
                        time.sleep(0.7)
                    else:
                        print ("Não entendi :/")
                        time.sleep(1.2)
                        print ("Escreva sim ou não, eu não entendo mais que isso haha.")
                        time.sleep(1.6)
print ("Obrigado por jogar!")