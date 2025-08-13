import pygame
import sys
import random
from settings import *
from jogador import Hero
from inimigo import Bot
from objetos import *


def tela_inicio(screen):
    # Carrega imagem de fundo
    background = pygame.image.load("imagens/tela/start.jpg").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    
    font = pygame.font.Font(None, 50)
    esperando = True

    while esperando:
        screen.blit(background, (0, 0))

        fonte = pygame.font.Font("fonte/texas_tango/texas_tango.otf", 30)

        mensagem = "Pressione ENTER para começar"

        # Posições
        x = WIDTH // 2
        y = HEIGHT - 100

# Desenha sombra
        screen.blit(fonte.render(mensagem, True, (0, 0, 0)), (x - fonte.size(mensagem)[0]//2 + 3, y + 3))
# Desenha texto principal
        screen.blit(fonte.render(mensagem, True, (255, 215, 0)), (x - fonte.size(mensagem)[0]//2, y))
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    esperando = False


def tela_game_over(screen):
    # Carrega imagem de fundo
    background = pygame.image.load("imagens/tela/game_over.jpg").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    font = pygame.font.Font(None, 60)
    small_font = pygame.font.Font(None, 36)
    esperando = True

    while esperando:
        screen.blit(background, (0, 0))

        # Fonte principal e pequena
        fonte = pygame.font.Font("fonte/texas_tango/texas_tango.otf", 60)       # FIM DE JOGO
        small_font = pygame.font.Font("fonte/texas_tango/texas_tango.otf", 22)  # instruções

# Mensagens
        mensagem_principal = "FIM DE JOGO"
        mensagem_instrucao = "Pressione R para reiniciar ou ESC para sair"

# Posições
        x_principal = WIDTH // 2
        y_principal = HEIGHT // 3
        x_instrucao = WIDTH // 2
        y_instrucao = HEIGHT // 2

# Desenha sombra e texto principal
        screen.blit(fonte.render(mensagem_principal, True, (0, 0, 0)), 
            (x_principal - fonte.size(mensagem_principal)[0]//2 + 3, y_principal + 3))
        screen.blit(fonte.render(mensagem_principal, True, (255, 215, 0)), 
            (x_principal - fonte.size(mensagem_principal)[0]//2, y_principal))

# Desenha sombra e texto da instrução
        screen.blit(small_font.render(mensagem_instrucao, True, (0, 0, 0)), 
            (x_instrucao - small_font.size(mensagem_instrucao)[0]//2 + 2, y_instrucao + 2))
        screen.blit(small_font.render(mensagem_instrucao, True, (255, 255, 255)), 
            (x_instrucao - small_font.size(mensagem_instrucao)[0]//2, y_instrucao))

        
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    esperando = False
                    main()
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Seis Tiros no Oeste")
    clock = pygame.time.Clock()
    tela_inicio(screen)

    # Cenário
    background = pygame.image.load("imagens/tela/fundo_jogo.png").convert()
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
            tela_game_over(screen)
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
            img_vida = pygame.image.load('imagens/objetos/coracao.png')
            img_vida = pygame.transform.scale(img_vida, (25, 25))
            screen.blit(img_vida, (20 + i * 25, 20))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
