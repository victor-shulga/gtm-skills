#!/usr/bin/env python3
"""
structural.py — structural (non-lexical) AI-writing detectors for detect.py.

Lexical detectors catch WORDS. These catch CONSTRUCTIONS: rhetorical shapes that
contain no banned vocabulary, no em dash and no AI cliche, yet read as generated.

Detectors:
    myth_flip          "Most teams think X. Actually Y."
    antithesis_pair    "Everyone does X. No one does Y."   (quantifier inversion)
    reversal_pair      "That's not strategy. It's guessing."
    comma_upsell       "It's not just a note app, it's a second brain."
    rule_of_three      three consecutive punch fragments
    throat_clear       opener carrying no fact
    question_close     comment-bait question as the final line

Plus rhythm metrics: sentence-length coefficient of variation and max/min ratio.
"""

import re
import statistics

# ---------------------------------------------------------------------------
# Sentence segmentation
# ---------------------------------------------------------------------------
# A line break is a sentence boundary too: LinkedIn copy is written one thought
# per line and frequently drops terminal punctuation.
_SENT_SPLIT = re.compile(r"(?<=[.!?…])\s+|\n+")
_MD_NOISE = re.compile(r"^\s*(#{1,6}\s+|[-*>•]\s+|→\s*|\d+[.)]\s+)")
# Viktor's "ялинка" bullets are short, parallel and sorted by length ON PURPOSE.
# They must never be read as a rule-of-three triad.
_BULLET = re.compile(r"^\s*([-*>•]\s+|→|\d+[.)]\s+)")


def sentences(text: str) -> list[dict]:
    """Return [{text, line, words}] for every non-empty sentence."""
    out: list[dict] = []
    line_no = 1
    pos = 0
    for chunk in _SENT_SPLIT.split(text):
        if chunk is None:
            continue
        idx = text.find(chunk, pos)
        if idx >= 0:
            line_no = text[:idx].count("\n") + 1
            pos = idx + len(chunk)
        clean = _MD_NOISE.sub("", chunk).strip()
        if not clean:
            continue
        words = re.findall(r"\b[\w’'-]+\b", clean)
        if not words:
            continue
        out.append({
            "text": clean,
            "line": line_no,
            "words": words,
            "bullet": bool(_BULLET.match(chunk)),
        })
    return out


# ---------------------------------------------------------------------------
# Marker vocabularies
# ---------------------------------------------------------------------------
BELIEF = {
    "uk": r"(більшість|бíльшість|усі|всі|багато хто|прийнято|зазвичай|часто)\s+\S*\s*(думаю|думают|думають|вважаю|вважають|впевнен|переконан|каж|говор|чул)",
    "en": r"\b(most|everyone|people|many|conventional wisdom|teams?|founders?)\b[^.!?]{0,40}\b(think|thinks|believe|believes|assume|assumes|say|says|is told)\b",
}
# The correction may sit a couple of words in ("It's actually a habit."), so allow
# a short prefix rather than anchoring hard at the sentence start.
_LEAD = r"^\W*(?:[\w'’-]+\s+){0,2}"
CORRECTION = {
    "uk": _LEAD + r"(насправді|але насправді|правда в тому|правда проста|а от|а насправді|по факту|реальність)",
    "en": _LEAD + r"(actually|in reality|the truth is|in fact|really)",
}
UNIVERSAL = {
    "uk": r"\b(усі|всі|кожен|кожна|кожне|завжди|будь-хто|всім|усім)\b",
    "en": r"\b(everyone|everybody|every|all|always|anyone)\b",
}
NEGATIVE_Q = {
    "uk": r"\b(ніхто|жоден|жодна|жодне|ніколи|нікому|ніщо)\b",
    "en": r"\b(no one|nobody|none|never|not a single|nothing)\b",
}
NEGATION_OPEN = {
    "uk": r"^\W*(це не|то не|справа не в|проблема не в|питання не в)\b",
    "en": r"^\W*(that'?s not|this is'?nt|it'?s not|the problem is'?nt)\b",
}
AFFIRM_OPEN = {
    "uk": r"^\W*(це |то |просто )",
    "en": r"^\W*(it'?s|that'?s|this is|just )",
}
COMMA_UPSELL = {
    "uk": r"\bце не (просто|лише|тільки)\b[^.!?\n]{2,60},\s*(це|а)\b",
    "en": r"\bit'?s not (just|only|merely)\b[^.!?\n]{2,60},\s*it'?s\b",
}
GENERIC_OPENER = {
    "uk": r"^\W*(у сучасн|в сучасн|у сьогоденн|у світі|в світі|коли йдеться|у наш час|в наш час|сьогодні бізнес|усі ми знаємо|всі ми знаємо)",
    "en": r"^\W*(in today'?s|in the (fast|ever)-?\w*|when it comes to|in the world of|we all know|nowadays|in an era)",
}
FIRST_PERSON = {
    "uk": r"\b(я|мене|мені|мій|моя|моє|мої|ми|нас|нам|наш|наша|наше|наші)\b",
    "en": r"\b(i|me|my|mine|we|us|our|ours)\b",
}

PUNCH_MAX_WORDS = 5      # a "fragment" for rule-of-three purposes
SHORT_MAX_WORDS = 12     # both halves of a mirrored pair must be short


def _has(pat: str, s: str) -> bool:
    return bool(re.search(pat, s, re.IGNORECASE))


def _hit(cat: str, sents: list[dict], i: int, span: int = 1) -> dict:
    quote = " ".join(s["text"] for s in sents[i:i + span])
    return {
        "category": cat,
        "line": sents[i]["line"],
        "quote": quote if len(quote) <= 160 else quote[:157] + "...",
    }


# ---------------------------------------------------------------------------
# Detectors
# ---------------------------------------------------------------------------
def find_structural(text: str, lang: str) -> list[dict]:
    lang = "uk" if lang == "uk" else "en"
    sents = sentences(text)
    hits: list[dict] = []
    if not sents:
        return hits

    for i, s in enumerate(sents):
        cur, nxt = s["text"], sents[i + 1]["text"] if i + 1 < len(sents) else ""
        nxt_words = len(sents[i + 1]["words"]) if i + 1 < len(sents) else 0

        # 1. myth flip: stated belief, then the tidy correction
        if _has(BELIEF[lang], cur):
            if _has(CORRECTION[lang], nxt) or _has(CORRECTION[lang], cur):
                hits.append(_hit("myth_flip", sents, i, 2 if nxt else 1))

        # 2. antithesis pair: quantifier inversion across two short sentences
        if nxt and len(s["words"]) <= SHORT_MAX_WORDS and nxt_words <= SHORT_MAX_WORDS:
            fwd = _has(UNIVERSAL[lang], cur) and _has(NEGATIVE_Q[lang], nxt)
            rev = _has(NEGATIVE_Q[lang], cur) and _has(UNIVERSAL[lang], nxt)
            if fwd or rev:
                hits.append(_hit("antithesis_pair", sents, i, 2))

        # 3. reversal pair: negation, then a one-word swap dressed as insight
        if nxt and _has(NEGATION_OPEN[lang], cur) and _has(AFFIRM_OPEN[lang], nxt) and nxt_words <= 8:
            hits.append(_hit("reversal_pair", sents, i, 2))

        # 4. comma upsell: category inflation right after a comma
        if _has(COMMA_UPSELL[lang], cur):
            hits.append(_hit("comma_upsell", sents, i))

        # 5. rule of three: three consecutive punch fragments that MIRROR each other.
        # Shortness alone is not the tell; three short sentences in a row are
        # ordinary writing. The tell is three short sentences built the same way.
        if i + 2 < len(sents):
            trio = sents[i:i + 3]
            lens = [len(t["words"]) for t in trio]
            firsts = [t["words"][0].lower() for t in trio]
            # Anaphora is the strong signal. Equal length alone is only meaningful
            # for real punch fragments; at 4-5 words it is a coincidence.
            anaphora = max(firsts.count(f) for f in firsts) >= 2
            parallel = anaphora or (len(set(lens)) == 1 and max(lens) <= 3)
            if (
                not any(t["bullet"] for t in trio)
                and max(lens) <= PUNCH_MAX_WORDS
                and max(lens) - min(lens) <= 1
                and parallel
                and not any(t["text"].rstrip().endswith(("?", ":")) for t in trio)
            ):
                hits.append(_hit("rule_of_three", sents, i, 3))

    # 6. throat-clear opener: first sentence carries no fact
    first = sents[0]
    generic = _has(GENERIC_OPENER[lang], first["text"])
    has_digit = bool(re.search(r"\d", first["text"]))
    has_proper = bool(re.search(r"(?<!^)(?<![.!?]\s)\b[A-ZА-ЯЄІЇҐ][\w’'-]{2,}", first["text"]))
    has_person = _has(FIRST_PERSON[lang], first["text"])
    if generic or not (has_digit or has_proper or has_person):
        hits.append({
            "category": "throat_clear",
            "line": first["line"],
            "quote": first["text"][:157],
            "note": "generic opener" if generic else "opener has no number, no name, no first person",
        })

    # 7. comment-bait close
    last = sents[-1]
    if last["text"].rstrip().endswith("?"):
        hits.append({
            "category": "question_close",
            "line": last["line"],
            "quote": last["text"][:157],
            "note": "hard fail for posts and creatives; expected for outbound email",
        })

    # de-duplicate identical (category, line) pairs
    seen: set[tuple] = set()
    unique: list[dict] = []
    for h in hits:
        key = (h["category"], h["line"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(h)
    return unique


# ---------------------------------------------------------------------------
# Rhythm
# ---------------------------------------------------------------------------
def rhythm(text: str) -> dict:
    """
    A model writes every sentence about the same length. People don't.
    coefficient_of_variation = stdev / mean of sentence word counts.
    """
    lens = [len(s["words"]) for s in sentences(text)]
    if len(lens) < 2:
        return {"sentences": len(lens), "coefficient_of_variation": None, "flat": False}
    mean = statistics.fmean(lens)
    stdev = statistics.pstdev(lens)
    cv = stdev / mean if mean else 0.0
    n = len(lens)
    return {
        "sentences": n,
        "mean_words": round(mean, 1),
        "shortest": min(lens),
        "longest": max(lens),
        "max_min_ratio": round(max(lens) / max(min(lens), 1), 1),
        "coefficient_of_variation": round(cv, 3),
        # threshold calibrated on Viktor's published posts: below 0.35 reads flat
        "flat": n >= 5 and cv < 0.35,
    }
