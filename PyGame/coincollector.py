from random import randint
WIDTH = 400
HEIGHT = 400
score = 0
game_over = False
crab = Actor("crab")
crab.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill("green")
    crab.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

    if game_over:
        screen.fill("red")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global score

    if keyboard.left:
        crab.x = crab.x - 4
    elif keyboard.right:
        crab.x = crab.x + 4
    elif keyboard.up:
        crab.y = crab.y - 4
    elif keyboard.down:
        crab.y = crab.y + 4

    coin_collected = crab.colliderect(coin)

    if coin_collected:
        score = score + 10
        place_coin()

clock.schedule(time_up, 7.0)
place_coin()
