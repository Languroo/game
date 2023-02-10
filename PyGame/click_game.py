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
def on_mouse_down(pos):
    if blob.collidepoint(pos):
        set_blob_hurt()
def set_blob_hurt():
    blob.image = 'hurt'
    sounds.eep.play()
    clock.schedule_unique(set_blob_normal, 1.0)
def set_blob_normal():
    blob.image = 'draft'
