import random
import os

###################################################################
os.system("cls")


pontos_user = 0
pontos_pc = 0

lista_jogadas = ["Pedra","Papel","Tesoura"]

while True:
    try:
        print("")
        print("########### Jogo Pedra, Papel e Tesoura ###########")
        print("")
        print("PLACAR:\nJogador: {}\nPC: {}".format(pontos_user,pontos_pc))
        print("")
        print("Escolha sua Jogada: 0 - Pedra | 1 - Papel | 2 - Tesoura")

        jogadaUser = int(input())
        jogadaPC = random.randint(0,2)

        print("----------------")
        print("Jogada Usuario: {}\nJogada PC: {}".format(lista_jogadas[jogadaUser], lista_jogadas[jogadaPC]))
        print("----------------")
        print("")
        if jogadaUser == jogadaPC:
            print("Empate!!!!")
        else:
            userVenceu = False
            if(jogadaUser > jogadaPC or (jogadaUser == 0 and jogadaPC == 2)): userVenceu = True

            if(userVenceu): 
                print("#### Você venceu #####")
                pontos_user +=1
            else:
                
                print("Você Perdeu :(")
                pontos_pc +=1      
    except Exception as e:
        print(e)
        
    print("----------------")
    print("")
    print("Deseja Jogar Novamente?\n1 - Jogar | 0 - Sair")
    
    opcao = int(input())
    if(opcao == 1): 
        os.system("cls")
        continue
    elif(opcao == 0): break
    else:
        print("Opção Invalida....")    


