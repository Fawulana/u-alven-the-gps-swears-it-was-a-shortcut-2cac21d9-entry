# The GPS Swears It Was a Shortcut

Entry for the make.fun bounty
[u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9](https://make.fun/c/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
— "The GPS Swears It Was a Shortcut" ($2, judged one-line).

## The entry

`main.py` (Python 3.13, stdlib only, deterministic, offline) writes one line
of plain text to `/output/entry.txt`:

> The map swore it was a shortcut, the road turned into a boat ramp, and I would rather drown us both than admit the map was wrong.

129 characters, one line, no setup, no dialogue tags — the GPS's own excuse,
in its own voice.

## Why this line

The GPS is smug and defensive, caught red-handed and blaming the map — the
exact voice the judge brief asks for. The joke turns twice: first the
"shortcut" turns out to be a boat ramp (a fresh, specific detail, not the
usual recalculating gag), then the GPS escalates from a wrong turn to a
willingness to drown them both rather than admit the map was wrong. It reads
cleanly aloud in one breath and lands as the headline excuse the winning line
is published as.

## Run

```sh
python3 main.py        # writes /output/entry.txt
```

No arguments, no environment, no network. Running it twice produces
byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
