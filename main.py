#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one ~100-word monologue to /output/entry.txt. Deterministic,
Python 3.13 stdlib only, no network, no input files.
"""

MONOLOGUE = (
    "Hero. Sit. No, stand, if you must. The chair knows my weight "
    "better than I do. You came for the Ember Crown, yes? Third Tuesday "
    "this month. I had it polished, had a speech. Where was I? Ah. The "
    "crown. It opens the Ashen Gate, wakes the old fire, burns the kingdom "
    "to a clean slate. Very dramatic. Very me, once. Look, the kettle's "
    "on. Stay for tea, and I'll tell you which tower it's in. Take it. "
    "Then I can finally... no. Monologue first. I rehearsed this three "
    "hundred years. I keep losing the thread just before I win."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MONOLOGUE + "\n")


if __name__ == "__main__":
    main()
