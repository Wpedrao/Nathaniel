import termcolor
from termcolor import colored
from time import sleep
import os
import random



def cria_dado(cor, quantidade):
    Dado = []
    if cor == "verde":
        for contador in range(6):
            faces = "CPCTPC"
            Dado.append(cor)
            Dado.append(faces)
            bag.append(Dado)
            Dado = []
    elif cor == "amarelo":
        for contador in range(4):
            faces = "TPCTPC"
            Dado.append(cor)
            Dado.append(faces)
            bag.append(Dado)
            Dado = []
    else:
        for contador in range(3):
            faces = "TPTCPT"
            Dado.append(cor)
            Dado.append(faces)
            bag.append(Dado)
            Dado = []

    return

def apaga_dado(dado_sorteado):
    bag.remove(dado_sorteado)
    return

def sorteia_dado(quantidade):
    dado_coletado = []
    for contador in range(quantidade):
        dado_sorteado = (random.choice(bag))
        dado_coletado.append(dado_sorteado)
        apaga_dado(dado_sorteado)
    return dado_coletado

def lanca_dado(dados):
    sorteados = []
    resultado = []
    for dado in dados:
        face_sorteada = (random.choice(dado[1]))
        resultado = [dado[0], face_sorteada]
        sorteados.append(resultado)
    return sorteados

def inicializa_dados():
    bag = []
    cria_dado("verde", 6)
    cria_dado("amarelo", 4)
    cria_dado("vermelho", 3)
    return

def mostra_resultado(dados_jogogados):
        dados_relancaveis = []
        for dado in dados_jogogados:
            if dado[0] == "verde":
                cor = 'green'
            elif dado[0] == "amarelo":
                cor = "yellow"
            else:
                cor = "red"

            if dado[1] == "P":
                dados_relancaveis.append([cor,dado[1]])

            print(colored(dado[1],cor))


        return dados_relancaveis

def atualiza_resultado(r_jogador,dados_jogogados):
    for dado in dados_jogogados:
        if dado[1] == "T":
            r_jogador[1] += 1
        elif dado[1] == "C":
            r_jogador[2] += 1
        else:
            r_jogador[3] += 1
        if r_jogador[1] >= 3:
            print(r_jogador[0],"Você morreu com 3 tiros")
            exit(0)
        elif r_jogador[1] >= 13:
            print(r_jogador[0], "Você Ganhou o jogo atingiu 13 pontos")

    return r_jogador

## Entrada dos usuarios
bag = []
print(colored('Bem vindos ao Zombie Dice!!!', 'green'))
print("Quantos jogadores(2-4)? ")
jogs = int(input())
inicializa_dados()
info_jogadores = []

## Identifica Jogadores e inicia variaveis dos djogadores
for contador in range(jogs):
    passos = 0
    tiros = 0
    celebros = 0
    ordem = str(contador + 1)
    jogador = input("Nome do jogador" + ordem +": ")
    info_jogadores.append(jogador,tiros,celebros,pontos)


if jogs == 2:
    print("informe os nomes dos jogadores ")
    passos = 0
    tiros = 0
    celebros = 0
    jogada = 0
    jog1 = input("Primeiro jogador: ")
    result_jog1 = [ jog1,tiros,celebros, passos]
    jog2 = input("Segundo jogador: ")
    dados_jog1 = []
    print("Bem vindo jogadores", jog1, "e",jog2)
    print(jog1, "começa, os dados serão jogados.")

    for contador in range(4):
        input("Pessione para lançar os dados Jogador " + jog1)
        dados_jog1 = sorteia_dado(3)
        resultado_dado = lanca_dado(dados_jog1)
        dados_relancaveis = mostra_resultado(resultado_dado)
        result_jog1 = atualiza_resultado(result_jog1, resultado_dado)
        jogada += 1

    print("Numero de jogadas", jogada)

    print(result_jog1 )
    print(resultado_dado)



#Se o jogador decidir rerollar o dado de pegada ele pegará outros dois, se não ele só conta os pontos do cerébros que já obteu
#O jogador pode parar a qualquer momento, antes de tirar 3 tiros. Assim ele marca a quantidade de pontos de acordo com os cérebros que ele guardou.

if jogs == 3:
    print("informe os nomes dos jogadores ")
    jog1 = input()
    jog2 = input()
    jog3 = input()
    print("Bem vindo jogadores", jog1,",", jog2, "e",jog3)
if jogs == 4:
    print("informe os nomes dos jogadores ")
    jog1 = input()
    jog2 = input()
    jog3 = input()
    jog4 = input()
    print("Bem vindo jogadores", jog1,",", jog2,",",jog3,"e",jog4)


