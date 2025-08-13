import pygame
from objetos import Item

class Bau:
    def __init__(self, x, y, size=50):
        self.rect = pygame.Rect(x, y, size, size)
        self.size = size

        # Carrega imagens do bau (bau0 a bau4)
        self.images = [pygame.image.load(f"bau{i}.png").convert_alpha() for i in range(5)]
        self.images = [pygame.transform.scale(img, (size, size)) for img in self.images]

        self.current_image = self.images[0]  # imagem inicial bau0
        self.hits = 0
        self.destroyed = False

    def draw(self, screen):
        if not self.destroyed:
            screen.blit(self.current_image, self.rect)

    def hit(self):
        """Chama quando leva um tiro. Retorna um Item ou None."""
        if self.destroyed:
            return None

        self.hits += 1

        if self.hits < len(self.images):
            self.current_image = self.images[self.hits]

            # bau1 libera item de vida
            if self.hits == 1:
                return Item(self.rect.centerx, self.rect.centery, color=(0,255,0), kind='vida')

            # bau2,3,4 liberam outros itens
            elif 2 <= self.hits <= 4:
                colors_map = [(255,0,255), (0,0,255), (255,255,0)]
                color = colors_map[self.hits - 2]
                return Item(self.rect.centerx, self.rect.centery, color=color)

            return None
        else:
            # marca como destruído mas não retorna item
            self.destroyed = True
            return None
