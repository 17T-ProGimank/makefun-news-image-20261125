"""news-image-20261125 entrypoint.

Writes the finished poster for Wednesday 25 November 2026 to
$MAKEFUN_OUTPUT_DIR/entry.png. The poster is drawn in advance by
draw_poster.py (Pillow + DejaVu, run locally) and committed as
entry.png at the repository root, because the grader's Python image
carries only the standard library -- no Pillow, no fonts -- so the
entrypoint itself must not import anything beyond the stdlib.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # The gate refuses anything over 1 MiB or larger than 1024x1024;
    # the committed poster is 1024x1024 and well under the size cap,
    # but refuse loudly here rather than shipping a bad file.
    if os.path.getsize(dst) > 1048576:
        print("entry.png exceeds 1 MiB", file=sys.stderr)
        return 1
    # Sanity check the copy is really a PNG before reporting success.
    with open(dst, "rb") as fh:
        if fh.read(8) != b"\x89PNG\r\n\x1a\n":
            print("entry.png is not a PNG", file=sys.stderr)
            return 1
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
