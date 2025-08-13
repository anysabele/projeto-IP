import pygame
import random
from settings import *

BOT_PATH = "imagens/inimigos/"

class Bot:
    def __init__(self, x, y, width=80, height=80, speed=3, lives=3):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed * 0.75
        self.lives = lives

        # projétil
        self.projectile = None
        self.projectile_speed = 7

        # Carrega animações
        self.images_walk = [pygame.image.load(f"{BOT_PATH}bandido_andando{i}.png").convert_alpha() for i in range(1,3)]
        self.images_walk = [pygame.transform.scale(img, (width, height)) for img in self.images_walk]

        self.images_shoot = [pygame.image.load(f"{BOT_PATH}bandido_jogando_tnt{i}.png").convert_alpha() for i in range(1,4)]
        self.images_shoot = [pygame.transform.scale(img, (width, height)) for img in self.images_shoot]

        self.image_dead = pygame.image.load(f"{BOT_PATH}bandido_morto.png").convert_alpha()
        self.image_dead = pygame.transform.scale(self.image_dead, (width, height))

        # estado
        self.state = 'idle'
        self.current_image = self.images_walk[0]
        self.frame_index = 0
        self.frame_counter = 0

        # movimento vertical
        self.direction_y = random.choice([-1,1])

    def update(self, screen_width, screen_height):
        if self.state == 'dead':
            self.current_image = self.image_dead
            return

        # movimenta horizontal
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.left = screen_width
            self.rect.y = random.randint(0, screen_height - self.rect.height)
        
        # movimenta vertical
        self.rect.y += self.direction_y * self.speed
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.direction_y *= -1

        # projétil
        if self.projectile:
            self.projectile.x -= self.projectile_speed
            if self.projectile.right < 0:
                self.projectile = None
                if self.state != 'dead':
                    self.state = 'idle'

        # chance de disparar
        if not self.projectile and random.random() > 0.65:
            self.shoot()

        # animação
        self.animate()

    def animate(self):
        self.frame_counter += 1
        if self.frame_counter % 10 == 0:
            self.frame_index += 1
            if self.state == 'idle' or self.state == 'walk':
                self.current_image = self.images_walk[self.frame_index % len(self.images_walk)]
            elif self.state == 'shoot':
                self.current_image = self.images_shoot[self.frame_index % len(self.images_shoot)]

    def draw(self, screen):
        screen.blit(self.current_image, self.rect)
        if self.projectile:
            pygame.draw.rect(screen, (255, 0, 0), self.projectile)

    def shoot(self):
        if not self.projectile and self.state != 'dead':
            self.projectile = pygame.Rect(self.rect.left - 10, self.rect.centery - 5, 10, 10)
            self.state = 'shoot'
            self.frame_index = 0

    def check_collision_with_hero(self, hero):
        if self.projectile and self.projectile.colliderect(hero.rect):
            hero.lives -= 1
            self.projectile = None
            if self.state != 'dead':
                self.state = 'idle'

    def hit(self):
        if self.state == 'dead':
            return False
        self.lives -= 1
        if self.lives <= 0:
            self.state = 'dead'
            self.current_image = self.image_dead
            return True
        return False
