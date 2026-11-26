"""A tiny helper that saves a short note to my younger self.

Running this script produces a single-line text file holding one
sentence I wish I had heard earlier. Nothing is fetched, nothing is
sent anywhere; the program only writes a local file.
"""

from pathlib import Path


def main() -> None:
    # One sentence, kept short enough to fit the bounty limit.
    message = "Dear younger me: stop apologizing for taking up space. The rooms that want you small were never built for you anyway."

    if not message:
        raise SystemExit("Entry is empty, so nothing was written.")
    if "\n" in message or "\r" in message:
        raise SystemExit("Entry must stay on a single line.")
    if not 1 <= len(message) <= 200:
        raise SystemExit("Entry must be between 1 and 200 characters long.")

    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(message + "\n", encoding="utf-8")
    print(f"Wrote {len(message)} characters to {target}")


if __name__ == "__main__":
    main()
