# YT Video link: https://youtu.be/WwH43__2mps

import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))

        # Grid constants
        squareSize = 32
        gridLength = squareSize * 20
        gridWidth = squareSize * 16
        color = "black"

        # Mole Initial Constants
        mole_x = 0
        mole_y = 0

        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")

            # drawing the vertical grid lines
            for x in range(0, gridLength + 1, squareSize):
                pygame.draw.line(screen, color, (x, 0), (x, gridWidth))

            # drawing the horizontal grid lines
            for y in range(0, gridWidth + 1, squareSize):
                pygame.draw.line(screen, color, (0, y), (gridLength, y))

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                clickedSquare_x = mouse_x // squareSize
                clickedSquare_y = mouse_y // squareSize

                if clickedSquare_x == mole_x and clickedSquare_y == mole_y:
                    mole_x = random.randrange(0, 20) # assign random x coordinate for square
                    mole_y = random.randrange(0, 16) # assign random y coordinate for square

            new_mole_x = mole_x * squareSize
            new_mole_y = mole_y * squareSize

            screen.blit(mole_image, mole_image.get_rect(topleft=(new_mole_x, new_mole_y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
