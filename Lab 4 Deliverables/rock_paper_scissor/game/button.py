import pygame
from game.icons import draw_gesture


class ChoiceButton:
    def __init__(self, choice_name, rect, color, hover_color):
        self.choice_name = choice_name
        self.rect = rect
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.SysFont(None, 26)

    def contains(self, pos):
        return self.rect.collidepoint(pos)

    def render(self, surface, enabled=True):
        mouse_pos = pygame.mouse.get_pos()
        hovered = enabled and self.rect.collidepoint(mouse_pos)
        bg_color = self.hover_color if hovered else self.color
        if not enabled:
            bg_color = tuple(c // 2 for c in self.color)

        pygame.draw.rect(surface, bg_color, self.rect, border_radius=8)
        pygame.draw.rect(surface, (230, 230, 235), self.rect, width=2, border_radius=8)

        # Small gesture icon on the left, label on the right
        icon_size = self.rect.height - 16
        icon_center = (self.rect.left + 12 + icon_size // 2, self.rect.centery)
        draw_gesture(surface, self.choice_name, icon_center, icon_size)

        text_surf = self.font.render(self.choice_name, True, (255, 255, 255))
        text_left = self.rect.left + 20 + icon_size
        text_area = self.rect.right - text_left
        surface.blit(
            text_surf,
            (
                text_left + (text_area - text_surf.get_width()) // 2,
                self.rect.centery - text_surf.get_height() // 2,
            ),
        )
