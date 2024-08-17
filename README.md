# randrg, a Deep Rock Galactic Randomizer

[Deep Rock Galactic](https://store.steampowered.com/app/548430/Deep_Rock_Galactic/) is a Co-Op bug shooting game and this is a tool to provide a randomized build. Recommended paired with [Random Mission Selection](https://drg.mod.io/random-mission-selection) or similar for the optimal random experience.

## Features:

- Random class

- Random primaries and secondaries

- Random build numbers and overclocks

- Random grenades

- Random perks

- 25% better RNG button (don't ask)

## To Run

You need [Python](https://www.python.org/) and [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/). Download ```randrg.py``` and run it with ```py randrg.py``` or similar.

## To Build

Randrg requires a `meta.json` file for some features. A copy of this file, generated on 08/16/24, is provided in the repo. To generate your own, follow the following steps:

1. Delete `raw.txt`, if it exists
1. Run `scraper.py`, this generates `raw.txt`
1. Run `keyChanger.py`, which performs pre-processing into `raw.json`
1. Run `parser.py`, which takes all of the builds and compresses them into `parsed.json`
1. Run `meta.py`, which takes the compressed builds and figures out how "meta" each upgrade is in `meta.json`
