import pygame
import random
from settings import *

class Bot:
    def __init__(self, x, y, width=80, height=80, speed=3, lives=3):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.lives = lives

        # projétil
        self.projectile = None
        self.projectile_speed = 7

        # imagens
        self.image_idle = pygame.image.load("bot1.png").convert_alpha()
        self.image_idle = pygame.transform.scale(self.image_idle, (width, height))
        self.image_walk = pygame.image.load("bot2.png").convert_alpha()
        self.image_walk = pygame.transform.scale(self.image_walk, (width, height))
        self.image_shoot = pygame.image.load("bot3.png").convert_alpha()
        self.image_shoot = pygame.transform.scale(self.image_shoot, (width, height))
        self.image_destroyed = pygame.image.load("bot4.png").convert_alpha()
        self.image_destroyed = pygame.transform.scale(self.image_destroyed, (width, height))

        # estado: 'idle', 'walk', 'shoot', 'dead'
        self.state = 'idle'
        self.current_image = self.image_idle

        # movimento vertical
        self.direction_y = random.choice([-1, 1])

    def update(self, screen_width, screen_height):
        if self.state == 'dead':
            # não se move se estiver morto
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

        # atualiza a imagem de acordo com o estado
        self.update_image()

    def update_image(self):
        if self.state == 'idle':
            self.current_image = self.image_idle
        elif self.state == 'walk':
            self.current_image = self.image_walk
        elif self.state == 'shoot':
            self.current_image = self.image_shoot
        elif self.state == 'dead':
            self.current_image = self.image_destroyed

    def draw(self, screen):
        screen.blit(self.current_image, self.rect)
        if self.projectile:
            pygame.draw.rect(screen, (255, 0, 0), self.projectile)

    def shoot(self):
        if not self.projectile and self.state != 'dead':
            self.projectile = pygame.Rect(self.rect.left - 10, self.rect.centery - 5, 10, 10)
            self.state = 'shoot'
            self.update_image()

    def check_collision_with_hero(self, hero):
        if self.projectile and self.projectile.colliderect(hero.rect):
            hero.lives -= 1
            self.projectile = None
            if self.state != 'dead':
                self.state = 'idle'
                self.update_image()

    def hit(self):
        """Reduz vida e retorna True se morrer"""
        if self.state == 'dead':
            return False
        self.lives -= 1
        if self.lives <= 0:
            self.state = 'dead'
            self.update_image()
            return True
        return False
