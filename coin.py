import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400
score = 0
game_over = False
fox = Actor("fox")
fox.pos = 100, 100
coin = Actor("coin")
coin.pos = 200, 200

# DRAW FUNCTION

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color = "black", topleft = (10, 10))
    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft = (10, 10), fontsize = 60)
    
# OTHER FUNCTIONS

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    
    if keyboard.left:
        fox.x = fox.x - 2
    elif keyboard.right:
        fox.x = fox.x + 2
    elif keyboard.up:
        fox.y = fox.y - 2
    elif keyboard.down:
        fox.y = fox.y + 2

    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score = score + 1
        place_coin()


clock.schedule(time_up, 60.0)
place_coin()

pgzrun.go()
