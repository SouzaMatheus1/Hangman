import random as rd
import pandas as pd
import os

def find_index(p_certa, palpite):
    for i in p_certa:
        if i == palpite:
            return p_certa.index(i)
            

# Banco de dados palavras
df = pd.read_csv('Lista-de-Palavras.txt', sep = ' ')
df = df.values

def definition_word():
#Definição da palavra sorteada
    palavra = rd.randrange(0, 29857)
    palavra_certa  = df[palavra]
    for i in palavra_certa:
        palavra_certa = i
    return palavra_certa

def concat_word(word):
    p = ''
    for i in word:
        p += i
    return p

palavra_certa = definition_word()
palavra_palpite = []
print(f"A palavra escolhida tem {len(palavra_certa)} letras!")
print(palavra_certa)

# Começo do jogo
entrada = int(input("1 - Começar.\n0 - Sair.\n"))
if entrada == 1:
        while True:
            palpite = input("Digite uma letra: ")
            palpite = palpite.upper()
            for i in palavra_certa:
                # i = letra da palavra sorteada
                if i == palpite:
                    print(f'Letra "{palpite}" adicionada!')
                    index_letra = find_index(palavra_certa, palpite)
                    palavra_palpite.insert(index_letra, palpite)
                    x = palavra_certa.replace(palpite, '')
                    print('palpite', palavra_palpite, len(palavra_palpite))
                    print('certa', palavra_certa, len(palavra_certa))
            if len(palavra_palpite) == len(palavra_certa):
                print('oi')
                break
           
        print(concat_word(palavra_palpite))
            
else:
    print("Obrigado por jogar!")
    