def analyze_deck(deck, deck_roles, role_warnings):

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