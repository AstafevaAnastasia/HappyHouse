# importing the required libraries

import pygame as pg
import sys
import time
from pygame.locals import *

# declaring the global variables

# for storing the 'x' or 'o'
# value as character
XO = 'x'

# storing the winner's value at
# any instant of code
winner = None

# to check if the game is a draw
draw = None

# to set width of the game window
width = 400

# to set height of the game window
height = 400

# to set background color of the
# game window
white = (255, 255, 255)

# color of the straightlines on that
# white game board, dividing board
# into 9 parts
line_color = (0, 0, 0)

# setting up a 3 * 3 board in canvas
board = [[None]*3, [None]*3, [None]*3]


# initializing the pygame window
pg.init()

# setting fps manually
fps = 30

# this is used to track time
CLOCK = pg.time.Clock()

# this method is used to build the
# infrastructure of the display
screen = pg.display.set_mode((width, height + 100), 0, 32)

# setting up a nametag for the
# game window
pg.display.set_caption("My Tic Tac Toe")

# loading the images as python object
initiating_window = pg.image.load("modified_cover.png")
x_img = pg.image.load("X_modified.png")
y_img = pg.image.load("o_modified.png")

# resizing images
initiating_window = pg.transform.scale(
    initiating_window, (width, height + 100))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(y_img, (80, 80))

#
# def game_initiating_window():
#
#     # displaying over the screen
#     screen.blit(initiating_window, (0, 0))
#
#     # updating the display
#     pg.display.update()
#     time.sleep(3)
#     screen.fill(white)
#
#     # drawing vertical lines
#     pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
#     pg.draw.line(screen, line_color, (width / 3 * 2, 0),
#                  (width / 3 * 2, height), 7)
#
#     # drawing horizontal lines
#     pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
#     pg.draw.line(screen, line_color, (0, height / 3 * 2),
#                  (width, height / 3 * 2), 7)
#     draw_status()
#
#
# def draw_status():
#
#     # getting the global variable draw
#     # into action
#     global draw
#
#     if winner is None:
#         message = XO.upper() + "'s Turn"
#     else:
#         message = winner.upper() + " won !"
#     if draw:
#         message = "Game Draw !"
#
#     # setting a font object
#     font = pg.font.Font(None, 30)
#
#     # setting the font properties like
#     # color and width of the text
#     text = font.render(message, 1, (255, 255, 255))
#
#     # copy the rendered message onto the board
#     # creating a small block at the bottom of the main display
#     screen.fill((0, 0, 0), (0, 400, 500, 100))
#     text_rect = text.get_rect(center=(width / 2, 500-50))
#     screen.blit(text, text_rect)
#     pg.display.update()