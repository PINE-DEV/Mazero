# About mazes: http://www.astrolog.org/labyrnth/algrithm.htm#perfect
# Wiki for maze generation algols: https://en.wikipedia.org/wiki/Maze_generation_algorithm

# About graphs: https://en.wikipedia.org/wiki/Graph_(abstract_data_type)

# About procedural content generator: http://pcg.wikidot.com/what-pcg-is
#def __recursiveBacktracker__(width, height):

from MazeGraph import *

class Maze:
    def __init__(self, width, height, mazeGraph):
        self.width = width
        self.height = height
        self.mazeGraph = mazeGraph

    def isValidMove(self, originCell, destinationCell):
        """Adjacent: Returns true if the move is valid"""

    def getMovableCells(self, originCell):
        """Neighbors: Returns an array of cells adjacent to the origin where you can move to"""

    def drawMaze(self, canvas, offset, walledTile, pathTile): # Save offset+tile in maze vs provide them each time (maybe provide them is better)
        """draws the maze on the given canvas"""
        for x in range(self.width):
            for y in range(self.height):
                drawX = x * walledTile.width + offset.x
                drawY = y * walledTile.height + offset.y
                canvas.drawTile(walledTile, drawX, drawY)

        for cellA, cellB in self.mazeGraph.getEdges():
            Ax = cellA.x * walledTile.width
            Ay = cellA.y * walledTile.height
            Bx = cellB.x * walledTile.width
            By = cellB.y * walledTile.height
            drawX = Ax + offset.x + (Bx - Ax) / 2
            drawY = Ay + offset.y + (By - Ay) / 2
            canvas.drawTile(pathTile, drawX, drawY)

class Canvas:
    def __init__(self, screen):
        self.screen = screen
    def drawTile(self, tile, x, y):
        rect = pygame.Rect(x - tile.width / 2, y - tile.height / 2, tile.width, tile.height)
        self.screen.blit(tile.sprite, rect)

class Tile:
    def __init__(self, sprite):
        self.width = sprite.get_rect().width
        self.height = sprite.get_rect().height
        self.sprite = sprite

# INIT GAME STUFF:
import sys

import pygame

pygame.init()
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)

walledSprite = pygame.image.load("walledSprite.png")
pathSprite = pygame.image.load("pathSprite.png")

mazeGraph = MazeGraph(12, 9)
maze = Maze(12, 9, mazeGraph)
canvas = Canvas(screen)
walledTile = Tile(walledSprite)
pathTile = Tile(pathSprite)
offset = Cell(walledTile.width,walledTile.height) # Maybe not use Cell?. I just need something with an x and a y, it could be a dictionary, really

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0,0,0))
    maze.drawMaze(canvas, offset, walledTile, pathTile)
    pygame.display.flip()
