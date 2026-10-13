# Lab 4 Deliverables – VibeCoding (Rock Paper Scissors)

**Aryan Upadhyay · PES1UG25CS806 · Section C**
Assigned repo (#59): https://github.com/SETAPESU26/59_rock_paper_scissor — cloned at commit `72e89d3`; no PR raised to SETAPESU26.

| # | Deliverable | Files |
|---|-------------|-------|
| a | **Videos** (≈10 s each) – before: winning throws are scored as losses; after: correct scoring, countdown + gesture icons, adaptive-AI hint, first-to-3 victory banner, R to restart | `videos/before_changes.mp4`, `videos/after_changes.mp4` |
| b | **Updated code** – bug fixed and all 3 README features added (see the game README, "Changes Made") | `rock_paper_scissor/` |
| c | **Chat history** – full exported transcript of the AI session (prompts, replies, every command and code edit), plus a task-by-task summary with the code diff | `Lab4_Chat_History_Full_Transcript.pdf`, `Lab4_Chat_History.pdf` / `.docx` |

| README task | Done |
|-------------|------|
| 1. Fix inverted outcome bug | ✅ all 9 combinations verified |
| 2. "First to X wins" match victory | ✅ first to 3, banner, R to restart |
| 3. Adaptive AI pattern tracking | ✅ after 6× ROCK the CPU picks PAPER ~83% |
| 4. Procedural gesture icons + reveal animation | ✅ drawn icons, "ROCK… PAPER… SCISSORS…" countdown, pop-in reveal |

Run it:

```bash
pip install pygame
cd rock_paper_scissor
python main.py
```
