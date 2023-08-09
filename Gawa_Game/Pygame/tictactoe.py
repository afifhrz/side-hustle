import random, pygame, sys
from pygame.locals import *

FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels
# REVEALSPEED = 8 # speed boxes' sliding reveals and covers
BOXSIZE = 130 # size of box height & width in pixels
# GAPSIZE = 10 # size of gap between boxes in pixels
BOARDWIDTH = 3 # number of columns of icons
BOARDHEIGHT = 3 # number of rows of icons
# assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE ))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE ))) / 2)

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
DIAMOND = 'diamond'

def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (BOXSIZE) + XMARGIN
    top = boxy * (BOXSIZE) + YMARGIN
    return (left, top)

def drawBoard(board, revealed):
    # Draws all of the boxes in their covered or revealed state.
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            if not revealed[boxx][boxy]:
                # Draw a covered box.
                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
            else:
                # Draw the (revealed) icon.
                shape, color = getShapeAndColor(board, boxx, boxy)
                drawIcon(shape, color, boxx, boxy)

def drawIcon(shape, color, boxx, boxy):
    quarter = int(BOXSIZE * 0.25) # syntactic sugar
    half =    int(BOXSIZE * 0.5)  # syntactic sugar

    left, top = leftTopCoordsOfBox(boxx, boxy) # get pixel coords from board coords
    # Draw the shapes
    if shape == DONUT:
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)
        pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top + half), quarter - 5)
    elif shape == DIAMOND:
        pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half)))

def getShapeAndColor(board, boxx, boxy):
    # shape value for x, y spot is stored in board[x][y][0]
    # color value for x, y spot is stored in board[x][y][1]
    return board[boxx][boxy][0], board[boxx][boxy][1]

def getRandomizedBoard():
    return [[,,],[,,],[,,]]

def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event
    pygame.display.set_caption('Tictactoe Game')

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelection = None # stores the (x, y) of the first box clicked.

    DISPLAYSURF.fill(BGCOLOR)
    startGameAnimation(mainBoard)

    while True: # main game loop
        mouseClicked = False

        DISPLAYSURF.fill(BGCOLOR) # drawing the window
        drawBoard(mainBoard, revealedBoxes)

        # for event in pygame.event.get(): # event handling loop
        #     if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
        #         pygame.quit()
        #         sys.exit()
        #     elif event.type == MOUSEMOTION:
        #         mousex, mousey = event.pos
        #     elif event.type == MOUSEBUTTONUP:
        #         mousex, mousey = event.pos
        #         mouseClicked = True

        # boxx, boxy = getBoxAtPixel(mousex, mousey)
        # if boxx != None and boxy != None:
        #     # The mouse is currently over a box.
        #     if not revealedBoxes[boxx][boxy]:
        #         drawHighlightBox(boxx, boxy)
        #     if not revealedBoxes[boxx][boxy] and mouseClicked:
        #         revealBoxesAnimation(mainBoard, [(boxx, boxy)])
        #         revealedBoxes[boxx][boxy] = True # set the box as "revealed"
        #         if firstSelection == None: # the current box was the first box clicked
        #             firstSelection = (boxx, boxy)
        #         else: # the current box was the second box clicked
        #             # Check if there is a match between the two icons.
        #             icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
        #             icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)

        #             if icon1shape != icon2shape or icon1color != icon2color:
        #                 # Icons don't match. Re-cover up both selections.
        #                 pygame.time.wait(1000) # 1000 milliseconds = 1 sec
        #                 coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
        #                 revealedBoxes[firstSelection[0]][firstSelection[1]] = False
        #                 revealedBoxes[boxx][boxy] = False
        #             elif hasWon(revealedBoxes): # check if all pairs found
        #                 gameWonAnimation(mainBoard)
        #                 pygame.time.wait(2000)

        #                 # Reset the board
        #                 mainBoard = getRandomizedBoard()
        #                 revealedBoxes = generateRevealedBoxesData(False)

        #                 # Show the fully unrevealed board for a second.
        #                 drawBoard(mainBoard, revealedBoxes)
        #                 pygame.display.update()
        #                 pygame.time.wait(1000)

        #                 # Replay the start game animation.
        #                 startGameAnimation(mainBoard)
        #             firstSelection = None # reset firstSelection variable

        # Redraw the screen and wait a clock tick.
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
if __name__ == '__main__':
    main()