#!/usr/bin/env python3
"""Summarize a pocket money ledger CSV for the current month."""
import calendar
import csv
import sys
from collections import defaultdict
from datetime import date


def main(path):
    today = date.today()
    income = expense = 0.0
    by_cat = defaultdict(float)
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            d = date.fromisoformat(row["date"])
            if (d.year, d.month) != (today.year, today.month):
                continue
            amt = float(row["amount"])
            if row["type"] == "income":
                income += amt
            elif row["type"] == "expense":
                expense += amt
                by_cat[row["category"]] += amt

    balance = income - expense
    days_left = calendar.monthrange(today.year, today.month)[1] - today.day + 1
    print(f"Month: {today:%B %Y}")
    print(f"Income:  {income:.2f}")
    print(f"Spent:   {expense:.2f}")
    print(f"Balance: {balance:.2f}")
    if by_cat:
        print("By category:")
        for cat, amt in sorted(by_cat.items(), key=lambda x: -x[1]):
            pct = f" ({amt / income:.0%} of income)" if income else ""
            print(f"  {cat}: {amt:.2f}{pct}")
    if balance > 0:
        per_day = balance / days_left
        print(f"Days left: {days_left} -> safe spend {per_day:.2f}/day, {per_day * 7:.2f}/week")
    else:
        print("No money left to spend this month.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: summary.py pocket-money.csv")
    main(sys.argv[1])
