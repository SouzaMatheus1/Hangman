import pandas as pd
from functions import *

print("Bem-vindo ao jogo da forca supremo!")
print("Welcome to supreme hangman game!\n")

print("Escolha o idioma: ")
print("Select the leanguage: ")
idioma = int(input("1 - Portguês (PT-BR)\n2 - English (EN-US)\n"))

if idioma == 1:
    # txt with all words
    df = pd.read_csv('Lista-de-Palavras.txt', sep = ' ')
    df = df.values
    pt_game(df)
elif idioma == 2:
    df = pd.read_csv('wordlist.txt', sep = ' ')
    df = df.values
    en_game(df)
else:
    print("Comando inválido! Tente novamente!")
    print("Invalid command! Try again!")
