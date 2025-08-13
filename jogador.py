import pygame
from settings import *

class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = 5
        self.lives = 3

        # projétil
        self.projectile = None
        self.projectile_speed = 10

        # imagens
        self.image_idle = pygame.image.load("heroi1.png").convert_alpha()
        self.image_idle = pygame.transform.scale(self.image_idle, (self.width, self.height))
        self.image_walk = pygame.image.load("heroi2.png").convert_alpha()
        self.image_walk = pygame.transform.scale(self.image_walk, (self.width, self.height))
        self.image_shoot = pygame.image.load("heroi3.png").convert_alpha()
        self.image_shoot = pygame.transform.scale(self.image_shoot, (self.width, self.height))
        self.current_image = self.image_idle

        # retângulo para colisão
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        moved = False
        shooting = False

        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            moved = True
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
            moved = True
        if keys[pygame.K_UP]:
            self.y -= self.speed
            moved = True
        if keys[pygame.K_DOWN]:
            self.y += self.speed
            moved = True
        if keys[pygame.K_SPACE]:
            self.shoot()
            shooting = True

        # Atualiza a imagem do herói
        if shooting:
            self.current_image = self.image_shoot
        elif moved:
            self.current_image = self.image_walk
        else:
            self.current_image = self.image_idle

        # Atualiza retângulo
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.current_image, (self.x, self.y))
        if self.projectile:
            pygame.draw.rect(screen, (255, 255, 0), self.projectile)

    def shoot(self):
        if not self.projectile:
            self.projectile = pygame.Rect(self.x + self.width, self.y + self.height//2 - 5, 10, 10)

    def update_projectile(self):
        if self.projectile:
            self.projectile.x += self.projectile_speed
            if self.projectile.x > 800:
                self.projectile = None
