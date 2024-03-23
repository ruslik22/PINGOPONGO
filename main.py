from pygame import *

SCREENSIZE = (700, 700)
BACKCOLOR = (255, 255, 255)

window = display.set_mode(SCREENSIZE)
display.set_caption('ping pong')

timer = time.Clock()

run = True

class GameSprite(sprite.Sprite):
    def __init__ (self, img, x, y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(img), width, height)
        self.speed = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class player(GameSprite):
    def update_left(self):
        keys = key_pressed()
        if keys[K_w] and self.rect.y >0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y + self.rect.height < SCREENSIZE[1]:
            self.rect.y -= self.speed

    def update_right(self):
        keys = key_pressed()
        if keys[K_w] and self.rect.y >0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y + self.rect.height < SCREENSIZE[1]:
            self.rect.y -= self.speed



while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.fill(BACKCOLOR)
    display.update()
    timer.tick(60)

