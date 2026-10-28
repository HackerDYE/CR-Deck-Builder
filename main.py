# RoyaleDeckBuilder - First Python Program

import json

with open("cards.json", "r", encoding="utf-8") as file:
    cards = json.load(file)

print("Welcome to RoyaleDeckBuilder!")

for card in cards:
    print(card["name"], "-", card["elixir"], "elixir", card["tags"])



# Calculate average elixir

total_elixir = 0

for card in cards:
    total_elixir += card["elixir"]

average_elixir = total_elixir / len(cards)

print("Average Elixir:", average_elixir)




# ==============================
# RoyaleDeckBuilder - Analyzer V2
# ==============================

def count_cards_with_any_tag(required_tags):
    count = 0

    for card in cards:
        for tag in required_tags:
            if tag in card["tags"]:
                count += 1
                break

    return count


# Roles we want to analyze
deck_roles = {
    "Win conditions": ["win_condition"],
    "Heavy-push defense": ["anti_tank", "defensive_building"],
    "Anti-Hog options": ["anti_hog"],
    "Swarm / Distraction": ["swarm", "distraction"],
    "Small spells": ["small_spell"],
    "Big spells": ["big_spell"],
    "Air defense": ["anti_air"],
    "Splash damage": ["splash"]
}


print("\n===== DECK ANALYSIS V2 =====")

for role, tags in deck_roles.items():
    count = count_cards_with_any_tag(tags)

    if count == 0:
        status = "MISSING"
    elif count == 1:
        status = "ONE OPTION"
    else:
        status = "MULTIPLE OPTIONS"

    print(f"{role}: {count} ({status})")

