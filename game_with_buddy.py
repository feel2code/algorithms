# ID 69075418


def welcome_to_the_club_buddy(game: list, fisting: int):
    """Check how much holes you can cover."""
    game = list(map(int, list(
        (''.join(game)).replace('.', '')
    )))
    biba = dict((x, game.count(x)) for x in set(game) if game.count(x) > 0)
    hole = 0
    for i in biba.values():
        if i <= fisting:
            hole += 1
    return hole


if __name__ == '__main__':
    buddies = 2
    fisting = int(input()) * buddies
    game = []
    for i in range(0, 4):
        game.append(str(input()))
    print(welcome_to_the_club_buddy(game, fisting))
