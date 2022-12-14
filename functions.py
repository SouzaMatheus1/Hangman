import random as rd
import os

# Word definition
def definition_word(df):
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


# Create a trophy
def trophy():
    return """ 
                    ##########################          
                    ##########################            
                    ##########################            
                    ##########################          
             ########################################    
            ###     ##########################     ###    
            ###     ##########################     ###    
             ####    #######################    ####    
                ####  #####################  ####      
                 ###############################        
                    #########################           
                          ##############                 
                            #########                 
                            #########                                         
                         ###############                  
                        #################                
                        #################                
                        #################                               
                                     """
               
def pt_game(df):
    palavra_certa = list(definition_word(df))
    palavra_palpite = empty_array(palavra_certa)
    letras_erradas = []
    chances = 0
    
    # Start game
    entrada = int(input("1 - Iniciar jogo.\n0 - Sair.\n"))
    if entrada == 1:
        os.system('cls')
        while True:
            print(f"A palavra secreta tem {len(palavra_certa)} letras!")
            palpite = input("Inserir uma letra: ")
            palpite = palpite.upper()
            if palpite not in palavra_certa:
                letras_erradas.append(palpite)
                print('Letra incorreta!\n')
                chances += 1
                if chances == 7:
                    print("Você perdeu! Tente novamente!")
                    break
            for i in palavra_certa:
                if i == palpite:
                    print(f'Letra "{palpite}" adicionada!\n')
                    index_letra = palavra_certa.index(i)
                    palavra_palpite.pop(index_letra)
                    palavra_certa[index_letra] = "_"
                    palavra_palpite.insert(index_letra, i)
                    print('Palavra:', concat_word(palavra_palpite))
            if palavra_certa.count('_') == len(palavra_certa):
                os.system('cls')
                print(trophy())
                print(f'''
                    A palavra secreta foi {concat_word(palavra_palpite)}!
                ''')
                print('''
                      Você ganhou! Parabéns!''')
                break
    elif entrada == 0:
        os.system('cls')
        print("Obrigado por jogar!")
    else:
        os.system('cls')
        print("Comando inválido. Tente novamente.")
    
def en_game(df):
    palavra_certa = list(definition_word(df))
    palavra_palpite = empty_array(palavra_certa)
    letras_erradas = []
    chances = 0
    
    # Start game
    entrada = int(input("1 - Start game.\n0 - Exit.\n"))
    if entrada == 1:
        os.system('cls')
        while True:
            print(f"The secret word has {len(palavra_certa)} letters!")
            palpite = input("Insert a letter: ")
            palpite = palpite.lower()
            if palpite not in palavra_certa:
                letras_erradas.append(palpite)
                print('Letter incorrect!\n')
                chances += 1
                if chances == 7:
                    print("You lose! Try again!")
                    break
            for i in palavra_certa:
                if i == palpite:
                    print(f'Letter "{palpite}" added!\n')
                    index_letra = palavra_certa.index(i)
                    palavra_palpite.pop(index_letra)
                    palavra_certa[index_letra] = "_"
                    palavra_palpite.insert(index_letra, i)
                    print('Word:', concat_word(palavra_palpite))
            if palavra_certa.count('_') == len(palavra_certa):
                os.system('cls')
                print(trophy())
                print(f'''
                    The secret word was {concat_word(palavra_palpite).upper()}!
                ''')
                print('''
                    You win! Congratulations!''')
                break            
    elif entrada == 0:
        os.system('cls')
        print("Thanks for play!")
    else:
        os.system('cls')
        print("Invalid command. Try again.")