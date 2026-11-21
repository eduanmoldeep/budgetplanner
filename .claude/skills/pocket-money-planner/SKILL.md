---
name: pocket-money-planner
description: Simple pocket money planner. Use when the user wants to plan, track, or review pocket money or a small personal budget — logging income or spending, setting a monthly allowance or savings goal, checking what's left, or getting a weekly spending limit.
---

# Pocket Money Planner

Keep it small and friendly. Money data lives in `pocket-money.csv` in the user's working directory (not in this skill folder).

## Ledger format

`pocket-money.csv`, header row required:

```
date,type,category,amount,note
2026-11-01,income,allowance,100.00,Monthly allowance
2026-11-03,expense,snacks,4.50,Lunch
```

- `type`: `income` or `expense`
- `amount`: positive number, no currency symbol
- `date`: `YYYY-MM-DD`

Optional goal line in `pocket-money.goal` (plain text): `name,target_amount` e.g. `Headphones,60`.

## Workflow

1. **Setup (first use):** If `pocket-money.csv` is missing, create it with the header. Ask the user once for their monthly allowance and any savings goal; add the allowance as an `income` row and write the goal file.
2. **Log:** For "I spent 5 on snacks" or "got 20 from grandma", append a row (use today's date unless told otherwise). Pick a short lowercase category (snacks, transport, games, clothes, gifts, other). Confirm in one line with the new balance.
3. **Review:** Run `python3 scripts/summary.py pocket-money.csv` (path relative to this skill folder) and relay the output: balance, spending by category, days left in month, and a safe daily/weekly spend.
4. **Plan:** Suggest the simple split 50% needs / 30% wants / 20% savings only if the user has no plan of their own. If a goal exists, say how much per week reaches it by when.

## Rules

- Never invent transactions; ask if an amount is unclear.
- Use the user's currency symbol if they mention one; otherwise show plain numbers.
- Warn gently when spending in a category exceeds 40% of income for the month.
- Keep replies short — a balance and one tip, not a lecture.
