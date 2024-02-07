from pygame import *

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, x, y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

window = display.set_mode((700, 500))
window.fill((200, 200, 255))
display.set_caption('ping pong game')

racket_l = Player('racket.png', 30, 200, 4, 50, 150)
racket_r = Player('racket.png', 620, 200, 4, 50, 150)
tennis_ball = GameSprite('tennis_ball.jpeg', 200, 200, 4, 50, 50)

font.init()
font1 = font.Font(None, 70)
lose1 = font1.render('left player loses!!', True, (0, 200, 200))
lose2 = font1.render('right player loses!!', True, (255, 0, 0))

speed_x = 3
speed_y = 3

player1_score = 0
player2_score = 0
font2 = font.Font(None, 25)

game = True
clock = time.Clock()
FPS = 60
finish = False

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill((200, 200, 255))
        window.blit(font2.render(str(player1_score), True, (200, 255, 0)), (30, 30))
        window.blit(font2.render(str(player2_score), True, (200, 255, 0)), (620, 30))
        racket_l.update_l()
        racket_r.update_r()
        tennis_ball.rect.x += speed_x
        tennis_ball.rect.y += speed_y

        if sprite.collide_rect(racket_l, tennis_ball) or sprite.collide_rect(racket_r, tennis_ball):
            speed_x *= -1
            speed_y *= 1

        if tennis_ball.rect.y > 500 - 50 or tennis_ball.rect.y < 0:
            speed_y *= -1

        if tennis_ball.rect.x < 0:
            
            # window.blit(lose1, (150, 200))
            player2_score += 1
            if player2_score == 10:
                window.blit(lose1, (200, 100))
                finish = True
            window.blit(font2.render(str(player2_score), True, (200, 255, 0)), (620, 30))
            tennis_ball.rect.x = 200
            tennis_ball.rect.y = 200
            

        if tennis_ball.rect.x > 700:
            
            # window.blit(lose2, (150, 200))
            player1_score += 1
            if player1_score == 10:
                window.blit(lose2, (200, 100))
                finish = True
            window.blit(font2.render(str(player1_score), True, (200, 255, 0)), (30, 30))
            tennis_ball.rect.x = 200
            tennis_ball.rect.y = 200

        racket_l.reset()
        racket_r.reset()
        tennis_ball.reset()
    display.update()
    clock.tick(FPS)