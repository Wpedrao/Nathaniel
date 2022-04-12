"""
      Nathaniel Azzolini Pedrão
      Desenvolvimento de Sistemas
      Raciocinio Computacional
"""
from termcolor import colored
from time import sleep
import random


def cria_dado(cor, quantidade):
    """
    Função responsavel pela criação dos dados com os paramentro cor
    e quantidade de dados da cor definida
    """
    Dado = []
    if cor == "green":
        for contador_cd in range(quantidade):
            faces = "CPCTPC"
            Dado.append(cor)
            Dado.append(faces)
            bag.append(Dado)
            Dado = []
    elif cor == "yellow":
        for contador_cd in range(quantidade):
            faces = "TPCTPC"
            Dado.append(cor)
            Dado.append(faces)
            bag.append(Dado)
            Dado = []
    else:
        for contador_cd in range(quantidade):
            faces = "TPTCPT"
            Dado.append(cor)
            Dado.append(faces)
            bag.append(Dado)
            Dado = []

    return


def apaga_dado(dado_sorteado):
    """
     Função responsavel pela remoção da sacola do dado sorteado
     informar o dado que foi sorteado
     """
    bag.remove(dado_sorteado)
    return


def sorteia_dado(quantidade, dados_relancaveis_l):
    """
     Função responsavel pelo sorteio dos dados, pegar da sacola,
     com o reaproveitamento dos dados marcados como relançaveis
     Informar a quantidade de dados a serem lançados e o conjunto de
     dados relançaveis
     Retorna o conjunto de dados a serem laçados
     """
    dado_coletado = []
    reutilizados = 0

    for dado_velho in dados_relancaveis_l:
        if dado_velho[1] == "P":
            if dado_velho[0] == "green":
                cor = "green"
                faces = "CPCTPC"
            elif dado_velho[0] == "yellow":
                cor = "yellow"
                faces = "TPCTPC"
            else:
                cor = "red"
                faces = "TPTCPT"
            dado_coletado.append([cor, faces])
            reutilizados += 1

    for contador_sd in range(quantidade - reutilizados):
        dado_sorteado = (random.choice(bag))
        dado_coletado.append(dado_sorteado)
        apaga_dado(dado_sorteado)

    return dado_coletado


def lanca_dado(dados):
    """
      Função responsavel pelo lançamento dos dados e alimenta os resultados
      Retorna o conjunto as faces dos dados lançados
    """
    sorteados = []
    for dado in dados:
        face_sorteada = (random.choice(dado[1]))
        resultado = [dado[0], face_sorteada]
        sorteados.append(resultado)
    return sorteados


def inicializa_dados():
    """
      Função responsavel pela criação dos dados
    """
    bag = []
    cria_dado("green", 6)
    cria_dado("yellow", 4)
    cria_dado("red", 3)
    return


def mostra_resultado(dados_jogogados):
    """
       Função responsavel por imprimir o resultado do lançamento dos dados
       recebe como parametro o resultado do lançamento imprimi resultado e
       acumula se existirem dados as serem relançados

     """
    relancaveis = []
    for dado in dados_jogogados:
        if dado[0] == "green":
            cor = 'green'
        elif dado[0] == "yellow":
            cor = "yellow"
        else:
            cor = "red"

        if dado[1] == "P":
            relancaveis.append([cor, dado[1]])

        print(colored(dado[1], cor))

    return relancaveis


def atualiza_resultado(r_jogador, dados_jogogados):
    """
       Função responsavel por atualizar o placar geral dos jogadores
       recebendo os dados da jogada e nome do jogador
       Verifica se o jogador morreu, e se jogador atingiu 13 pontos e ganhou o jogo
       retorna o placar do jogador atualizado
     """
    for dado in dados_jogogados:
        if dado[1] == "T":
            r_jogador[1] += 1
        elif dado[1] == "C":
            r_jogador[2] += 1

        if r_jogador[1] >= 3:
            if r_jogador[3] == 0:
                print(r_jogador[0], "Você morreu com 3 tiros")
                r_jogador[3] = 1
        elif r_jogador[2] >= 13:
            print(r_jogador[0], "Você Ganhou o jogo atingiu 13 pontos")
            exit(0)

    return r_jogador


def continuar_lancar(jogador_l):
    """
       Função responsavel pela solicitação de continuidade de lançamentos dentro
       do turno do jogador
       Retorna 0 quando passa a vez
       Rerona 1 quando vai continuar
     """
    while True:
        resposta = input("Lançar novamente " + jogador_l + " (s/n):")
        print("*" * 10)
        if resposta not in "SNsn":
            print("Informe (s/n) ")
        else:
            if resposta in "Nn":
                print("Passou a vez")
                sleep(0.8)
                print("\n\n\n\n\n\n\n")
                return 0
            else:
                print("\n\n\n\n\n\n\n")
                return 1


def placar(jogadores_local):
    """
       Função responsavel por mostrar o placar geral da partida recebe jogadores
    """
    print("JOGADOR        Tiros    Celebros")
    for jogador_l in jogadores_local:
        nome_jogador = jogador_l[0] + "            "
        print(nome_jogador[0:10], "      ", jogador_l[1], "      ", jogador_l[2])
    return


# Inicialização do programa
# Entrada dos usuarios
bag = []

print(colored('Bem vindos ao Zombie Dice!!!', 'green'))

while True:
    print("Quantos jogadores? Digite 0 para encerrar")
    jogs = int(input())
    if jogs == 0:
        print(colored("\n\n\n\n\n\nObrigado por jogar Zombie Dice!!!", 'green'))
        exit(0)
    elif jogs < 2:
        print(colored("Favor informar um numero maior que 1 ou 0 para sair", 'green'))
    elif jogs > 99:
        print(colored("Favor informar um numero menor que 99 ou 0 para sair", 'green'))
    else:
        break

inicializa_dados()
jogadores = []
mortos = 0
# Identifica Jogadores e inicia as variaveis dos jogadores
for contador in range(jogs):
    passos = 0
    tiros = 0
    celebros = 0
    morto = 0
    ordem = str(contador + 1)
    nome = input("Nome do jogador " + ordem + ": ")
    jogador = [nome.title(), tiros, celebros, morto]
    jogadores.append(jogador)

print("Bem Vindos ao Jogo")
for jogador in jogadores:
    print(colored(jogador[0], 'green'))

print("\n\n\n\n\n\n\n")

# Turnos do Jogo
print(colored("Vamos começar o jogo", 'green'))
contador = 0
dados_novos = 3
dados_relancaveis = []
while True:
    if jogadores[contador][3] == 0:
        print(colored("Jogador " + jogadores[contador][0], 'green'))
        if mortos - 1 == 0:
            print(colored("Jogador " + jogadores[contador][0] + "  Venceu", 'green'))
            print("Os demais jogadores morreram")
            placar(jogadores)
            break
        input("Tecle enter para Selecionar e lançar os dados")
        dados_selecionados = sorteia_dado(dados_novos, dados_relancaveis)
        resultado_dado = lanca_dado(dados_selecionados)
        dados_relancaveis = mostra_resultado(resultado_dado)
        jogadores[contador] = atualiza_resultado(jogadores[contador], resultado_dado)
        placar(jogadores)

        if len(dados_relancaveis) + len(bag) < 3:
            print("Impossivel continuar a jogar menos de 3 dados na BAG")
            # numero de tiros volta a 0 após passar a jogada
            jogadores[contador][1] = 0
            contador += 1
            inicializa_dados()
            if contador > (len(jogadores) - 1):
                contador = 0
        else:
            if jogadores[contador][3] == 1:
                print("Jogador", jogadores[contador][0], "esta morto pulando a vez")
                contador += 1
                mortos += 1
                inicializa_dados()
                if contador > (len(jogadores) - 1):
                    contador = 0
            else:
                if continuar_lancar(jogadores[contador][0]) == 0:
                    # numero de tiraos volta a 0 após passar a jogada
                    jogadores[contador][1] = 0
                    contador += 1
                    inicializa_dados()
                    if contador > (len(jogadores) - 1):
                        contador = 0
    else:
        print("O jogador", jogadores[contador][0], "Está morto...")
        contador += 1
        inicializa_dados()
        if contador > (len(jogadores) - 1):
            contador = 0
