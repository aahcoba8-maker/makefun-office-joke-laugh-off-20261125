"""One-line office joke entry for make.fun.

Writes the joke to entry.txt in the output directory the grader provides
(MAKEFUN_OUTPUT_DIR), falling back to the script directory when unset.
The file holds exactly the joke bytes, no trailing newline, so the entry
stays as small as possible (the leaderboard tie-break favours fewer bytes).
"""

import os

JOKE = "I asked my boss for a raise and he gave me a standing desk \u2014 technically, I'm taller now."

# The sealed gate accepts UTF-8 text of 1 to 200 characters, not only
# whitespace. Check the joke against it before writing, so a bad edit
# fails loudly here instead of silently scoring 0 on the server.


def main():
    if not (1 <= len(JOKE) <= 200 and JOKE.strip()):
        raise SystemExit("joke fails the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the joke bytes, which also
    # keeps the Size column (the tie-break) as small as possible.
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
