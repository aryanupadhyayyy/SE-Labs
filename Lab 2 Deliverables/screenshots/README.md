# Lab 2 – Jira steps and screenshots

Jira project **Podcast-Guest-Scheduler** (key **PGS**), Scrum, company-managed.

## 1. Create the project
Jira → **+** next to Projects → Software development → **Scrum** → **Company-managed** → name `Podcast-Guest-Scheduler`, key `PGS`.

## 2. Load the backlog
**Option A – CSV import:** ⚙️ Settings → System → External system import → **CSV** → upload `../jira_import.csv`.
Map: *Work type* → Issue Type, *Summary* → Summary, *Description* → Description, *Priority* → Priority,
*Story Points* → Story Points, *Issue ID* → Issue ID, *Parent* → Parent. Skip *Sprint* (sprints are created in step 4).

**Option B – by hand:** create the 4 epics, then each story with **Create work item** under its epic, using
`../Lab2_EPICs_and_User_Stories.pdf`. Set Priority and Story Points (More fields → Story Points) on each story.

## 3. Screenshots of the backlog
| File name | What to capture |
|-----------|-----------------|
| `01_backlog_epics_stories.png` | **Backlog** with the Epic panel open (press **E**), showing all 4 epics and the 12 stories |
| `02_story_points.png` | Backlog with the story-point badges visible, and one epic expanded showing its point total |

## 4. Sprint 1
Create sprint **PGS Sprint 1**, drag in stories 1.1, 1.2, 2.1, 2.2, 3.1 (18 pts), **Start sprint** with duration **1 week**.

| File name | What to capture |
|-----------|-----------------|
| `03_active_sprint_board.png` | **Active sprints** board with some stories in To Do, In Progress and Done |

Move everything to **Done** → **Complete sprint**.

## 5. Sprint 2
Create **PGS Sprint 2** with stories 2.4, 3.2, 3.3, 4.1, 4.2 (17 pts), start (1 week), move to Done, complete.

## 6. Burndown charts
| File name | What to capture |
|-----------|-----------------|
| `04_burndown_sprint1.png` | **Reports → Burndown Chart**, sprint = PGS Sprint 1, Story Points |
| `05_burndown_sprint2.png` | Same for PGS Sprint 2 |

Put the 5 images in this folder. They are then combined into `Lab2_Jira_Screenshots.pdf` (backlog, story points,
sprint board, burndown chart).
