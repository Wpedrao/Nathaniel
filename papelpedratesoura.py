import termcolor
from termcolor import colored
from time import sleep
import os
import random


def ppt():
    while True:

        print("1 Qual sua escolha(pedra, papel, tesoura ou 0 para sair do jogo)")
        print("2 Qual sua escolha(pedra, papel, tesoura ou 0 para sair do jogo)")
        print("3 Qual sua escolha(pedra, papel, tesoura ou 0 para sair do jogo)")
        print("4 Qual sua escolha(pedra, papel, tesoura ou 0 para sair do jogo)")
        print("0 Sai do menu")


        jogador = input()
        if jogador == "0":
          return

        computador = (random.choice("123"))
        # 1 pedra
        # 2 papel
        # 3 tesoura

        if computador == 1:
            jog_comp = "pedra"
        elif computador == 2:
            jog_comp = "papel mesmo"
        else:
            jog_comp = "tesoura"

        print("O computador escolheu", jog_comp)

        if jog_comp == jogador.lower():
            print("O jogo empatou")
        elif jog_comp == "tesoura" and jogador.lower() == "papel":
            print("Você perdeu")
        elif jog_comp == "tesoura" and jogador.lower() == "pedra":
            print("Você Ganhou")
        elif jog_comp == "pedra" and jogador.lower() == "papel":
            print("Você Ganhou")
        elif jog_comp == "pedra" and jogador.lower() == "tesoura":
            print("Você perdeu")
        elif jog_comp == "papel" and jogador.lower() == "tesoura":
            print("Você Ganhou")
        elif jog_comp == "papel" and jogador.lower() == "pedra":
            print("Você perdeu")

def menu():
    print("Quer jogar PPT")
    return input("")



#Main
while True:
    escolha=menu()
    if escolha == "ppt":
       ppt()
    elif escolha == "saida":
        exit(0)
    elif escolha =="Ola":
        print("Ola")







