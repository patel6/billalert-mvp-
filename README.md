# billalert-mvp-
AI civic engagement MVP: tracks AZ bills, summarizes with LLM, demo build.
# BillAlert MVP

BillAlert is an AI-powered platform that tracks Arizona state legislation, summarizes bills in plain language, and shows users bills based on selected interests.

## MVP Flow
Login → Select Preferences → View Filtered Bills → Read AI Summaries

## Scope (MVP Only)
- Arizona bills only
- Interest-based filtering (healthcare, education, taxes, housing, etc.)
- 3–4 sentence AI summaries
- Demo login (no real accounts)
- In-memory sessions (no database)

## Repo Structure
- /frontend — UI (login, preferences, dashboard)
- /backend — API + LLM wrapper + bill fetching
- /docs — notes, diagrams, demo script, presentation support
