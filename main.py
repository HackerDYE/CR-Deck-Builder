# RoyaleDeckBuilder - First Python Program

import json

# ==============================
# RoyaleDeckBuilder - Deck Selection
# ==============================


# Load available cards
with open("cards.json", "r", encoding="utf-8") as file:
    available_cards = json.load(file)

# Display available cards
print("===== AVAILABLE CARDS =====")

# Sort cards by elixir (ascending)
available_cards = sorted(available_cards, key=lambda card: card["elixir"])  

for index, card in enumerate(available_cards, start=1):
    print(f"{index}. {card['name']} ({card['elixir']} elixir)")

# Ask the user to choose 8 cards

# Select 8 cards
while True:
    user_input = input(
        "\nEnter 8 card numbers separated by commas (or q to quit): "
    )

    if user_input.lower().strip() == "q":
        print("Goodbye!")
        raise SystemExit

    try:
        numbers = [
            int(x.strip()) for x in user_input.split(",")
        ]
    except ValueError:
        print("Please enter numbers only!")
        continue

    if len(numbers) != 8:
        print("A deck must contain exactly 8 cards!")
        continue

    if len(set(numbers)) != 8:
        print("You cannot select the same card twice!")
        continue

    if any(n < 1 or n > len(available_cards) for n in numbers):
        print("One or more card numbers are invalid!")
        continue

    # All checks passed
    break

# Build the selected deck
cards = [available_cards[n - 1] for n in numbers]

print("\n===== YOUR DECK =====")

for card in cards:
    print(f"- {card['name']}")


# Deck roles we want to analyze
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


def analyze_deck(deck, deck_roles):

    print("\n===== DECK ANALYSIS =====")

    # 1. Average elixir
    total_elixir = 0

    for card in deck:
        total_elixir += card["elixir"]

    average_elixir = total_elixir / len(deck)

    print(f"Average Elixir: {average_elixir:.2f}")

    # 2. Minimum 4-card cycle
    sorted_cards = sorted(
        deck, key=lambda card: card["elixir"]
    )

    min_four_cards = 0

    for card in sorted_cards[:4]:
        min_four_cards += card["elixir"]

    print(f"Minimum 4-Card Cycle: {min_four_cards}")

    print("Cycle Cards:")
    for card in sorted_cards[:4]:
        print(f"- {card['name']}")

    # 3. Deck role analysis
    print("\n===== ROLE COVERAGE =====")

    for role, required_tags in deck_roles.items():

        count = 0

        for card in deck:
            for tag in required_tags:
                if tag in card["tags"]:
                    count += 1
                    break

        print(f"{role}: {count}")


#Analyze Deck
analyze_deck(cards, deck_roles)