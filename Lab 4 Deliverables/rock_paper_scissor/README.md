# Rock Paper Scissor Lab

This project is an interactive hand-game duel using **Pygame**. It introduces students to dictionary-based rule lookups, automated CPU decision-making, temporary result display timers, and modular UI button interaction within an object-oriented codebase.
---

## What's Provided

A working Rock Paper Scissors game with:

- Three interactive choice buttons (`ROCK`, `PAPER`, `SCISSORS`) with mouse hover and click response states
- An automated computer opponent selecting moves at random
- Live scoreboard tracking player score and CPU score independently
- Timed result display that shows the outcome for 1.8 seconds before clearing picks for the next round

It has **one deliberate bug** and **three optional features** left as tasks to implement. You are expected to **analyze**, **interact with an AI assistant**, and **complete/fix** the game to make it fully functional and more interesting.

### **Use an LLM (e.g. ChatGPT or Claude) as your debugging and pair-programming partner for this lab.**
---

## Getting Started

### Setup

1. Make sure you have Python 3.10+ installed.
2. Install dependencies:

```bash
pip install pygame
```

3. Run the game:

```bash
python main.py
```

**Controls:** Left-click ROCK, PAPER or SCISSORS to throw. The match is first to 3 wins; press R to play again after the match ends.


## Tasks to Complete

Each task must be completed using an iterative process involving LLM suggestions and your critical code review.

### Task 1: Fix the inverted outcome evaluation bug

Whenever the player throws a winning hand against the computer, the game awards the point to the CPU instead of the player. Correct the outcome evaluation logic so standard rules apply (Rock beats Scissors, Scissors beats Paper, and Paper beats Rock).

### Task 2: Implement "First to X Wins" match victory state

The game currently loops endlessly with no decisive match conclusion. Introduce a target win ceiling that halts play when reached, presents an end-of-match victory banner declaring the ultimate winner, and prompts the player to restart.

### Task 3: Implement adaptive AI pattern tracking

The computer currently picks its moves entirely at random. Introduce adaptive intelligence that records the player's recent throw tendencies and dynamically biases CPU selections toward the counter-move when a player repeatedly favors a specific option.

### Task 4: Implement Procedural Gesture Icons & Reveal Animations

Selections are currently rendered as plain text labels. Create distinct visual graphic icons for Rock, Paper, and Scissors, adding a synchronized countdown or shaking reveal animation before displaying both choices each turn.

---

## Expected Behavior

- Clicking any choice button selects that move, rolls a CPU choice, and evaluates the winner correctly.
- Rock beats Scissors, Scissors beats Paper, Paper beats Rock, and identical choices result in a Draw.
- Scores increment accurately and the round outcome stays visible for 1.8 seconds before clearing picks back to
---

## Folder Structure

```
rock_paper_scissors/
├── game/
│   ├── button.py
│   ├── game_engine.py
│   └── icons.py
├── main.py
└── README.md
```

## Submission Checklist

Submission is only the following three things:

- [x] A 10-second video of gameplay **before** your changes, showing the bug/broken behavior
- [x] A 10-second video of gameplay **after** your changes, showing the bug fixed and the new features working
- [x] The Chat/LLM used page link, with the complete chat history


---

## Changes Made (Lab 4 submission - PES1UG25CS806)

| Task | What changed | Where |
|------|--------------|-------|
| 1. Inverted outcome bug | The rule table awarded every winning hand to the CPU. Replaced it with a single `BEATS` map (Rock>Scissors, Scissors>Paper, Paper>Rock) so the winner is derived from one source of truth. All 9 combinations verified. | `game/game_engine.py` `determine_winner` |
| 2. First to X wins | Added `target_wins` (default 3), a `MATCH_OVER` state, a victory banner with the final score, input lock while the match is over, and **R** to restart. | `game/game_engine.py` `resolve_round`, `render_match_over`, `reset_match` |
| 3. Adaptive AI | The CPU keeps the player's last 6 throws and weights its pick toward the counter of each recent move (`1 + 1.5 * count`). It decides *before* seeing the current throw. When one move appears 3+ times a hint shows: "CPU has noticed you favour ROCK...". With 6 ROCKs in history the CPU picks PAPER ~83% of the time; with no history it is uniform. | `game/game_engine.py` `cpu_pick` |
| 4. Gesture icons + reveal | New `game/icons.py` draws Rock (lumpy fist/stone), Paper (ruled sheet with folded corner) and Scissors (blades + rings) with pygame primitives. Each round plays a synced "ROCK... PAPER... SCISSORS..." countdown where both fists bob, then the real gestures pop in with a scale-up. Buttons show small icons too. | `game/icons.py`, `game/button.py`, `game/game_engine.py` `render_arena` |

The window was enlarged to 640x400 (`main.py`) to fit the icon arena.
