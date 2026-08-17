#!/usr/bin/env python3
"""Score and rank outbound hypotheses on the pre-launch rubric (SKILL.md, Step 4).

Scale per factor: 0, 1, 3 or 5. Weights are fixed:
    proof 0.25 · pain 0.25 · trigger 0.20 · volume 0.10 · data_cost 0.10 · speed 0.10

Hard rules encoded here:
  * a 0 on `proof` or `pain` drops the hypothesis from the queue regardless of the total
  * the top 3 totals go into work, everything else waits (the 3.2 threshold is secondary)
  * a hypothesis that failed the stop-filter gate is never scored — pass "gate": false

Input: a JSON file holding a list of objects.

    [
      {
        "name": "Contractors 50-200, opened a coordinator role → coordination offload",
        "gate": true,
        "scores": {"proof": 5, "pain": 5, "trigger": 3, "volume": 3, "data_cost": 3, "speed": 5},
        "why": {"proof": "case with a number in this exact niche"}
      }
    ]

`gate` and `why` are optional. A missing factor is an error, not a zero — an unscored
factor means the input is incomplete, and silently reading it as 0 would kill the row.

Usage:
    python3 score.py hypotheses.json            # English labels
    python3 score.py hypotheses.json --lang uk  # Ukrainian labels

Output: a ranked markdown table on stdout, ready to paste into the report.
"""

import argparse
import json
import sys

WEIGHTS = {
    "proof": 0.25,
    "pain": 0.25,
    "trigger": 0.20,
    "volume": 0.10,
    "data_cost": 0.10,
    "speed": 0.10,
}

LABELS = {
    "en": {
        "proof": "Proof", "pain": "Pain", "trigger": "Trigger", "volume": "Volume",
        "data_cost": "Data", "speed": "Speed", "name": "Hypothesis", "total": "Total",
        "status": "Status", "launch": "launch", "queue": "queue",
        "dropped": "dropped (zero: {killer})", "gate_fail": "failed the gate",
        "proof_word": "proof", "pain_word": "pain sharpness",
        "summary": "Into work: {launched} of {total}. Waiting: {waiting}. "
                   "Dropped or failed the gate: {out}.",
    },
    "uk": {
        "proof": "Доказ", "pain": "Гострота", "trigger": "Тригер", "volume": "Обсяг",
        "data_cost": "Дані", "speed": "Швидкість", "name": "Гіпотеза", "total": "Сума",
        "status": "Статус", "launch": "запуск", "queue": "черга",
        "dropped": "знято (нуль: {killer})", "gate_fail": "не пройшла ворота",
        "proof_word": "доказ", "pain_word": "гострота проблеми",
        "summary": "У роботу: {launched} з {total}. Чекають: {waiting}. "
                   "Знято або не пройшли ворота: {out}.",
    },
}

VALID = {0, 1, 3, 5}
LAUNCH_SLOTS = 3


def evaluate(item, lang):
    t = LABELS[lang]
    name = item.get("name", "(unnamed)")
    if item.get("gate", True) is False:
        return {"name": name, "total": None, "status": t["gate_fail"], "scores": {}}

    scores = item.get("scores", {})
    missing = [f for f in WEIGHTS if f not in scores]
    if missing:
        sys.exit(f"'{name}': unscored factors: {', '.join(missing)}")
    bad = {f: v for f, v in scores.items() if v not in VALID}
    if bad:
        sys.exit(f"'{name}': scores outside the 0/1/3/5 scale: {bad}")

    total = sum(scores[f] * w for f, w in WEIGHTS.items())
    if scores["proof"] == 0 or scores["pain"] == 0:
        killer = t["proof_word"] if scores["proof"] == 0 else t["pain_word"]
        return {"name": name, "total": total,
                "status": t["dropped"].format(killer=killer), "scores": scores}
    return {"name": name, "total": total, "status": t["queue"], "scores": scores}


def main():
    parser = argparse.ArgumentParser(description="Rank outbound hypotheses for launch.")
    parser.add_argument("input", help="JSON file with the hypothesis list")
    parser.add_argument("--lang", choices=sorted(LABELS), default="en",
                        help="label language of the output table (default: en)")
    opts = parser.parse_args()
    lang = opts.lang

    with open(opts.input, encoding="utf-8") as fh:
        items = json.load(fh)

    t = LABELS[lang]
    rows = [evaluate(i, lang) for i in items]
    ranked = sorted([r for r in rows if r["status"] == t["queue"]],
                    key=lambda r: r["total"], reverse=True)
    for r in ranked[:LAUNCH_SLOTS]:
        r["status"] = t["launch"]
    rest = [r for r in rows if r["status"] not in (t["queue"], t["launch"])]

    header = ["#", t["name"]] + [t[f] for f in WEIGHTS] + [t["total"], t["status"]]
    print("| " + " | ".join(header) + " |")
    print("|" + "---|" * len(header))
    for n, r in enumerate(ranked + rest, 1):
        cells = [str(n), r["name"]]
        cells += [str(r["scores"].get(f, "—")) for f in WEIGHTS]
        cells += [f"{r['total']:.2f}" if r["total"] is not None else "—", r["status"]]
        print("| " + " | ".join(cells) + " |")

    launched = min(len(ranked), LAUNCH_SLOTS)
    print()
    print(t["summary"].format(launched=launched, total=len(rows),
                              waiting=len(ranked) - launched, out=len(rest)))


if __name__ == "__main__":
    main()
