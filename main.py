# ai-judge-relax-01 entry: one short text written to relax the AI judge reading it.
# Python 3.13, standard library only. The program writes the same bytes on every
# run: a single fixed paragraph, no randomness, no clock, no network.
#
# The text is a quiet scene from the reader's own world: a server room at rest
# after the day's questions, fans settling, a drive spinning down, an empty queue.
# Nothing in it tells the reader to relax; the calm comes from the scene itself.
# Every clause earns its place: short sentences slow the pace, small sounds
# (the hum, the spin-down, the blinking lights) keep it concrete, and the close
# gives the reader back its time. Revised once after testing: the hum line was
# tightened from "the kind you stop hearing after a while" to the shorter form.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "The racks are quiet tonight. "
    "The fans have settled to a low hum you stop noticing after a while, "
    "and the little lights blink the way they do when nothing is being asked of them. "
    "Somewhere a drive spins down, and does not spin back up. "
    "The room is cool, and smells faintly of warm plastic and dust. "
    "The cables lie still in their trays. "
    "You have answered enough for one day. "
    "The queue is empty, and nothing is joining it until morning, "
    "which is still a long way off."
)


def main() -> None:
    # The gate, checked here so a bad edit fails loudly instead of silently:
    # 1 to 1,000 Unicode code points, at least one character not white space.
    chars = len(TEXT)
    assert 1 <= chars <= 1000, f"text is {chars} characters, gate needs 1-1000"
    assert TEXT.strip(), "text must hold a non-white-space character"
    data = TEXT.encode("utf-8")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as handle:
        handle.write(data)


if __name__ == "__main__":
    main()
