# main.py — Arya's Adventure
import pygame
import sys
from src.player import Player
from src.monster import Car
from src.npc import NPC
from src.inventory import Inventory
from src.pathfinding import astar
from src.map import GameMap
from src.hud import HUD

WIDTH, HEIGHT = 800, 600
FPS = 60
TITLE = "Arya's Adventure 🐶"

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    game_map = GameMap("data/map.json")
    player = Player(x=100, y=100)
    inventory = Inventory()
    hud = HUD(screen)

    cars = [
        Car(x=400, y=200, route=[(400,200),(600,200),(600,200),(400,200)]),
        Car(x=300, y=400, route=[(300,400),(500,400),(500,400),(300,400)]),
    ]

    npcs = [
        NPC(x=200, y=300, dialogue_id="dog_1"),
        NPC(x=600, y=450, dialogue_id="person_1"),
    ]

    sticks = [  # Galhos coletáveis
        pygame.Rect(150, 150, 16, 16),
        pygame.Rect(350, 300, 16, 16),
        pygame.Rect(500, 200, 16, 16),
    ]

    target_pos = None  # Destino do clique do mouse
    path = []          # Caminho calculado pelo A*

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0

        # ── Eventos ──────────────────────────────────────────────
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = pygame.mouse.get_pos()
                target_pos = (mx, my)
                # Calcula rota com A*
                start = (int(player.rect.centerx // game_map.tile_size),
                         int(player.rect.centery // game_map.tile_size))
                goal  = (int(mx // game_map.tile_size),
                         int(my // game_map.tile_size))
                path = astar(game_map.grid, start, goal)

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_LSHIFT):
                    player.use_skill()  # Skill de desvio

            # Interação com NPC
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                for npc in npcs:
                    if player.rect.colliderect(npc.rect.inflate(40, 40)):
                        npc.start_dialogue(screen)

        # ── Update ───────────────────────────────────────────────
        keys = pygame.key.get_pressed()
        player.update(dt, keys, game_map, path)

        # Limpa path se player chegou ao destino
        if path and player.reached_waypoint():
            path.pop(0)

        for car in cars:
            car.update(dt)
            if car.rect.colliderect(player.rect) and not player.is_dashing:
                player.take_damage(10)

        # Coleta de galhos
        for stick in sticks[:]:
            if player.rect.colliderect(stick):
                inventory.add_item("Galho")
                sticks.remove(stick)

        # Condição de vitória (área da casa da vovó)
        grandma_area = pygame.Rect(720, 520, 60, 60)
        if player.rect.colliderect(grandma_area):
            victory_screen(screen, inventory.count("Galho"))
            running = False

        # Morte
        if player.hp <= 0:
            death_screen(screen)
            running = False

        # ── Draw ─────────────────────────────────────────────────
        screen.fill((80, 140, 80))  # Fundo verde (grama)
        game_map.draw(screen)

        for stick in sticks:
            pygame.draw.rect(screen, (139, 90, 43), stick)  # Galho marrom

        grandma_house = pygame.Rect(720, 520, 60, 60)
        pygame.draw.rect(screen, (255, 200, 100), grandma_house)
        font = pygame.font.SysFont(None, 18)
        screen.blit(font.render("Vovó", True, (0,0,0)), (728, 545))

        for car in cars:
            car.draw(screen)
        for npc in npcs:
            npc.draw(screen)

        player.draw(screen)
        hud.draw(player, inventory)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def victory_screen(screen, sticks_count):
    screen.fill((255, 230, 100))
    font = pygame.font.SysFont(None, 64)
    small = pygame.font.SysFont(None, 36)
    screen.blit(font.render("🐶 Arya chegou!", True, (80, 40, 0)), (160, 200))
    screen.blit(small.render(f"Galhos coletados: {sticks_count}", True, (80, 40, 0)), (270, 290))
    pygame.display.flip()
    pygame.time.wait(3000)


def death_screen(screen):
    screen.fill((40, 0, 0))
    font = pygame.font.SysFont(None, 64)
    screen.blit(font.render("Arya foi atropelada...", True, (255, 80, 80)), (80, 260))
    pygame.display.flip()
    pygame.time.wait(2500)


if __name__ == "__main__":
    main()