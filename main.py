import pygame
import os
import numpy as np
import random 
import math 

# Colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)
WINDOW_SIZE = [1000, 1000]

cards = {1:'Ace_of_Spades', 2:'Ace_of_Clubs', 3:'Ace_of_Diamonds', 4:'Ace_of_Hearts',
        5:'2_of_Spades', 6:'2_of_Clubs', 7:'2_of_Diamonds', 8: '2_of_Hearts',
        9:'3_of_Spades', 10:'3_of_Clubs', 11:'3_of_Diamonds',12:'3_of_Hearts',
        13:'4_of_Spades', 14:'4_of_Clubs', 15:'4_of_Diamonds',16:'4_of_Hearts',
        17:'5_of_Spades', 18:'5_of_Clubs', 19:'5_of_Diamonds',20:'5_of_Hearts',
        21:'6_of_Spades', 22:'6_of_Clubs', 23:'6_of_Diamonds',24:'6_of_Hearts',
        25:'7_of_Spades', 26:'7_of_Clubs', 27:'7_of_Diamonds', 28:'7_of_Hearts',
        29:'8_of_Spades', 30:'8_of_Clubs', 31:'8_of_Diamonds',32:'8_of_Hearts',
        33:'9_of_Spades', 34:'9_of_Clubs', 35:'9_of_Diamonds',36:'9_of_Hearts',
        37:'10_of_Spades', 38:'10_of_Clubs', 39:'10_of_Diamonds',40:'10_of_Hearts',
        41:'Jack_of_Spades', 42:'Jack_of_Clubs', 43:'Jack_of_Diamonds',44:'Jack_of_Hearts',
        45:'Queen_of_Spades', 46:'Queen_of_Clubs', 47:'Queen_of_Diamonds',48:'Queen_of_Hearts',
        49:'King_of_Spades', 50:'King_of_Clubs', 51:'King_of_Diamonds', 52: 'King_of_Hearts'}


class Player():
    def __init__(self, name = ""):
        self.deck = []
        self.play_status = True 
        self.name = name
        self.position = ()
    def __str__(self):
        return self.name 

class Game():
    def __init__(self, list_of_players = [], number_of_players = 0):
        self.list_of_players = list_of_players
        self.number_of_players = number_of_players
        self.winner = ''
        # create players 
        if number_of_players == 1:
            self.player1 = Player("Player1")
            self.player1.position = (WINDOW_SIZE[0] // 2, WINDOW_SIZE - (WINDOW_SIZE[1] // 10))
        if number_of_players == 2:
            self.player1 = Player("Player1")
            self.player1.position = (WINDOW_SIZE[0] // 10, WINDOW_SIZE[1] // 2)
            self.player2 = Player("Player2")
            self.player2.position = (WINDOW_SIZE[0] - (WINDOW_SIZE[0] // 10), WINDOW_SIZE[1] // 2)
        if number_of_players == 3:
            self.player1 = Player("Player1")
            self.player1.position = 
            self.player2 = Player("Player2")
            self.player2.position = 
            self.player3 = Player("Player3")
            self.player3.position = 
        if number_of_players == 4:
            self.player1 = Player("Player1")
            self.player1.position = 
            self.player2 = Player("Player2")
            self.player2.position = 
            self.player3 = Player("Player3")
            self.player3.position = 
            self.player4 = Player("Player4")
            self.player4.position = 

    def check_winners(self):
        for player in self.list_of_players:
            if player.deck == []:
                winner = str(player)
                return str(player)
            
              
# DISPLAY TEXT BOX FOR PLAYER NUMBER ENTRY
# https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame 

# UPDATE LIST OF PLAYERS AND NUMBER OF PLAYERS




players = [] 
player1 = Player("Gerald")
players.append(player1)
player2 = Player("Jimmy")
players.append(player2)
player3 = Player("Angel")
players.append(player3)
player4 = Player("Lavi")
players.append(player4)




#display text box for "master user" to install 
print("""
    Welcome to the Pygame adaptation of 13!
                by Braxton Goss

From Wikipedia: Tiến lên, also known as Vietnamese 
cards, Thirteen, Poison, Killer 13, Bomb, is a 
shedding-type card game popular in Vietnam. 
It is derived from Chinese card games Winner, 
which uses a specially printed deck of cards, and Big Two.
    """)
def requestPlayers():
    done = False
    while not done: 
        playersChoice = input("Please enter the number of players: ")
        try:
            if int(playersChoice) <= 4 and int(playersChoice) >= 1:
                return int(playersChoice)
            elif int(playersChoice) > 4:
                print("Oops! That is too many players! \nRemember, this game can only be played with 4 people MAXIMUM!\n")
            elif int(playersChoice) < 1:
                print("Now, how the heck am I supposed to start your game with that few people? Try again.\n")
        except ValueError:
            print("That is just NOT a valid input, try again...\n")
    
number_of_players = requestPlayers()

# start game 
game = Game(players, number_of_players)
rect_dimensions = WINDOW_SIZE[0] // 4



def redrawWindow():
    pygame.display.update()

#start game
pygame.init() 
icon = pygame.image.load("card_images/cardsInHand.png")
pygame.display.set_caption("Card Game: 13 by Braxton Goss")
pygame.display.set_icon(icon)
display = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
display.fill(BLACK)


def main():
    RUN = True
    while RUN: 
        # event fetching
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                RUN = False
                break
            elif event.type == pygame.KEYDOWN:
                pass
            # get position of mouse
            pos = pygame.mouse.get_pos()
            pressed = pygame.mouse.get_pressed()

            if pos[0] <= (WINDOW_SIZE[0] // 2) and pressed[0]:
                # generate random card
                cardNumber = random.randint(1, 52)
                cardImage = pygame.image.load('card_images/' + cards[cardNumber] + '.jpg')

                # draw card to screen 
                display.blit(cardImage, (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
        redrawWindow()


main() 

    # # testing ANIMATION 
    # player = pygame.image.load("cards.png")
    # position = player.get_rect()
    # display.blit(player, position)          #draw the player
    # pygame.display.update()                #and show it all
    # for x in range(100):                   #animate 100 frames
    #     display.fill(WHITE)
    #     position = position.move(2, 0)     #move player
    #     display.blit(player, position)      #draw new player
    #     pygame.display.update()            #and show it all
    #     pygame.time.delay(100)             #stop the program for 1/10 second