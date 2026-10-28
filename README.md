# RoyaleDeckBuilder

A beginner-friendly **Clash Royale deck analyzer** built with Python.

> **Status:** Early working prototype — my first software mini project.

## Overview

RoyaleDeckBuilder is a small project for exploring how Clash Royale decks are put together. It reads a deck from a JSON file and checks basic characteristics such as average elixir cost, win conditions, defensive options, and spell coverage.

The goal of **version 1** is not to find the perfect deck or recreate the judgment of an experienced player. It is to build a simple, explainable program while learning Python, JSON, and Git.

## What it does now

- Loads card data from `cards.json`.
- Calculates the deck's average elixir cost.
- Counts how many cards cover each role, based on manually assigned tags.
- Reports whether each role has **no option**, **one option**, or **multiple options**.

The current role checks include:

- Win conditions
- Heavy-push defense (anti-tank or defensive buildings)
- Hog Rider defense
- Swarm or distraction
- Small spells and big spells
- Air defense
- Splash damage

These checks are **guidelines, not a deck-quality score**. Some effective decks intentionally lack a conventional role or use multiple offensive cards instead.

## Getting started

### Requirements

- Python 3
- Any code editor (VS Code recommended)

No third-party Python packages are required for the current version.

### Run locally

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Make sure `main.py` and `cards.json` are in the same folder.
4. From the VS Code terminal on Windows, run:

   `py main.py`

Edit the eight card entries in `cards.json` to experiment with a different deck, then run the program again.

### Project structure

    RoyaleDeckBuilder/
    ├── main.py       # Load data and analyze a deck
    ├── cards.json    # Example deck and card-role tags
    └── README.md     # Project documentation

## Card data

Each card currently has a name, elixir cost, and a list of custom role tags:

    {
      "name": "Skeletons",
      "elixir": 1,
      "tags": ["cycle", "swarm", "distraction"]
    }

The tags are manually chosen for this prototype. They describe possible roles, **not guaranteed counters**. For example, two cards marked `anti_hog` may not be equally reliable against Hog Rider.

## Scope and roadmap

### Version 1: Basic deck analyzer

- [x] Set up Python and VS Code.
- [x] Store sample cards in JSON.
- [x] Load JSON data in Python.
- [x] Calculate average elixir.
- [x] Check and count basic deck roles.
- [ ] Allow users to choose a deck without manually editing JSON.
- [ ] Add basic validation and tests.
- [ ] Improve the clarity of analysis messages.

### Possible future features (not commitments)

- Simple deck suggestions from a small list of existing decks.
- Favorite-card and elixir-preference filters.
- Better handling of card synergy, matchup coverage, and different deck archetypes.
- Player card levels and profiles from the official Clash Royale API.
- A simple web interface.

**Not in version 1:** AI coaching, automatically generating competitive decks, live meta tracking, detailed matchup predictions, or a comprehensive card-synergy database.

## Limitations

- Role tags are subjective and incomplete.
- Counting matching tags does not measure counter strength, card synergy, or win rate.
- The current program analyzes the cards in a local JSON file; it does not fetch live game data.
- An unusual but viable deck may trigger warnings because it breaks conventional deck-building guidelines.

## Why I'm building this

I enjoy Clash Royale and often help friends think about deck choices. This is a way to combine that interest with learning software development. The priority is to finish a small project I understand, then improve it if time and experience allow.

## Disclaimer

This is an unofficial fan project and is not endorsed by Supercell. See [Supercell's Fan Content Policy](https://supercell.com/en/fan-content-policy/).