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
        self.image = transform.scale(image.load(img),(width, height))
        self.speed = 4
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y + self.rect.height < SCREENSIZE[1]:
            self.rect.y += self.speed

    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y + self.rect.height < SCREENSIZE[1]:
            self.rect.y += self.speed

platform_left = player('platform.png',20,320,4,25,99)
platform_right = player('platform.png',660,320,4,25,99)


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False


    window.fill(BACKCOLOR)



    platform_left.reset()
    platform_right.reset()

    platform_left.update_left()
    platform_right.update_right()


    


    display.update()
    timer.tick(60)

