import math
import pygame


def draw_rock(surface, center, size):
    cx, cy = center
    r = size // 2
    # Lumpy boulder outline built from a perturbed circle
    points = []
    bumps = [1.0, 0.92, 1.04, 0.95, 1.02, 0.9, 1.05, 0.94, 1.0, 0.93, 1.03, 0.96]
    for i, k in enumerate(bumps):
        angle = 2 * math.pi * i / len(bumps)
        points.append((cx + math.cos(angle) * r * k, cy + math.sin(angle) * r * k * 0.85))
    pygame.draw.polygon(surface, (128, 128, 140), points)
    pygame.draw.polygon(surface, (70, 70, 82), points, width=max(2, size // 30))

    # Knuckle creases and a highlight to read as a clenched fist / stone
    crease = (90, 90, 102)
    for i in range(3):
        x = cx - r * 0.45 + i * r * 0.45
        pygame.draw.arc(surface, crease, pygame.Rect(x - r * 0.2, cy - r * 0.55, r * 0.4, r * 0.4), math.pi, 2 * math.pi, max(2, size // 40))
    pygame.draw.circle(surface, (170, 170, 182), (int(cx - r * 0.35), int(cy + r * 0.15)), max(2, size // 12))


def draw_paper(surface, center, size):
    cx, cy = center
    w, h = int(size * 0.72), int(size * 0.92)
    rect = pygame.Rect(cx - w // 2, cy - h // 2, w, h)
    fold = size // 5

    sheet = [
        rect.topleft,
        (rect.right - fold, rect.top),
        (rect.right, rect.top + fold),
        rect.bottomright,
        rect.bottomleft,
    ]
    pygame.draw.polygon(surface, (240, 242, 248), sheet)
    pygame.draw.polygon(surface, (120, 130, 150), sheet, width=max(2, size // 30))

    # Dog-eared corner
    corner = [(rect.right - fold, rect.top), (rect.right - fold, rect.top + fold), (rect.right, rect.top + fold)]
    pygame.draw.polygon(surface, (200, 205, 218), corner)
    pygame.draw.polygon(surface, (120, 130, 150), corner, width=max(1, size // 40))

    # Ruled lines
    line_gap = h // 7
    for i in range(2, 7):
        y = rect.top + i * line_gap
        pygame.draw.line(surface, (150, 175, 215), (rect.left + w // 8, y), (rect.right - w // 8, y), max(1, size // 45))


def draw_scissors(surface, center, size):
    cx, cy = center
    r = size // 2
    pivot = (cx, cy + r * 0.05)
    blade = (205, 210, 220)
    edge = (90, 95, 110)

    # Two blades crossing in an X above the pivot
    for side in (-1, 1):
        tip = (cx + side * r * 0.55, cy - r * 0.95)
        base_l = (pivot[0] - side * r * 0.22, pivot[1] + r * 0.08)
        base_r = (pivot[0] + side * r * 0.08, pivot[1] - r * 0.2)
        poly = [base_l, tip, base_r]
        pygame.draw.polygon(surface, blade, poly)
        pygame.draw.polygon(surface, edge, poly, width=max(1, size // 40))

    # Finger rings below the pivot
    ring_r = int(r * 0.3)
    for side in (-1, 1):
        ring_c = (int(cx + side * r * 0.4), int(cy + r * 0.6))
        pygame.draw.line(surface, (200, 60, 60), pivot, ring_c, max(3, size // 14))
        pygame.draw.circle(surface, (200, 60, 60), ring_c, ring_r, width=max(3, size // 14))

    pygame.draw.circle(surface, (60, 60, 70), (int(pivot[0]), int(pivot[1])), max(3, size // 16))


_DRAWERS = {"ROCK": draw_rock, "PAPER": draw_paper, "SCISSORS": draw_scissors}


def draw_gesture(surface, choice, center, size):
    drawer = _DRAWERS.get(choice)
    if drawer:
        drawer(surface, center, size)
