from graph import *


def paint_foundation(x, y, width, foundation_height):
    pass

def paint_walls(x,y, width, eight):
    pass

def paint_roof(x,y, width, height): 
    pass
    


def paint_house(x, y, width, height):

    foundation_height = int(height* 0.1)
    walls_height = int(height * 0.5)
    roof_height = height - foundation_height - walls_height

    paint_foundation(x, y + walls_height, width, foundation_height)
    paint_walls(x,y, width, walls_height)
    paint_roof(x,y, width, roof_height)
    

def main():
    paint_house(150, 150, 120, 100)
    run()


main()