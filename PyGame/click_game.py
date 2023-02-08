blob = Actor('draft')
blob.pos = 100, 50

WIDTH = 500
HEIGHT = blob.height + 20

def draw():
    screen.fill((128,0,0))
    blob.draw()

def update():
    blob.left = blob.left + 2
    if blob.left > WIDTH:
        blob.right = 0
