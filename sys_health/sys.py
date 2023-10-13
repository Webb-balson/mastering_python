from pathlib import Path
import sys

all_args = sys.argv[1:]
opts = [opt for opt in all_args if opt.startswith("-")]
args = [opt for opt in all_args if not opt.startswith("-")]

fname = Path(__file__).name

if len(args) == 0:
    t = [opt for opt in all_args if opt.startswith("-t")]
    p = [opt for opt in all_args if not opt.startswith("-p")]

    if t:
        try:
            time_o = int(t[0].split("=")[-1])
        except ValueError:
            print("Please enter a valid timeout integer")
    else:
        time_o = 5

    if t:
        try:
            time_o = int(t[0].split("=")[-1])
        except ValueError:
            print("Please enter a valid timeout integer")
    else:
        perc6
    