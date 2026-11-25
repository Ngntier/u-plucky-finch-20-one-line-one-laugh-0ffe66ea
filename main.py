"""One Line, One Laugh.

Writes a single funny line of at most 200 characters to entry.txt
inside the output directory make.fun's grader reads.
"""

import os

ENTRY = "I asked the void for a sign and it sent me a CAPTCHA."


def main():
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(ENTRY))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
