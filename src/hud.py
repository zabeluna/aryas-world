# src/hud.py
import pygame

DASH_COOLDOWN = 1.5

class HUD:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 26)

    def draw(self, player, inventory):
        # ── Barra de HP ──────────────────────────────────────────
        bar_w = 160
        bar_h = 18
        hp_ratio = player.hp / player.max_hp
        pygame.draw.rect(self.screen, (80, 0, 0),   (10, 10, bar_w, bar_h))
        pygame.draw.rect(self.screen, (220, 50, 50), (10, 10, int(bar_w * hp_ratio), bar_h))
        pygame.draw.rect(self.screen, (255,255,255), (10, 10, bar_w, bar_h), 1)
        hp_text = self.font.render(f"HP: {player.hp}", True, (255, 255, 255))
        self.screen.blit(hp_text, (14, 11))

        # ── Galhos coletados ─────────────────────────────────────
        sticks = inventory.count("Galho")
        stick_text = self.font.render(f"🌿 Galhos: {sticks}", True, (255, 230, 100))
        self.screen.blit(stick_text, (10, 36))

        # ── Cooldown da Skill ─────────────────────────────────────
        cd = player.dash_cooldown_timer
        cd_ratio = 1.0 - (cd / DASH_COOLDOWN) if cd > 0 else 1.0
        cd_w = 100
        cd_h = 12
        pygame.draw.rect(self.screen, (30, 30, 80),   (10, 60, cd_w, cd_h))
        pygame.draw.rect(self.screen, (80, 80, 255),  (10, 60, int(cd_w * cd_ratio), cd_h))
        pygame.draw.rect(self.screen, (200,200,255),  (10, 60, cd_w, cd_h), 1)
        cd_label = self.font.render("DASH [SPC]", True,
                                    (255, 255, 255) if cd == 0 else (150, 150, 255))
        self.screen.blit(cd_label, (116, 58))