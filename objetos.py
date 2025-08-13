import pygame

class Trunk:
    def __init__(self, x, y, size=50, type_index=0):
        """
        type_index: 0 → bau1, 1 → bau2, 2 → bau3, 3 → bau4
        """
        self.rect = pygame.Rect(x, y, size, size)
        self.size = size
        self.hits = 0
        self.destroyed = False
        self.type_index = type_index

        # Carrega imagens dos baús
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(f"bau{i}.png").convert_alpha()
            img = pygame.transform.scale(img, (size, size))
            self.images.append(img)
        self.current_image = self.images[self.type_index]

    def draw(self, screen):
        if not self.destroyed:
            screen.blit(self.current_image, self.rect)

    def hit(self):
        """Conta um tiro. Retorna True se destruir o baú."""
        if self.destroyed:
            return False
        self.hits += 1
        if self.hits >= 2:
            self.destroyed = True
            return True
        return False

    def spawn_item(self):
        """
        Cria o item correspondente ao tipo de baú.
        type_index = 0 → item1 (restaura vida)
        type_index = 1 → item2
        type_index = 2 → item3
        type_index = 3 → item4
        """
        item_kind = f"item{self.type_index + 1}"
        image_path = f"{item_kind}.png"
        return Item(self.rect.centerx, self.rect.centery, radius=25, kind=item_kind, image_path=image_path)


class Item:
    def __init__(self, x, y, radius=25, kind='item1', image_path=None):
        self.x = x
        self.y = y
        self.radius = radius
        self.kind = kind
        self.collected = False
        self.index = 0  # posição na HUD

        if image_path:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (radius*2, radius*2))
        else:
            self.image = None

    def draw(self, screen):
        if self.collected:
            # HUD: desenha menor abaixo das vidas
            screen_x = 20 + 30 * self.index
            screen_y = 40
            if self.image:
                small_img = pygame.transform.scale(self.image, (self.radius, self.radius))
                screen.blit(small_img, (screen_x, screen_y))
        else:
            if self.image:
                screen.blit(self.image, (self.x - self.radius, self.y - self.radius))
