import pygame
from settings import *
from efeitos_sonoros import *

HERO_PATH = "imagens/cowboy/"

class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = 5
        self.lives = 3
        self.max_lives = 3

        # projétil
        self.projectile = None
        self.projectile_speed = 10

        # imagens
        self.image_idle = pygame.image.load(HERO_PATH + "cowboy_andando1.png").convert_alpha()
        self.image_idle = pygame.transform.scale(self.image_idle, (self.width, self.height))

        self.images_walk = [pygame.image.load(HERO_PATH + f"cowboy_andando{i}.png").convert_alpha() for i in range(1, 3)]
        self.images_walk = [pygame.transform.scale(img, (self.width, self.height)) for img in self.images_walk]

        self.images_shoot = [pygame.image.load(HERO_PATH + f"cowboy_atirando{i}.png").convert_alpha() for i in range(1, 5)]
        self.images_shoot = [pygame.transform.scale(img, (self.width, self.height)) for img in self.images_shoot]

        self.current_image = self.image_idle
        self.walk_index = 0
        self.shoot_index = 0

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
            self.current_image = self.images_shoot[self.shoot_index]
            self.shoot_index = (self.shoot_index + 1) % len(self.images_shoot)
        elif moved:
            self.current_image = self.images_walk[self.walk_index]
            self.walk_index = (self.walk_index + 1) % len(self.images_walk)
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
            tiro_som.play()
            
    def update_projectile(self):
        if self.projectile:
            self.projectile.x += self.projectile_speed
            if self.projectile.x > 800:
                self.projectile = None
