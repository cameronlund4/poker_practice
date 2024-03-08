import sys
from deuces import Deck, Card, Evaluator
from random import randint

MIN_PLAYERS = 2
MAX_PLAYERS = 10


def deal_hand():
    pass

def table_to_string(hand: list[Card]) -> str:
    return ''.join(Card.int_to_pretty_str(card).strip() for card in hand)

def print_table(table: list[Card], hands: list[list[Card]], classes: list[str] | None = None) -> None:
    print(f"Table: {table_to_string(table)}")
    for i, hand in enumerate(hands):
        hand_class = ""
        if classes:
            hand_class = f" ({classes[i]})"
        print(f"\tPlayer {i+1}: {table_to_string(hand)}{hand_class}")

def get_max_hand_count():
    while True:
        players_text = input(
            f"How many players max per hand? ({MIN_PLAYERS}-{MAX_PLAYERS}): "
        )
        try:
            players = int(players_text)
        except Exception:
            continue
        if not MIN_PLAYERS <= players <= MAX_PLAYERS:
            continue
        return players

def get_winner_guess_or_quit(hand_players: int, wins: int, losses: int):
    while True:
        winner_guess_text = input(
            f"Which player wins? (quit|1-{hand_players}): "
        )
        if winner_guess_text == "quit":
            print(f"Exiting. Got {wins}/{wins+losses} correct.")
            sys.exit(0)
        try:
            winner_guess = int(winner_guess_text) - 1
        except Exception:
            continue
        if not 0 <= winner_guess <= hand_players - 1:
            continue
        return winner_guess, winner_guess_text

def main():
    max_hand_count = get_max_hand_count()
    evaluator = Evaluator()
    wins = 0
    losses = 0
    while True:
        deck = Deck()
        hand_players = randint(MIN_PLAYERS, max_hand_count)

        table = deck.draw(5)
        hands = [deck.draw(2) for _ in range(hand_players)]
        evaluations = [evaluator.evaluate(table, hand) for hand in hands]
        classes = [evaluator.class_to_string(evaluator.get_rank_class(e)) for e in evaluations]
        winning_score = min(evaluations)

        winners = [i for i, e in enumerate(evaluations) if e == winning_score]
        winner_text = ",".join([str(winner+1) for winner in winners])

        print_table(table, hands)
        print()

        winner_guess, winner_guess_text = get_winner_guess_or_quit(hand_players, wins, losses)
        print_table(table, hands, classes)
        print()

        if winner_guess not in winners:
            print(f"WRONG! Winner was {winner_text} ({classes[winners[0]]}), not {winner_guess_text} ({classes[winner_guess]})")
            losses += 1
        else:
            print(f"Correct! {winner_text} wins with {classes[winner_guess]}")
            wins += 1

        print("\n-------------------------------------\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Failed unexpectedly! {str(exc)}")
        sys.exit(1)
