#Создай собственный Шутер!
''''from pygame import *
from random import randint


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_mode((win_width, win_height))
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
font.init()
font1 = font.Font(None, 36)
win = font1.render('YOU WIN', True,(255,255,255))
lose = font1.render('YOU LOSE', True,(180, 0, 0))
font2 = font.Font(None, 36 )

score = 0
lost = 0
max_lost = 3
goal = 10



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (55, 55))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
            bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
            bullets.add(bullet)

class Enemy(GameSprite):
    def update (self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1



class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

monsters = sprite.Group()
ship = Player('rocket.png', 5, win_height - 100, 80, 100, 10)
Enemies = sprite.Group()
bullets = sprite.Group()
finish = False
#основной цикл игры:
for i in range(1, 6):
    monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)
bullets = sprite.Group()
#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
#основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
   #событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
       #событие нажатия на пробел - спрайт стреляет
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()
 #сама игра: действия спрайтов, проверка правил игры, перерисовка
    if not finish:
       #обновляем фон
        window.blit(background,(0,0))
 
       #производим движения спрайтов
        ship.update()
        monsters.update()
        bullets.update()
 
       
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)

        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
           #этот цикл повторится столько раз, сколько монстров подбито
            score = score + 1
            monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)
 
       #возможный проигрыш: пропустили слишком много или герой столкнулся с врагом
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True #проиграли, ставим фон и больше не управляем спрайтами.
            window.blit(lose, (200, 200))
 
       #проверка выигрыша: сколько очков набрали?
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))
 
       #пишем текст на экране
        text = font2.render("Счет: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))
 
        text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))
 
        display.update()
        time.delay(50)'''

from pygame import *
from random import randint


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_mode((win_width, win_height))
background = transform.scale(image.load("plate.png"), (800, 600))

mixer.init()
fire_sound = mixer.Sound('fire.ogg')
font.init()
font1 = font.SysFont('Arial', 36)
win = font1.render('похавал', True,(0, 255, 0))
lose = font1.render('ГОЛОДНЫЙ остался', True,(180, 0, 0))
font2 = font.SysFont('Arial', 36 )

score = 0
lost = 0
max_lost = 3
goal = 10



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
            bullet = Bullet('fork.png', self.rect.centerx, self.rect.top, 130, 90, -15)
            bullets.add(bullet)

class Enemy(GameSprite):
    def update (self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1



class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

monsters = sprite.Group()
ship = Player('opened_mouth-removebg-preview.png', 5, win_height - 180, 140, 140, 10)
Enemies = sprite.Group()
bullets = sprite.Group()
finish = False
#основной цикл игры:
for i in range(1, 6):
    monster = Enemy('pelmen.jpg', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)
bullets = sprite.Group()
#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
#основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
   #событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
       #событие нажатия на пробел - спрайт стреляет
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()
 #сама игра: действия спрайтов, проверка правил игры, перерисовка
    if not finish:
       #обновляем фон
        window.blit(background,(0,0))
 
       #производим движения спрайтов
        ship.update()
        monsters.update()
        bullets.update()
 
       
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)

        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
           #этот цикл повторится столько раз, сколько монстров подбито
            score = score + 1
            monster = Enemy('pelmen.jpg', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)
 
       #возможный проигрыш: пропустили слишком много или герой столкнулся с врагом
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True #проиграли, ставим фон и больше не управляем спрайтами.
            window.blit(lose, (200, 200))
 
       #проверка выигрыша: сколько очков набрали?
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))
 
       #пишем текст на экране
        text = font2.render("Счет: " + str(score), 1, (0, 0, 255))
        window.blit(text, (10, 20))
 
        text_lose = font2.render("Пропущено: " + str(lost), 1, (0, 0, 255))
        window.blit(text_lose, (10, 50))
 
        display.update()
        time.delay(50)