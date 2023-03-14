import pyglet
pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

def center_img(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2

player_img = pyglet.resource.image("player.png")
center_img(player_img)
bullet_img = pyglet.resource.image("bullet.png")
center_img(bullet_img)
asteroid_img = pyglet.resource.image("asteroid.png")
center_img(asteroid_img)