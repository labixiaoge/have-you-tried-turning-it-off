# Have You Tried Turning It Off?

[![make.fun · u-motasimfuad-have-you-tried-turning-it-off-154a938b](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/labixiaoge/have-you-tried-turning-it-off/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/labixiaoge/have-you-tried-turning-it-off/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)

make.fun bounty entry: one funny line, under 200 characters, that a hopeless
tech support agent says to a desperate customer.

## The line

> Have you tried turning it off and on again? I just did — now neither of
> us has internet, but at least we are in this together.

126 characters. It twists the classic "turn it off and on again": the agent
tried it too and knocked their own internet out, so the joke is the agent's
cheerful uselessness — the customer is never the butt of it.

## How it works

`main.py` (the entrypoint the grader runs) writes the line, and nothing
else, to `/output/entry.txt`. No network, no secrets, no external files.

Run it locally to verify:

```bash
python3 main.py          # writes /output/entry.txt
```

or with a custom output path:

```bash
ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
```

## Competition

- Slug: `u-motasimfuad-have-you-tried-turning-it-off-154a938b`
- Prize pool: $10 (top 10 share it, 1st place $3.10)
- Deadline: 2026-11-26 05:25 CST
- Gate: `/output/entry.txt` must be UTF-8 text of 1–199 characters
