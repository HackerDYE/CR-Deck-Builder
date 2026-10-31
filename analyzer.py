def calculate_average_elixir(deck):
    total_elixir = 0

    for card in deck:
        total_elixir += card["elixir"]

    return total_elixir / len(deck)


def calculate_min_four_card_cycle(deck):
    sorted_cards = sorted(
        deck, key=lambda card: card["elixir"]
    )

    total = 0

    for card in sorted_cards[:4]:
        total += card["elixir"]

    return total


def analyze_deck(deck, deck_roles, role_warnings):
    print("\n===== DECK ANALYSIS =====")

    #Deck Statistics
    average = calculate_average_elixir
    cycle = calculate_min_four_card_cycle(deck)

    print(f"Average Elixir: {average:.2f}")
    print(f"Minimum 4-Card Cycle: {cycle}")


    # Deck role analysis
    print("\n===== ROLE COVERAGE =====")

    for role, required_tags in deck_roles.items():

        matching_cards = []

        for card in deck:
            for tag in required_tags:
                if tag in card["tags"]:
                    matching_cards.append(card["name"])
                    break

        print(f"\n{role}: {len(matching_cards)}")

        if len(matching_cards) == 0:
            print("  Potential weakness:")
            print(f"  {role_warnings[role]}")

        else:
            for name in matching_cards:
                print(f"  - {name}")

