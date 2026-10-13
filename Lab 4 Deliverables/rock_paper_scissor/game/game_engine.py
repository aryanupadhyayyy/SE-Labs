import math
import random
from collections import Counter, deque

import pygame
from game.button import ChoiceButton
from game.icons import draw_gesture

# Which move beats which: key beats value
BEATS = {"ROCK": "SCISSORS", "SCISSORS": "PAPER", "PAPER": "ROCK"}
# The move that beats the key
COUNTER = {loser: winner for winner, loser in BEATS.items()}

STATE_IDLE = "IDLE"
STATE_COUNTDOWN = "COUNTDOWN"
STATE_RESULT = "RESULT"
STATE_MATCH_OVER = "MATCH_OVER"


class GameEngine:
    def __init__(self, width, height, target_wins=3):
        self.width = width
        self.height = height

        self.choices = ["ROCK", "PAPER", "SCISSORS"]
        btn_w, btn_h = 160, 50
        gap = 20
        total_w = 3 * btn_w + 2 * gap
        start_x = (width - total_w) // 2
        btn_y = height - 70

        self.buttons = [
            ChoiceButton("ROCK", pygame.Rect(start_x, btn_y, btn_w, btn_h), (160, 50, 50), (200, 70, 70)),
            ChoiceButton("PAPER", pygame.Rect(start_x + btn_w + gap, btn_y, btn_w, btn_h), (40, 100, 170), (60, 130, 210)),
            ChoiceButton("SCISSORS", pygame.Rect(start_x + 2 * (btn_w + gap), btn_y, btn_w, btn_h), (180, 140, 30), (220, 180, 50)),
        ]

        # Match settings
        self.target_wins = target_wins

        # Adaptive AI settings: look at the player's last N throws
        self.history_size = 6
        self.bias_strength = 1.5

        self.display_duration = 1800
        self.countdown_beat = 350
        self.countdown_words = ["ROCK...", "PAPER...", "SCISSORS..."]
        self.countdown_duration = self.countdown_beat * len(self.countdown_words)
        self.reveal_pop = 220

        self.font_title = pygame.font.SysFont(None, 36)
        self.font_hud = pygame.font.SysFont(None, 26)
        self.font_arena = pygame.font.SysFont(None, 32)
        self.font_small = pygame.font.SysFont(None, 22)
        self.font_banner = pygame.font.SysFont(None, 54)

        self.reset_match()

    def reset_match(self):
        self.player_choice = None
        self.cpu_choice = None
        self.result_text = "Make your move!"
        self.result_color = (220, 225, 235)

        self.player_score = 0
        self.cpu_score = 0
        self.match_winner = None

        self.player_history = deque(maxlen=self.history_size)
        self.ai_note = ""

        self.state = STATE_IDLE
        self.state_started = pygame.time.get_ticks()

    def determine_winner(self, player, cpu):
        if player == cpu:
            return "TIE"
        return "PLAYER" if BEATS[player] == cpu else "CPU"

    def cpu_pick(self):
        """Pick a CPU move, biased toward countering the player's recent favourites."""
        weights = {choice: 1.0 for choice in self.choices}
        counts = Counter(self.player_history)
        for move, count in counts.items():
            weights[COUNTER[move]] += count * self.bias_strength

        if counts:
            favourite, fav_count = counts.most_common(1)[0]
            if fav_count >= 3:
                self.ai_note = f"CPU has noticed you favour {favourite}..."
            else:
                self.ai_note = ""

        return random.choices(self.choices, weights=[weights[c] for c in self.choices])[0]

    def play_round(self, choice):
        self.player_choice = choice
        # The CPU decides from history *before* this throw so it can't peek
        self.cpu_choice = self.cpu_pick()
        self.player_history.append(choice)

        self.state = STATE_COUNTDOWN
        self.state_started = pygame.time.get_ticks()

    def resolve_round(self):
        outcome = self.determine_winner(self.player_choice, self.cpu_choice)
        if outcome == "PLAYER":
            self.player_score += 1
            self.result_text = f"You Win! {self.player_choice} beats {self.cpu_choice}."
            self.result_color = (80, 230, 120)
        elif outcome == "CPU":
            self.cpu_score += 1
            self.result_text = f"You Lose! {self.cpu_choice} beats {self.player_choice}."
            self.result_color = (240, 80, 80)
        else:
            self.result_text = f"It's a Draw! Both picked {self.player_choice}."
            self.result_color = (240, 210, 80)

        if self.player_score >= self.target_wins:
            self.match_winner = "PLAYER"
        elif self.cpu_score >= self.target_wins:
            self.match_winner = "CPU"

        self.state = STATE_RESULT
        self.state_started = pygame.time.get_ticks()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            if self.state == STATE_MATCH_OVER:
                self.reset_match()
            return

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.state not in (STATE_IDLE, STATE_RESULT):
                return
            for btn in self.buttons:
                if btn.contains(event.pos):
                    self.play_round(btn.choice_name)
                    break

    def update(self):
        elapsed = pygame.time.get_ticks() - self.state_started

        if self.state == STATE_COUNTDOWN and elapsed >= self.countdown_duration:
            self.resolve_round()
        elif self.state == STATE_RESULT and self.match_winner and elapsed >= self.display_duration:
            self.state = STATE_MATCH_OVER
            self.state_started = pygame.time.get_ticks()
        elif self.state == STATE_RESULT and elapsed >= self.display_duration:
            self.player_choice = None
            self.cpu_choice = None
            self.result_text = "Make your move!"
            self.result_color = (190, 195, 205)
            self.state = STATE_IDLE
            self.state_started = pygame.time.get_ticks()

    def render_arena(self, screen):
        elapsed = pygame.time.get_ticks() - self.state_started
        left_x, right_x, icon_y = self.width // 4, 3 * self.width // 4, 185
        base_size = 100

        you = self.font_hud.render("YOU", True, (100, 180, 255))
        cpu = self.font_hud.render("CPU", True, (255, 120, 120))
        screen.blit(you, (left_x - you.get_width() // 2, 100))
        screen.blit(cpu, (right_x - cpu.get_width() // 2, 100))

        vs = self.font_arena.render("VS", True, (120, 128, 145))
        screen.blit(vs, (self.width // 2 - vs.get_width() // 2, icon_y - vs.get_height() // 2))

        if self.state == STATE_COUNTDOWN:
            # Both fists bob in sync once per beat before the reveal
            beat_phase = (elapsed % self.countdown_beat) / self.countdown_beat
            offset = int(-abs(math.sin(beat_phase * math.pi)) * 22)
            draw_gesture(screen, "ROCK", (left_x, icon_y + offset), base_size)
            draw_gesture(screen, "ROCK", (right_x, icon_y + offset), base_size)
        elif self.player_choice and self.cpu_choice:
            # Pop the revealed gestures in with a short scale-up
            pop = min(1.0, elapsed / self.reveal_pop) if self.state == STATE_RESULT else 1.0
            size = int(base_size * (0.6 + 0.4 * pop))
            draw_gesture(screen, self.player_choice, (left_x, icon_y), size)
            draw_gesture(screen, self.cpu_choice, (right_x, icon_y), size)
        else:
            for x in (left_x, right_x):
                pygame.draw.circle(screen, (45, 52, 66), (x, icon_y), base_size // 2, width=3)
                q = self.font_arena.render("?", True, (90, 98, 115))
                screen.blit(q, (x - q.get_width() // 2, icon_y - q.get_height() // 2))

    def render_match_over(self, screen):
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((10, 12, 18, 215))
        screen.blit(overlay, (0, 0))

        won = self.match_winner == "PLAYER"
        title = "YOU WIN THE MATCH!" if won else "CPU WINS THE MATCH!"
        color = (80, 230, 120) if won else (240, 80, 80)

        banner = pygame.Rect(40, self.height // 2 - 90, self.width - 80, 180)
        pygame.draw.rect(screen, (30, 35, 46), banner, border_radius=14)
        pygame.draw.rect(screen, color, banner, width=3, border_radius=14)

        lines = [
            (self.font_banner.render(title, True, color), banner.top + 28),
            (self.font_arena.render(f"Final Score  {self.player_score} - {self.cpu_score}", True, (230, 232, 238)), banner.top + 88),
            (self.font_hud.render("Press R to play again", True, (190, 195, 205)), banner.top + 132),
        ]
        for surf, y in lines:
            screen.blit(surf, (self.width // 2 - surf.get_width() // 2, y))

    def render(self, screen):
        screen.fill((24, 28, 36))

        title_surf = self.font_title.render("Rock Paper Scissors", True, (245, 245, 245))
        screen.blit(title_surf, (self.width // 2 - title_surf.get_width() // 2, 14))

        p_surf = self.font_hud.render(f"Player Score: {self.player_score}", True, (100, 180, 255))
        c_surf = self.font_hud.render(f"CPU Score: {self.cpu_score}", True, (255, 120, 120))
        t_surf = self.font_small.render(f"First to {self.target_wins} wins", True, (160, 166, 180))
        screen.blit(p_surf, (35, 52))
        screen.blit(c_surf, (self.width - c_surf.get_width() - 35, 52))
        screen.blit(t_surf, (self.width // 2 - t_surf.get_width() // 2, 55))

        pygame.draw.line(screen, (45, 52, 66), (25, 82), (self.width - 25, 82), 2)

        self.render_arena(screen)

        if self.state == STATE_COUNTDOWN:
            beat = min(len(self.countdown_words) - 1, (pygame.time.get_ticks() - self.state_started) // self.countdown_beat)
            res_surf = self.font_arena.render(self.countdown_words[beat], True, (230, 232, 238))
        else:
            res_surf = self.font_arena.render(self.result_text, True, self.result_color)
        screen.blit(res_surf, (self.width // 2 - res_surf.get_width() // 2, 262))

        if self.ai_note:
            note = self.font_small.render(self.ai_note, True, (200, 150, 255))
            screen.blit(note, (self.width // 2 - note.get_width() // 2, 296))

        enabled = self.state in (STATE_IDLE, STATE_RESULT)
        for btn in self.buttons:
            btn.render(screen, enabled)

        if self.state == STATE_MATCH_OVER:
            self.render_match_over(screen)
