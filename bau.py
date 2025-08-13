import pygame
from objetos import Item
from sprites import Bau_dinamite, Bau_cactoazul, Bau_cactovermelho, Bau_ouro, Bau_medalha

class Bau:
    def __init__(self, x, y, size=50, type_index=0):
        self.rect = pygame.Rect(x, y, size, size)
        self.size = size
        self.hits = 0
        self.destroyed = False
        self.type_index = type_index

        # seleciona o sprite certo
        if type_index == 0:
            self.sprite = Bau_dinamite()
        elif type_index == 1:
            self.sprite = Bau_cactoazul()
        elif type_index == 2:
            self.sprite = Bau_cactovermelho()
        elif type_index == 3:
            self.sprite = Bau_ouro()
        elif type_index == 4:
            self.sprite = Bau_medalha()
        else:
            self.sprite = Bau_dinamite()

        self.sprite.rect.center = self.rect.center

    def draw(self, screen):
        if not self.destroyed:
            screen.blit(self.sprite.image, self.rect)

    def hit(self):
        """Chama quando leva um tiro. Retorna um Item ou None."""
        if self.destroyed:
            return None

        self.hits += 1
        # quando atinge 2 hits destrói
        if self.hits >= 2:
            self.destroyed = True
            return self.spawn_item()
        return None

    def spawn_item(self):
        """Cria o item correspondente ao tipo de baú."""
        item_kind = f"item{self.type_index + 1}"
        image_path = f"imagens/objetos/{item_kind}.png"
        return Item(self.rect.centerx, self.rect.centery, radius=25, kind=item_kind, image_path=image_path)
