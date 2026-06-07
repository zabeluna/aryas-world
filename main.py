# main.py — Arya's Adventure
import pygame
import sys
from src.player import Player
from src.monster import Car
from src.npc import NPC
from src.inventory import Inventory
from src.pathfinding import astar
from src.tsp import solve_tsp
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
    player = Player(x=48, y=140)
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

    sticks = [
        pygame.Rect(150, 150, 16, 16),
        pygame.Rect(350, 300, 16, 16),
        pygame.Rect(500, 200, 16, 16),
    ]

    target_pos = None
    path = []
    show_tsp_route = True

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = pygame.mouse.get_pos()
                target_pos = (mx, my)
                start = (int(player.rect.centerx // game_map.tile_size),
                         int(player.rect.centery // game_map.tile_size))
                goal  = (int(mx // game_map.tile_size),
                         int(my // game_map.tile_size))
                path = astar(game_map.grid, start, goal)

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_LSHIFT):
                    player.use_skill()

            # Interação com NPC
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                for npc in npcs:
                    if player.rect.colliderect(npc.rect.inflate(40, 40)):
                        npc.start_dialogue(screen)

            # Abrir/fechar inventário
            if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                hud.toggle_inventory()

            # Mostrar/ocultar rota TSP dos galhos restantes
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                show_tsp_route = not show_tsp_route

        keys = pygame.key.get_pressed()
        player.update(dt, keys, game_map, path)

        if path and player.reached_waypoint():
            path.pop(0)

        for car in cars:
            car.update(dt)

        for stick in sticks[:]:
            if player.rect.colliderect(stick):
                inventory.add_item("Galho")
                sticks.remove(stick)

        grandma_area = pygame.Rect(720, 520, 60, 60)
        if player.rect.colliderect(grandma_area):
            victory_screen(screen, inventory.count("Galho"))
            running = False

        game_map.draw(screen)

        for stick in sticks:
            draw_stick(screen, stick)

        grandma_house = pygame.Rect(720, 520, 60, 60)
        draw_grandma_house(screen, grandma_house)

        for car in cars:
            car.draw(screen)
        for npc in npcs:
            npc.draw(screen)

        if show_tsp_route:
            draw_tsp_route(screen, player, sticks)

        player.draw(screen)
        hud.draw(player, inventory, show_tsp_route)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def draw_tsp_route(screen, player, sticks):
    if not sticks:
        return

    points = [player.rect.center] + [stick.center for stick in sticks]
    route, distance = solve_tsp(points, return_to_start=False)
    route_points = [points[index] for index in route]

    if len(route_points) >= 2:
        pygame.draw.lines(screen, (255, 245, 120), False, route_points, 3)

    font = pygame.font.SysFont(None, 20)
    for order, point in enumerate(route_points[1:], start=1):
        pygame.draw.circle(screen, (255, 245, 120), point, 11, 2)
        label = font.render(str(order), True, (30, 30, 30))
        screen.blit(label, (point[0] - 5, point[1] - 7))

    distance_label = font.render(f"TSP rota: {distance:.0f}px", True, (255, 245, 120))
    screen.blit(distance_label, (10, 104))


def draw_stick(screen, rect):
    start = (rect.left + 2, rect.centery + 4)
    end = (rect.right - 2, rect.centery - 4)
    pygame.draw.line(screen, (92, 54, 28), start, end, 5)
    pygame.draw.line(screen, (145, 91, 48), start, end, 2)
    pygame.draw.line(screen, (92, 54, 28), rect.center, (rect.right, rect.top + 2), 3)
    pygame.draw.circle(screen, (255, 234, 132), rect.center, 10, 1)


def draw_grandma_house(screen, rect):
    shadow = pygame.Rect(rect.x + 4, rect.y + 6, rect.width, rect.height)
    pygame.draw.rect(screen, (70, 72, 70), shadow, border_radius=4)

    roof_points = [
        (rect.left - 6, rect.top + 20),
        (rect.centerx, rect.top - 8),
        (rect.right + 6, rect.top + 20),
    ]
    pygame.draw.polygon(screen, (168, 72, 58), roof_points)
    pygame.draw.polygon(screen, (109, 48, 45), roof_points, 2)

    body = pygame.Rect(rect.x, rect.y + 18, rect.width, rect.height - 12)
    pygame.draw.rect(screen, (252, 214, 144), body, border_radius=5)
    pygame.draw.rect(screen, (140, 98, 66), body, 2, border_radius=5)

    door = pygame.Rect(rect.centerx - 8, rect.bottom - 24, 16, 24)
    pygame.draw.rect(screen, (112, 77, 48), door, border_radius=3)
    pygame.draw.circle(screen, (245, 220, 115), (door.right - 4, door.centery), 2)

    for wx in (rect.x + 8, rect.right - 20):
        window = pygame.Rect(wx, rect.y + 30, 14, 12)
        pygame.draw.rect(screen, (155, 213, 235), window, border_radius=2)
        pygame.draw.rect(screen, (88, 126, 150), window, 1, border_radius=2)

    font = pygame.font.SysFont(None, 17)
    label = font.render("Vovo", True, (76, 48, 32))
    screen.blit(label, (rect.x + 15, rect.y + 21))


def victory_screen(screen, sticks_count):
    screen.fill((255, 230, 100))
    font = pygame.font.SysFont(None, 64)
    small = pygame.font.SysFont(None, 36)
    screen.blit(font.render("Arya chegou!", True, (80, 40, 0)), (160, 200))
    screen.blit(small.render(f"Galhos coletados: {sticks_count}", True, (80, 40, 0)), (270, 290))
    pygame.display.flip()
    pygame.time.wait(3000)


if __name__ == "__main__":
    main()
