from collections import Counter
from itertools import product
import random
#from Board import *


def evaluate(guess, secret):
    """Return the pair (bulls, cows) where `bulls` is a count of the
    characters in `guess` that appear at the same position in `secret`
    and `cows` is a count of the characters in `guess` that appear at
    a different position in `secret`.

        >>> evaluate('ABCD', 'ACAD')
        (2, 1)
        >>> evaluate('ABAB', 'AABB')
        (2, 2)
        >>> evaluate('ABCD', 'DCBA')
        (0, 4)

    """
    matches = sum((Counter(secret) & Counter(guess)).values())
    bulls = sum(c == g for c, g in zip(secret, guess))
    return bulls, matches - bulls

def knuth(secret):
    """Run Knuth's 5-guess algorithm on the given secret."""
    assert(secret in ALL_CODES)
    codes = ALL_CODES
    key = lambda g: max(Counter(evaluate(g, c) for c in codes).values())
    guess = 'AABB'
    while True:
        feedback = evaluate(guess, secret)
        print("Guess {}: feedback {}".format(guess, feedback))
        if guess == secret:
            break
        codes = [c for c in codes if evaluate(guess, c) == feedback]
        if len(codes) == 1:
            guess = codes[0]
        else:
            guess = min(ALL_CODES, key=key)


pattern = [random.choice('ABCDEF') for _ in range(4)]
ALL_CODES = [''.join(c) for c in product('ABCDEF', repeat=4)]








