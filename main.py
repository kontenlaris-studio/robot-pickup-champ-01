"""The Robot Pickup Line Championship entry: the update he stopped avoiding."""

import os

TEXT = (
    "Are you a software update? Because I've been avoiding you all week, "
    "but tonight I finally want to see what changes."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    print(f"wrote {path} ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
