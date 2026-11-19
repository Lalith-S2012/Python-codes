import pygame

def main():
    pygame.init()
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('color changing sprite')

    colors = {
        'red' : pygame.Color('red'),
        'blue' : pygame.Color('blue'),
        'white' : pygame.Color('white'),
        'purple' : pygame.Color('purple'),
    }