"""Run FlySort from an editor's Run button or with ``python run.py``.

    python run.py                  watch the fly sort a demo list in your browser
    python run.py 42 7 19 3        watch it sort your numbers
    python run.py --text 42 7 19   print the comparisons in the terminal instead

The first run downloads about 135 MB of connectome data into ./data.
"""

import os
import sys

# Run from the project folder, whichever folder the editor started in, so the
# package and ./data are found.
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sys.path.insert(0, HERE)

try:
    import numpy, pandas, pyarrow, scipy  # noqa: E401,F401
except ImportError as missing:
    sys.exit(
        f"FlySort needs a library that isn't installed yet ({missing.name}).\n"
        f"Install everything it needs with:\n\n"
        f'    "{sys.executable}" -m pip install -e "{HERE}"\n'
    )

if __name__ == "__main__":
    args = sys.argv[1:]
    if "--text" in args:
        args.remove("--text")
        from flybrain_sort.__main__ import main

        main(args or ["42", "7", "19", "3", "88", "61", "25", "50"])
    else:
        from flybrain_sort.gui import main

        main(args)
