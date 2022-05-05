# %%
'''Welcome to Hangman
The game where you have to guess the word using 5 attempts'''
import random
import time
from time import sleep
import os

def swap(letter, word):
    for i in range(len(word)):
        if word[i]==letter:
            global word_guessed
            word_guessed=word_guessed[:i]+letter+word_guessed[i+1:]
    return word_guessed    

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list=word_list
        self.num_lives=num_lives

    def ask_letter(self, letter,list_letter):
        os.system("cls")
        print(f"\n=== Please guess your letter ===")
        for j in hang_dict[self.num_lives]:
            print(j)
        print("================================")
        print(" ".join(list(word_guessed)))
        used=" ".join(list_letter)
        if len(list_letter)>0: 
            print(f"\n You have {self.num_lives} lives left and used letters: {used}")
        else: print(f"\n You have {self.num_lives} lives left and {len(word)} letters to guess.")

        
        letter=input('Please guess the letter  ').upper()
        if len(letter)!=1:
            print ("\nPlease, enter just ***ONE*** character\n")
            time.sleep(3)
            self.ask_letter(letter, list_letter)
        elif letter in list_letter:
            print (f"{letter} was already tried\n")
            time.sleep(3)
            self.ask_letter(letter, list_letter)
        elif letter in ['0','1','2','3','4','5','6','7','8','9']:
            print (f"{letter} is a number, please enter the letter\n")
            time.sleep(3)
            self.ask_letter(letter, list_letter)
        else:
            list_letter.append(letter)
            self.check_letter(letter, word, word_guessed)

    def check_letter(self, letter, word, word_guessed):
        if letter in word:
            word_guessed=swap(letter, word)
            if word_guessed==word:
                print(f"\nThe word is {word_guessed}")
                print("\n CONGRATULATIONS, you won!")
                exit
            else: self.ask_letter(letter,list_letter)      
        else:
            self.num_lives-=1
            print(f'SORRY, {letter} is not in the word.')
            print(f'\nYou have {self.num_lives} lives left.')
            if self.num_lives==0: 
                os.system("cls")
                print (f"You ran out of lives. The word was")
                print ("."*(10), end="")
                time.sleep(2)
                print (f"\n{word.upper()}")
                print("\n".join(str(item) for item in hang_dict[0]))
                quit
            else: self.ask_letter(letter,list_letter)
            

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    game.ask_letter(letter, list_letter)


if __name__ == '__main__':
    os.system("cls")
    print("=====================")
    print("What Fruit Can It Be?")
    print("=====================")
    time.sleep(3)
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    list_letter=[]
    letter=''
    word=random.choice(word_list).upper()
    word_guessed='_'*len(word)
    hang_dict={
        5:[' ___', ' |', ' |','_|_'],
        4:[' ___', ' |  O', ' |','_|_'],
        3:[' ___', ' |  O', ' | /|','_|_'],
        2:[' ___', ' |  O', ' | /|\\','_|_'],
        1:[' ___', ' |  O', ' | /|\\','_|_/'],
        0:[' ___', ' |  O', ' | /|\\','_|_/ \\']}
    play_game(word_list)
    
# %%
