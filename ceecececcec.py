
from pygame import *
from random import *
kill = 0
window = display.set_mode((700, 500))
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
window = display.set_mode((700, 500))
FPS = 60
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
clock = time.Clock()
game = True
class GameSprite(sprite.Sprite):
        def __init__(self, player_image, player_speed, player_x, player_y, width, height):
            super().__init__()
            self.image = transform.scale(image.load(player_image), (width, height))
            self.speed = player_speed
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y

        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 595:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet('bullet.png', 10,self.rect.centerx, self.rect.top,  20, 25 )
        Bullets.add(bullet)

lost = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = randint(0,650)
            lost = lost + 1


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()

hero = Player('rocket.png', 10, 450, 380, 65 , 120)
ufo = Enemy('ufo.png', randint (2, 6),randint(100, 600),200, 40, 65 )
ufo1 = Enemy('ufo.png', randint (2, 6),randint(100, 600),200, 40, 65 )
ufo2 = Enemy('ufo.png', randint (2, 6),randint(100, 600),200, 40, 65 )
ufo3 = Enemy('ufo.png', randint (2, 6),randint(100, 600),200, 40, 65 )
ufo4 = Enemy('ufo.png', randint (2, 6),randint(100, 600),200, 40, 65 )
ufo5 = Enemy('ufo.png', randint (2, 6),randint(100, 600),200, 40, 65 )

monsters = sprite.Group()
monsters.add(ufo)
monsters.add(ufo1)
monsters.add(ufo2)
monsters.add(ufo3)
monsters.add(ufo4)
monsters.add(ufo5)
Bullets = sprite.Group()

font.init()
font1  =font.Font('ИArial', 36)

finished = False
while game:

    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                #fire_sound.play()
                hero.fire()
    if finished != True:
        window.blit(background, (0, 0))
        monsters.draw(window)
        Bullets.draw(window)
        text_lose = font1.render("Пропущено:" + str(lost), 1, (255, 255, 255))
        text_killed = font1.render("Убито:" + str(kill), 1, (255, 255, 255))
        window.blit(text_lose, (20, 20))
        window.blit(text_killed, (40, 40))
        Bullets.update()
        hero.reset()
        hero.update()
        ufo.reset()
        ufo.update()
        sprites_list = sprite.groupcollide(monsters, Bullets, True, True)
        for i in sprites_list:
            kill = kill+1
            ufo = Enemy('ufo.png', randint(2, 6), randint(100, 600), 0, 40, 65)
            monsters.add(ufo)
        if kill > 10:
            finished = True
            win = font1.render("Победа" , 1, (255, 255, 255))
            window.blit(win, (350, 200))

        if lost > 20:
            finished = True
            win = font1.render("Поражение", 1, (255, 255, 255))
            window.blit(win, (350, 200))
        display.update()
        monsters.update()
