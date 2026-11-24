"""Dad Joke Showdown entry: one dad joke, at most 200 characters.

Writes a single dad joke to /output/entry.txt. Deterministic, no network,
no randomness, no environment secrets.
"""

import os

JOKE = "My guitar never worries. It just frets a little."

# Gate self-check: the sealed scorer only accepts 1-200 characters of
# non-whitespace UTF-8. Fail loudly here instead of shipping a bad entry.
# (Counted: 48 characters.)
assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, gate needs 1-200"
assert JOKE.strip(), "joke must not be whitespace only"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
