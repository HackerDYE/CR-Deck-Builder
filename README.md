# RoyaleDeckBuilder

**A personalized Clash Royale deck recommendation tool.**

> Project status: Planning / Day 1 — this is my first mini project.

## Overview

The strongest meta deck is not always the best deck for an individual player. A player may own certain cards at high levels, know some archetypes well, or lack the resources to upgrade a popular deck.

RoyaleCoach aims to recommend **practical decks and card upgrades** by combining a player's collection with a small set of candidate decks. Over time, it may also consider reliable, permitted meta and battle statistics.

## The problem

Existing deck rankings help players identify strong decks, but they do not always answer:

- Which deck fits **my current card levels**?
- Which deck can I use **without upgrading many cards**?
- Which cards should I **prioritize upgrading**?
- Why is one deck a better fit for me than another?

## Minimum viable product (MVP)

The first working version will:

1. Read a sample player profile from a local JSON file.
2. Compare the player's card collection against **5–10 manually curated decks**.
3. Recommend the best **three** candidate decks.
4. Explain the recommendations using transparent rules (for example, available cards and card levels).
5. Suggest a card to upgrade for each recommended deck.

**Important:** The first version will run locally with sample data. It will not need a live API, a chatbot, or a website.

## Planned features (not implemented yet)

- Enter a Clash Royale player tag and load a profile using the official Clash Royale API.
- Show a player's card levels and current deck.
- Add a simple Streamlit web interface.
- Include up-to-date meta information when a permitted, reliable data source is available.
- Analyze matchups or personal win rates **only when enough match data exists**; display sample sizes.
- Optionally use an LLM to explain recommendations, while keeping scores and evidence checkable.

## Proposed technology

- **Python** — core logic and data processing
- **JSON** — sample player profiles and candidate decks
- **Git & GitHub** — version control and project history
- **Requests** — API requests (later)
- **pytest** — tests (later)
- **Streamlit** — optional web interface (later)

## Roadmap

- [x] Decide on the project idea and scope.
- [x] Write the initial README.
- [ ] Create the repository and make the first commit.
- [ ] Learn basic Python dictionaries, lists, functions, and JSON.
- [ ] Create a sample player profile and five sample decks.
- [ ] Implement a basic deck-matching algorithm.
- [ ] Show the top three recommendations with explanations.
- [ ] Add basic tests.
- [ ] Connect to the official Clash Royale API.
- [ ] Build a simple interface.
- [ ] Evaluate and improve recommendations.

## Initial recommendation approach

Start with explainable rules, not machine learning:

- **Availability:** Does the player have all required cards?
- **Levels:** Are the deck's cards sufficiently upgraded for the player's intended mode?
- **Familiarity (later):** Has the player used some of these cards recently?
- **Meta strength (later):** Is there a reliable, dated dataset supporting this deck?

The recommender will state *why* it chose a deck. Scores and their weights are experimental and will be tested, not treated as objective truths.

## Data sources and limitations

- Planned player data source: [Official Clash Royale API](https://developer.clashroyale.com/).
- [RoyaleAPI](https://royaleapi.com/) is a useful website for research, but its public developer API was discontinued. **This project will not rely on scraping RoyaleAPI.**
- A recent battle log is not a complete lifetime match history. Any win-rate or matchup analysis must disclose the sample size and may be unavailable.
- API keys are secrets and must never be committed to GitHub.
- This project provides **out-of-game advice**, not gameplay automation.

## Current state

This repository is in the planning stage. No functional recommendation engine has been implemented yet.

## Disclaimer

This material is unofficial and is not endorsed by Supercell. For more information see [Supercell's Fan Content Policy](https://supercell.com/en/fan-content-policy/).
