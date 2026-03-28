# src/npc.py
import pygame
import json, os

# Árvore de diálogo embutida (pode ser carregada de data/dialogues.json)
DIALOGUES = {
    "dog_1": {
        "text": "Au au! Cuidado com os carros na próxima rua!",
        "choices": [
            {"label": "Obrigada, Arya vai com cuidado!",  "next": "dog_1b"},
            {"label": "Não tenho medo de nada!",           "next": "dog_1c"},
        ]
    },
    "dog_1b": {"text": "Boa sorte! A vovó está te esperando! 🐾", "choices": []},
    "dog_1c": {"text": "Hm... coragem é bom, mas cuidado é melhor.", "choices": []},

    "person_1": {
        "text": "Que cachorra linda! Está perdida?",
        "choices": [
            {"label": "Não! Vou à casa da vovó.",  "next": "person_1b"},
            {"label": "Au! (Sem resposta)",          "next": "person_1c"},
        ]
    },
    "person_1b": {"text": "Que fofo! A casa fica ali na esquina. Bom caminho!", "choices": []},
    "person_1c": {"text": "Cachorros... nunca explicam nada.", "choices": []},
}

class NPC:
    def __init__(self, x, y, dialogue_id):
        self.rect = pygame.Rect(x, y, 28, 36)
        self.dialogue_id = dialogue_id
        self.color = (100, 180, 255)

    def start_dialogue(self, screen):
        node_id = self.dialogue_id
        font_big  = pygame.font.SysFont(None, 28)
        font_small = pygame.font.SysFont(None, 24)
        clock = pygame.time.Clock()

        running = True
        while running:
            node = DIALOGUES.get(node_id)
            if not node:
                break

            # Fundo do diálogo
            overlay = pygame.Surface((800, 180), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 420))

            # Texto principal
            text_surf = font_big.render(node["text"], True, (255, 255, 255))
            screen.blit(text_surf, (20, 435))

            choices = node.get("choices", [])
            if not choices:
                info = font_small.render("Pressione ENTER para fechar", True, (200, 200, 200))
                screen.blit(info, (20, 475))
                pygame.display.flip()
                waiting = True
                while waiting:
                    for ev in pygame.event.get():
                        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                            waiting = False
                        if ev.type == pygame.QUIT:
                            waiting = False
                            running = False
                break

            selected = 0
            choosing = True
            while choosing:
                # Redesenha painel de escolha
                overlay2 = pygame.Surface((800, 180), pygame.SRCALPHA)
                overlay2.fill((0, 0, 0, 180))
                screen.blit(overlay2, (0, 420))
                screen.blit(text_surf, (20, 435))

                for i, choice in enumerate(choices):
                    color = (255, 230, 0) if i == selected else (200, 200, 200)
                    prefix = "▶ " if i == selected else "  "
                    c_surf = font_small.render(f"{prefix}{choice['label']}", True, color)
                    screen.blit(c_surf, (30, 470 + i * 26))

                pygame.display.flip()
                clock.tick(30)

                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        choosing = False
                        running = False
                    if ev.type == pygame.KEYDOWN:
                        if ev.key == pygame.K_UP:
                            selected = (selected - 1) % len(choices)
                        if ev.key == pygame.K_DOWN:
                            selected = (selected + 1) % len(choices)
                        if ev.key == pygame.K_RETURN:
                            node_id = choices[selected]["next"]
                            choosing = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=6)
        # Cabeça
        head = pygame.Rect(self.rect.x + 6, self.rect.y - 14, 16, 16)
        pygame.draw.ellipse(screen, (255, 220, 180), head)
        # Label E para interagir
        font = pygame.font.SysFont(None, 18)
        screen.blit(font.render("[E]", True, (255, 255, 0)),
                    (self.rect.x, self.rect.y - 26))