import random
def computador_joga(fosforos):
    if fosforos %5 == 0:
        jogada = random.randint(1,4)
    else:
        jogada = fosforos % 5
    print(f"Computados tirou {jogada} fosforos.")
    return jogada
def jogador_joga():
    while True:
        try:
            jogada = int(input("Quantos fosforos quer tirar? (1-4):"))
            if jogada in [1, 2, 3, 4]:
                return jogada
            else:
                print("Jogada inválida. Insira um número entre 1 e 4.")
        except ValueError:
            print("Entrada inválida. Insira im número entre 1 e 4.")
def modo_jogador_primeiro():
    fosforos = 21
    print("\nModo 1: Começa a jogar.")
    while fosforos > 0:
        print(f"Fosforos restantes: {fosforos}")
        jogada_jogador = jogador_joga()
        fosforos -= jogada_jogador
        if fosforos <= 0:
            print("Perdeu! Retirou o último fosforo.")
            break
        print(f"Fosforos restantes: {fosforos}")
        jogada_computador = computador_joga(fosforos)
        fosforos -=jogada_computador
        if fosforos <= 0:
            print("Ganhou! O computador tirou o último fosforo.")
            break
def modo_computador_primeiro():
    fosforos = 21
    print("\nModos 2: O computador começa a jogar.")
    while fosforos > 0:
        print(f"Fosforos restantes: {fosforos}")
        jogada_computador = computador_joga(fosforos)
        fosforos -= jogada_computador
        if fosforos <= 0:
            print("Perdeu! Retirou o último fosforo.")
            break
def iniciar_jogo():
    print("Bem-vindo ao jogo dos 21 fosforos!")
    print("Quem retirar o último fosforo perde o jogo.")
    while True:
        print("\nEscolha o modo de jogo:")
        print("1 - O jogador começa.")
        print("2 - O computador começa.")
        modo = input("Digite o número do modo:")
        if modo == '1':
            modo_jogador_primeiro()
            break
        elif modo == '2':
            modo_computador_primeiro()
            break
        else:
            print("Opção inválida. Tente novamente.")
iniciar_jogo()
