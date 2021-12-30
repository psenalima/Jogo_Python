def escolha_jogo():
    import forca
    import advinhacao


    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("****Escolha seu jogo****")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    print("[1] Forca [2] Advinhacao")

    jogo = int(input('Escolha quel jogo deseja: '))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()

    elif(jogo == 2):
        print("Jogando advinhacao")
        advinhacao.jogar()

if(__name__=="__main__"):
    escolha_jogo()