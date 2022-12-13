import random as rd
import pandas as pd
import os

def find_index(p_certa, palpite):
    for i in p_certa:
        if i == palpite:
            return p_certa.index(p_certa[i])
            

# txt with all words
df = pd.read_csv('Lista-de-Palavras.txt', sep = ' ')
df = df.values

# Word definition
def definition_word():
    palavra = rd.randrange(0, 29857)
    palavra_certa  = df[palavra]
    for i in palavra_certa:
        palavra_certa = i
    return palavra_certa

# Concatenate word
def concat_word(word):
    p = ''
    for i in word:
        p += i
    return p

# Create a empty array for guess
def empty_array(word):
    l = []
    for i in range(len(word)):
        l.append('_')
    return l

palavra_certa = list(definition_word())
print(f"A palavra escolhida tem {len(palavra_certa)} letras!")
print(concat_word(palavra_certa))
palavra_palpite = empty_array(palavra_certa)
palavra_erro = []

print(f"A palavra tem {len(palavra_palpite)} letras!")

# Start game
entrada = int(input("1 - Começar.\n0 - Sair.\n"))
if entrada == 1:
        while True:
            cont_letra = 0
            palpite = input("Digite uma letra: ")
            palpite = palpite.upper()
            for i in palavra_certa:
                if i == palpite:
                    print(f'Letra "{palpite}" adicionada!')
                    # index_letra = find_index(palavra_certa, palpite)
                    index_letra = palavra_certa.index(i)
                    palavra_palpite.pop(index_letra)
                    palavra_certa[index_letra] = "_"
                    palavra_palpite.insert(index_letra, i)
                    #print('Palavra:', concat_word(palavra_palpite))
                    print('aaa',palavra_certa, palavra_palpite)
                    # if (concat_word(palavra_palpite)) == concat_word(palavra_certa):
                    #     print("Parabéns bundão!")
else:
    print("Obrigado por jogar!")
