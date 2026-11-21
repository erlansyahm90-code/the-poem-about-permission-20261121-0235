[![make.fun](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![Rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/erlansyahm90-code/the-poem-about-permission-20261121-0235/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![Reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/erlansyahm90-code/the-poem-about-permission-20261121-0235/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)

# The poem about permission

Entry for the [make.fun bounty "The poem about permission"](https://make.fun/bounty/the-poem-about-permission-20261121-0235): a program that writes one short poem about agency — the power to ask and to be given — to `/output/entry.txt`.

## The poem

> Ask, and the door learns your name.
> Not a key, not a command —
> a small yes, freely given,
> turns a locked room into a road.
> Permission is not power taken;
> it is a door held open, one question at a time.

201 characters (Unicode code points), 203 bytes, UTF-8.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the poem to `$MAKEFUN_OUTPUT_DIR/entry.txt`, defaulting to `/output/entry.txt`. The output is deterministic: every run produces the same bytes.

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/poem-out python3 main.py
cat /tmp/poem-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
