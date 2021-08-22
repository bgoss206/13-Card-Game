import pygame
import os
import numpy as np
import random 
import math 

# Colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)
WINDOW_SIZE = [1000, 1000]
rect_height = WINDOW_SIZE[1] // 4
rect_width = WINDOW_SIZE[0] // 2
button_height = WINDOW_SIZE[1] // 10
button_width = WINDOW_SIZE[0] // 5 
playing_area_height = WINDOW_SIZE[1] // 3
playing_area_width = WINDOW_SIZE[0] // 3

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
    def __init__(self, rect, name = ""):
        self.deck = []
        self.play_status = True 
        self.name = name
        self.rect = rect  # rect parameters: top left of rectangle (x, y, width, height)
    def __str__(self):
        return self.name 

class Game():
    def __init__(self, number_of_players = 0):
        self.list_of_players = []
        self.number_of_players = number_of_players

        # create players 
        if number_of_players == 1:
            self.list_of_players.append(Player(pygame.Rect(WINDOW_SIZE[0] // 2 - (rect_width // 2), WINDOW_SIZE[1] - (rect_height // 2), rect_width, rect_height), "Player1")) # buttom 
        if number_of_players == 2:
            self.list_of_players.append(Player(pygame.Rect(WINDOW_SIZE[0] // 2 - (rect_width // 2), WINDOW_SIZE[1] - (rect_height // 2), rect_width, rect_height), "Player1")) # bottom
            self.list_of_players.append(Player(pygame.Rect(WINDOW_SIZE[0] // 2 - (rect_width // 2), -rect_height // 2, rect_width, rect_height), "Player2")) # top
        if number_of_players == 3:
            self.list_of_players.append(Player(pygame.Rect(WINDOW_SIZE[0] // 2 - (rect_width // 2), WINDOW_SIZE[1] - (rect_height // 2), rect_width, rect_height), "Player1")) # bottom
            self.list_of_players.append(Player(pygame.Rect(WINDOW_SIZE[0] // 2 - (rect_width // 2), -rect_height // 2, rect_width, rect_height), "Player2")) # top
            self.list_of_players.append(Player(pygame.Rect(-rect_height // 2, (WINDOW_SIZE[1] // 2) - (rect_width // 2), rect_height, rect_width), "Player3")) # left
        if number_of_players == 4:
            self.list_of_players.append(Player(pygame.Rect(WINDOW_SIZE[0] // 2 - (rect_width // 2), WINDOW_SIZE[1] - (rect_height // 2), rect_width, rect_height), "Player1")) # bottom
            self.list_of_players.append(Player(pygame.Rect(WINDOW_SIZE[0] // 2 - (rect_width // 2), -rect_height // 2, rect_width, rect_height), "Player2")) # top
            self.list_of_players.append(Player(pygame.Rect(-rect_height // 2, (WINDOW_SIZE[1] // 2) - (rect_width // 2), rect_height, rect_width), "Player3")) # left 
            self.list_of_players.append(Player(pygame.Rect(WINDOW_SIZE[0] - (rect_height // 2), (WINDOW_SIZE[1] // 2) - (rect_width // 2), rect_height, rect_width), "Player4")) # right

    def check_winners(self):
        for player in self.list_of_players:
            if player.deck == []:
                winner = str(player)
                return winner 
            
              
# DISPLAY TEXT BOX FOR PLAYER NUMBER ENTRY
# https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame 

# UPDATE LIST OF PLAYERS AND NUMBER OF PLAYERS


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
game = Game(number_of_players)

def drawCards(rotation, player, display):
    # CHANGE ROTATION ADDITION VS SUBTRACTION 
    for card in range(len(player.deck)):
        card_image = pygame.image.load('card_images/' + player.deck[card] + '.jpg')
        new_image = pygame.transform.rotate(card_image, rotation)
        if rotation == 0:
            display.blit(new_image, (player.rect.x + ((card_image.get_width() // 2) * card), player.rect.y)) 
        elif rotation == 90:
            display.blit(new_image, (player.rect.x, player.rect.y + ((card_image.get_width() // 2) * card)))
        elif rotation == 180:
            display.blit(new_image, (player.rect.x + ((card_image.get_width() // 2) * card), player.rect.y + (rect_height * 0.65)))
        elif rotation == 270:
            display.blit(new_image, (player.rect.x + (rect_height * 0.65), player.rect.y + ((card_image.get_width() // 2) * card)))

def redrawWindow():
    pygame.display.update()

#start game
pygame.init() 
icon = pygame.image.load("card_images/cardsInHand.png")
pygame.display.set_caption("Card Game: 13 by Braxton Goss")
pygame.display.set_icon(icon)
display = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
display.fill(BLACK)


# player sectors
for players in game.list_of_players:
    rect = players.rect
    pygame.draw.ellipse(display, WHITE, rect)

# start button (x, y, width, height)
# start text within start button 
start_button = pygame.Rect(WINDOW_SIZE[0] // 2 - (button_width // 2), WINDOW_SIZE[1] - (WINDOW_SIZE[1] // 4), button_width, button_height)
pygame.draw.rect(display, (255, 0, 0), start_button)
font = pygame.font.SysFont("algerian", 32, bold=True)
label = font.render("START", 1, BLACK)
display.blit(label, (start_button.x + (start_button.width // 4) - (start_button.width // 20), start_button.y + (start_button.height // 3)))




# in-play pile 
play_pile = pygame.Rect(WINDOW_SIZE[0] // 2 - (playing_area_width // 2), WINDOW_SIZE[1] // 2 - (playing_area_width // 2), playing_area_width, playing_area_height)
pygame.draw.rect(display, (0, 0, 255), play_pile, width = 5)

def main():
    RUN = True
    while RUN: 
        # event fetching
        for event in pygame.event.get():

            # get position of mouse
            pos = pygame.mouse.get_pos()
            pressed = pygame.mouse.get_pressed()

            if event.type == pygame.QUIT:
                pygame.quit()
                RUN = False
            elif event.type == pygame.KEYDOWN:
                pass
            
            # if start button is pressed down with leftmousebutton (pressed[0])
            if pressed[0] and start_button.collidepoint(pos):
                
                # remove start button
                display.blit()

                # VIRTUALLY: give players the cards 
                for player in game.list_of_players:
                    while len(player.deck) < 13:
                        # generate random card NOTE: [*cards] returns a list of all keys in dictionary
                        cardNumber = random.choice([*cards])
                        
                        # add random card to player's deck 
                        player.deck.append(cards[cardNumber])

                        # remove played card from the choices in dictionary
                        del cards[cardNumber]

                # VISUALLY: give players the cards 
                for player in game.list_of_players:
                    current_player = str(player)
                    # bottom player
                    if current_player == "Player1":
                        drawCards(0, player, display)
                    # top player
                    if current_player == "Player2": 
                        rotation = 180
                        drawCards(rotation, player, display)
                    # left - player3 
                    if current_player == "Player3": 
                        rotation = 270
                        drawCards(rotation, player, display)
                    # right - player4 
                    if current_player == "Player4": 
                        rotation = 90
                        drawCards(rotation, player, display)




             # fetch image
             # 
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