import pygame
import sys
import random
from settings import *
from jogador import Hero
from inimigo import Bot
from objetos import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hero vs Bots + Trunks/Items + Baús")
    clock = pygame.time.Clock()

    # Cenário
    background = pygame.image.load("fundo.png").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # Herói
    hero = Hero(100, 300)

    # Bots
    NUM_BOTS = 5
    bots = []
    for _ in range(NUM_BOTS):
        x = random.randint(WIDTH, WIDTH + 300)
        y = random.randint(0, HEIGHT - 50)
        bots.append(Bot(x, y))

    # Objetos
    trunks = []
    items = []
    collected_items = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- Atualizações ---
        hero.handle_keys()
        hero.update_projectile()

        # Atualiza bots
        for bot in bots:
            bot.update(WIDTH, HEIGHT)
            bot.shoot()
            bot.check_collision_with_hero(hero)

            # Colisão projétil herói → bot
            if hero.projectile and hero.projectile.colliderect(bot.rect):
                hero.projectile = None
                died = bot.hit()
                if died:
                    # cria Trunk/baú na posição do bot
                    type_index = random.randint(0, 3)
                    trunks.append(Trunk(bot.rect.centerx, bot.rect.centery, size=50, type_index=type_index))
                    # reposiciona bot
                    bot.rect.x = random.randint(WIDTH, WIDTH + 300)
                    bot.rect.y = random.randint(0, HEIGHT - bot.rect.height)
                    bot.lives = 3

        # Colisão projétil herói → trunks
        for trunk in trunks[:]:
            if hero.projectile and hero.projectile.colliderect(trunk.rect):
                hero.projectile = None
                if trunk.hit():
                    # cria item correspondente ao tipo do baú
                    item = trunk.spawn_item()
                    items.append(item)
                    trunks.remove(trunk)

        # Colisão herói → items
        for item in items[:]:
            item_rect = pygame.Rect(item.x - item.radius, item.y - item.radius, item.radius*2, item.radius*2)
            if hero.rect.colliderect(item_rect):
                item.collected = True
                item.index = len(collected_items)
                collected_items.append(item)
                items.remove(item)
                # Se for item1 (restaura vida)
                if item.kind == 'item1':
                    hero.lives += 1

        # Fim de jogo
        if hero.lives <= 0:
            print("Game Over!")
            running = False

        # --- Desenho ---
        screen.blit(background, (0, 0))
        hero.draw(screen)
        for bot in bots:
            bot.draw(screen)
        for trunk in trunks:
            trunk.draw(screen)
        for item in items:
            item.draw(screen)
        for item in collected_items:
            item.draw(screen)  # HUD

        # HUD: vidas do herói
        for i in range(hero.lives):
            pygame.draw.circle(screen, (0, 255, 0), (20 + i*25, 20), 12)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
