import pgzrun
from random import randint
WIDTH=600
HEIGHT=600
TITLE='RECTANGLE'

def draw():
    width=400
    height=HEIGHT-200
    r=255
    g=10
    b=randint(0,255)
    screen.fill('blue')
    for i  in range (20):
        rectangle=Rect((0,0),(width,height))
        rectangle.center=250,250
        screen.draw.rect(rectangle,(r,g,b))
        width-=10
        height+=10
        r-=10
        g+=10

def update():
    pass




























pgzrun.go()