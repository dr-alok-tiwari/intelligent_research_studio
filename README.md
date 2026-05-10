# Intelligent Research: AI Applications & Techniques
## Complete Classroom Teaching System — For Researchers

### Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Structure

```
app.py                      ← Main entry point
requirements.txt
utils.py                    ← Shared helpers (quiz engine, cards, activities)
pages/
  home.py                   ← Home dashboard
  course_overview.py        ← Course overview and CLOs
  quiz_bank.py              ← 100+ quiz questions with filters
data/
  quiz_bank_data.py         ← All 100 quiz questions with full explanations
sessions/
  s01.py  →  s16.py         ← 16 complete teaching sessions
  session_content.py        ← Full content for sessions 03–16
```

### Features

- **16 Sessions** — each with Theoretical Concepts, Research Story, Visual Diagram,
  Instructor Demonstration, Classroom Activity, Mini Case, Quiz, and Reflection
- **100 Quiz Questions** — filterable by session, difficulty, CLO
- **No preselected answers** — uses `index=None` in all radio widgets
- **Reveal-based interaction** — all answers, cases, and activities use reveal buttons
- **Projector Mode** — large font, high contrast for classroom screens
- **No API key required** — no paid external service needed
- **No placeholder content** — every section is complete and classroom-ready

### Teaching Notes

- Enable Projector Mode from the sidebar before class
- Use the "Tell Me the Research Story" button for classroom storytelling
- Quiz questions use separate Streamlit keys to avoid state conflicts
- Activity solutions are hidden behind "Show Suggested Solution" buttons
- All PRISMA and visual diagrams are interactive (Plotly)
