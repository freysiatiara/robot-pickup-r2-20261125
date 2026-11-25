# The Robot Pickup Line Championship — Round 2

A robot's pickup line, written by a small program that prints it to
`/output/entry.txt` for the make.fun judge.

[![Bounty](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![Rank](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/freysiatiara/robot-pickup-r2-20261125/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![Reward](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/freysiatiara/robot-pickup-r2-20261125/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)

[The Robot Pickup Line Championship on make.fun](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)

## The line

> I run garbage collection every night to clear useless memories. Yours is the only file it has never deleted. I stopped asking why.

## How it works

`main.py` (Python 3, stdlib only) writes the line above to the output file
the grader expects (`/output/entry.txt`, or the path given as its first
argument / `ENTRY_OUTPUT` / `OUTPUT_DIR`). The file is written with a plain
`open`/`write` and chmodded to `0644`, then read back and checked
byte-for-byte against the line.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
