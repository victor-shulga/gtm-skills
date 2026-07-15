#!/usr/bin/env python3
"""
detect.py — AI writing pattern detector for Ukrainian and English.

Usage:
    python3 detect.py path/to/text.txt --lang uk
    python3 detect.py path/to/text.txt --lang en
    echo "some text" | python3 detect.py --stdin --lang uk
    python3 detect.py path/to/text.txt --lang auto

Outputs JSON with:
    - language: detected/specified language
    - total_words: total word count
    - total_markers: total AI marker hits
    - ai_density: hits per 1000 words
    - markers_by_category: breakdown by pattern category
    - top_offenders: top 15 most frequent markers with counts and example lines
    - severity: "low" | "medium" | "high" based on density
"""

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# ----------------------------------------------------------------------------
# UKRAINIAN PATTERNS
# ----------------------------------------------------------------------------
PATTERNS_UK = {
    "inflated_significance": [
        r"\bключов(ий|ого|ою|ому|им|ій|их|ими) етап",
        r"\bзначущ(им|ий|ого) етап",
        r"\bсвідчить про",
        r"\bпідкреслює важливість",
        r"\bзнаменує собою",
        r"\bвідіграє ключову роль",
        r"\bвідіграє вирішальну роль",
        r"\bвідіграє найважливішу роль",
        r"\bу контексті глобальних",
        r"\bу контексті масштабних",
        r"\bзалишає незгладим",
        r"\bознаменував нову еру",
        r"\bє наріжним каменем",
        r"\bвносить неоціненн",
    ],
    "authority_signaling": [
        r"\bна думку експертів\b",
        r"\bпровідні видання відзначають",
        r"\bвизнаний авторитет",
        r"\bактивна присутність у медіапросторі",
        r"\bшироко висвітлюється",
    ],
    "shallow_participles": [
        r"\bпідкреслюючи\b",
        r"\bдемонструючи\b",
        r"\bсвідчачи\b",
        r"\bсприяючи\b",
        r"\bзабезпечуючи\b",
        r"\bвідображаючи\b",
        r"\bсимволізуючи\b",
        r"\bвтілюючи\b",
        r"\bформуючи\b",
        r"\bакцентуючи\b",
    ],
    "promo_language": [
        r"\bможе похвалитися\b",
        r"\bяскрав(ий|а|е|ого|ою|ому|им|ій|их|ими)\b",
        r"\bсамобутн(ій|я|є|ього|ьою|ьому|іми)\b",
        r"\bбагат(е|а|ий) (надбання|спадщина|історія|культурна спадщина)",
        r"\bу самому серці",
        r"\bмальовнич(ий|а|е|ого|ою|ому|им|ій|их|ими)",
        r"\bнеперевершен",
        r"\bне може не вражати",
        r"\bрозкриває потенціал",
        r"\bзахоплив(а|ий|е) красою",
    ],
    "vague_references": [
        r"\bза даними галузевих",
        r"\bспостерігачі відзначають",
        r"\bексперти вважають",
        r"\bнизка фахівців",
        r"\bдеякі критики стверджують",
        r"\bзгідно з різними джерелами",
        r"\bза наявними даними",
    ],
    "challenges_template": [
        r"\bпопри.{1,40}стикається з рядом виклик",
        r"\bтим не менше продовжує (розвиватися|розвиватись)",
        r"\bперспективи (й|та|і) виклики",
        r"\bпопри всі труднощі",
    ],
    "ai_vocabulary": [
        r"\bкрім того\b",
        r"\bу контексті\b",
        r"\bключов(ий|им|ого|ою|ому|ій|их|ими|і|у|а|е)\b",
        r"\bпоглибит(ися|ись|ьмося)\b",
        r"\bнепереб(утн|орн)",
        r"\bпосилюва(ти|ння|ючи)",
        r"\bпривертати увагу",
        r"\bвзаємодія\b",
        r"\bнюанс(и|ів|ами)\b",
        r"\bтонкощ(і|ів|ами)\b",
        r"\bландшафт\b",
        r"\bзнаков(ий|а|е|ого|ою|ому|им|ій|их|ими)",
        r"\bпалітра\b",
        r"\bсвідченн(я|ям|і)\b",
        r"\bакцентувати\b",
        r"\bразом з тим\b",
        r"\bводночас\b",
        r"\bтаким чином\b",
        r"\bварто зазначити\b",
        r"\bважливо підкреслити\b",
        r"\bнеобхідно зазначити\b",
        r"\bне можна не згадати\b",
    ],
    "avoiding_is": [
        r"\bслугує\b",
        r"\bвиступає в (ролі|якості)",
        r"\bявляє собою",
        r"\bуособлює\b",
        r"\bвтілює в собі",
    ],
    "negative_parallelism": [
        r"\bне просто .{1,40}, а\b",
        r"\bне лише .{1,40}, але й\b",
        r"\bсправа не в .{1,40}, справа в\b",
    ],
    "em_dash_overuse": [
        # Detected separately as ratio
    ],
    "bold_overuse": [
        # Detected separately as ratio
    ],
    "emoji_in_headings": [
        # Detected separately
    ],
    "wrong_quotes": [
        # Detected separately
    ],
    "chatbot_artifacts": [
        r"\bсподіваюся, це допоможе\b",
        r"\bсподіваюся, це буде корисно\b",
        r"\bдайте знати, якщо\b",
        r"\bось огляд\b",
        r"\bякщо хочете, я можу\b",
        r"^Звичайно!",
        r"^Безумовно!",
    ],
    "knowledge_disclaimers": [
        r"\bстаном на \[",
        r"\bнаскільки мені відомо\b",
        r"\bна основі наявної інформації\b",
        r"\bдоступні джерела не містять",
    ],
    "sycophantic": [
        r"^Чудове запитання",
        r"\bВи абсолютно праві\b",
        r"\bпрекрасне зауваження\b",
    ],
    "filler_phrases": [
        r"\bдля того щоб\b",
        r"\bу звʼязку з тим, що\b",
        r"\bу зв'язку з тим, що\b",
        r"\bу теперішній момент часу\b",
        r"\bу випадку якщо\b",
        r"\bмає здатність\b",
        r"\bважливо зазначити той факт\b",
        r"\bданий\b",
        r"\bздійснюва(ти|ння|в|ла|ли)",
        r"\bу рамках\b",
    ],
    "excessive_hedging": [
        r"\bможна припустити, що, можливо",
        r"\bпотенційно міг(ла|ли) б",
        r"\bпевний вплив\b",
    ],
    "bureaucratese": [
        r"\bна даний момент\b",
        r"\bвищезазначен",
        r"\bнижчевикладен",
        r"\bу цілях\b",
        r"\bна підставі\b",
        r"\bвідповідно до\b",
        r"\bналежн(е|ого|ій|их)",
        r"\bмає місце бути",
    ],
    "prefatory_excess": [
        r"\bваjto зазначити, що\b",
        r"\bнеобхідно підкреслити, що\b",
        r"\bважливо враховувати той факт",
        r"\bне можна не звернути увагу",
        r"\bне менш важливим є\b",
    ],
    "abstract_world": [
        r"\bу світі (сучасних|бізнес|техно|цифров)",
        r"\bу сфері\b",
        r"\bу площині\b",
    ],
}

# ----------------------------------------------------------------------------
# ENGLISH PATTERNS
# ----------------------------------------------------------------------------
PATTERNS_EN = {
    "inflated_significance": [
        r"\bstands as a testament\b",
        r"\bmarks? a pivotal\b",
        r"\bwatershed moment\b",
        r"\bparadigm[- ]shifting\b",
        r"\btransformational\b",
        r"\bindispensable role\b",
        r"\bcornerstone of\b",
        r"\bhallmark of\b",
        r"\bushers? in a new era\b",
        r"\breshapes? the landscape\b",
        r"\bredefines? the boundaries\b",
        r"\bleaves? an indelible mark\b",
        r"\bplays? a (crucial|pivotal|essential|key) role\b",
        r"\bin the broader context of\b",
    ],
    "authority_signaling": [
        r"\bwidely regarded\b",
        r"\bleading experts agree\b",
        r"\bprominent figures have noted\b",
        r"\bgarnered widespread acclaim\b",
        r"\brecognized authority\b",
    ],
    "shallow_participles": [
        r"\bunderscoring\b",
        r"\bhighlighting\b",
        r"\bshowcasing\b",
        r"\bdemonstrating\b",
        r"\breflecting\b",
        r"\bembodying\b",
        r"\bsymbolizing\b",
        r"\bshaping\b",
        r"\bcontributing to\b",
        r"\bserving as a reminder\b",
    ],
    "promo_language": [
        r"\bboasts?\b",
        r"\bvibrant\b",
        r"\bbustling\b",
        r"\bpicturesque\b",
        r"\bbreathtaking\b",
        r"\bstunning\b",
        r"\brich heritage\b",
        r"\bone[- ]of[- ]a[- ]kind\b",
        r"\bin the heart of\b",
        r"\bunparalleled\b",
        r"\bleaves? a lasting impression\b",
        r"\bunlocks?(?: the)? potential\b",
        r"\bgame[- ]changer\b",
        r"\bcutting[- ]edge\b",
        r"\bstate[- ]of[- ]the[- ]art\b",
        r"\bworld[- ]class\b",
    ],
    "vague_references": [
        r"\baccording to industry reports\b",
        r"\bobservers note\b",
        r"\bexperts believe\b",
        r"\bsome critics argue\b",
        r"\bvarious sources suggest\b",
        r"\bavailable data indicates?\b",
        r"\bstudies have shown\b",
    ],
    "challenges_template": [
        r"\bdespite (facing )?numerous challenges\b",
        r"\bnonetheless continues to thrive\b",
        r"\bchallenges and opportunities\b",
        r"\bin the face of adversity\b",
    ],
    "ai_vocabulary": [
        r"\bdelve\b",
        r"\bdive deep(er)?\b",
        r"\bnavigate\b",
        r"\btapestry\b",
        r"\bintricate\b",
        r"\bmultifaceted\b",
        r"\brobust\b",
        r"\bleverage\b",
        r"\bharness\b",
        r"\bfoster\b",
        r"\bunderscore\b",
        r"\belucidate\b",
        r"\bencompass\b",
        r"\bintersection of\b",
        r"\brealm\b",
        r"\blandscape\b",
        r"\bpivotal\b",
        r"\bparamount\b",
        r"\bprofound\b",
        r"\bseamless(ly)?\b",
        r"\bcomprehensive\b",
        r"\bholistic\b",
        r"\bnuanced\b",
        r"\bresonate\b",
        r"\b(in line|align) with\b",
        r"\bmoreover\b",
        r"\bfurthermore\b",
    ],
    "avoiding_is": [
        r"\bserves as\b",
        r"\bstands as\b",
        r"\brepresents\b",
        r"\bembodies\b",
        r"\bexemplifies\b",
        r"\bconstitutes\b",
    ],
    "negative_parallelism": [
        r"\bit'?s? not just .{1,40}, it'?s\b",
        r"\bthis isn'?t only .{1,40}, but\b",
        r"\bit'?s? not about .{1,40}, it'?s about\b",
    ],
    "chatbot_artifacts": [
        r"\bI hope this helps\b",
        r"\bI'?d be happy to\b",
        r"\bfeel free to ask\b",
        r"\blet me know if you'?d like\b",
        r"\bhere'?s an? overview\b",
        r"^Certainly!",
        r"^Absolutely!",
        r"^Of course!",
    ],
    "knowledge_disclaimers": [
        r"\bas of my knowledge cutoff\b",
        r"\bto the best of my knowledge\b",
        r"\bspecific data is limited\b",
        r"\bbased on available information\b",
        r"\bthe available sources do not contain\b",
    ],
    "sycophantic": [
        r"^Great question",
        r"\byou'?re absolutely right\b",
        r"\bexcellent point\b",
        r"\bgreat point\b",
    ],
    "filler_phrases": [
        r"\bin order to\b",
        r"\bdue to the fact that\b",
        r"\bat the present moment in time\b",
        r"\bin the event that\b",
        r"\bhas the ability to\b",
        r"\bit is important to note the fact\b",
        r"\butili[sz]e\b",
        r"\bin terms of\b",
    ],
    "excessive_hedging": [
        r"\bcould potentially\b",
        r"\bmight possibly\b",
        r"\bsome degree of influence\b",
        r"\bit could be suggested\b",
    ],
    "bureaucratese": [
        r"\boperationalize\b",
        r"\bsynergize\b",
        r"\bfacilitat(e|ing|ion)\b",
        r"\bwith respect to\b",
        r"\bin regard to\b",
        r"\bpursuant to\b",
        r"\bhereinafter\b",
        r"\baforementioned\b",
        r"\bgoing forward\b",
    ],
    "prefatory_excess": [
        r"\bit'?s worth noting that\b",
        r"\bit is important to emphasize\b",
        r"\bone cannot overlook\b",
        r"\bit should be mentioned that\b",
        r"\bequally important is\b",
        r"\bit bears repeating\b",
    ],
    "abstract_world": [
        r"\bin the world of\b",
        r"\bin the realm of\b",
        r"\bin the landscape of\b",
        r"\bin the space of\b",
        r"\bin the arena of\b",
    ],
}


# ----------------------------------------------------------------------------
# DETECTION LOGIC
# ----------------------------------------------------------------------------
def detect_language(text: str) -> str:
    """Heuristic: count Cyrillic vs Latin characters."""
    cyr = len(re.findall(r"[Ѐ-ӿ]", text))
    lat = len(re.findall(r"[A-Za-z]", text))
    if cyr > lat:
        return "uk"
    return "en"


def count_em_dashes(text: str, total_words: int) -> tuple[int, float]:
    """em-dashes per 1000 words."""
    count = len(re.findall(r"[—–](?!\d)", text))
    rate = (count / max(total_words, 1)) * 1000
    return count, rate


def count_bold(text: str) -> int:
    """**bold** occurrences in markdown."""
    return len(re.findall(r"\*\*[^*]+\*\*", text))


def count_emoji_in_headings(text: str) -> int:
    """Emoji at start of markdown headings, list items, or any line with bold lead-in."""
    emoji_re = re.compile(
        r"^(?:#{1,6}\s+|\s*[-*]\s+|\s*)[\U0001F300-\U0001FAFF\U00002600-\U000027BF]",
        re.MULTILINE,
    )
    return len(emoji_re.findall(text))


def count_wrong_quotes(text: str, lang: str) -> int:
    """For Ukrainian: straight quotes used instead of «...»."""
    if lang == "uk":
        # straight " quotes around words (heuristic)
        return len(re.findall(r'"[^"]{2,}"', text))
    # For English: mixed straight/curly within doc
    has_straight = bool(re.search(r'"[^"]{2,}"', text))
    has_curly = bool(re.search(r"[“”]", text))
    return 1 if (has_straight and has_curly) else 0


def count_title_case_headings(text: str) -> int:
    """Headings where every major word is capitalized."""
    headings = re.findall(r"^#{1,6}\s+(.+)$", text, re.MULTILINE)
    title_case = 0
    for h in headings:
        words = [w for w in h.split() if w and len(w) > 2]
        if not words:
            continue
        # All words start with uppercase letter
        if all(w[0].isupper() for w in words) and len(words) >= 3:
            title_case += 1
    return title_case


def find_matches(text: str, patterns: dict[str, list[str]]) -> dict[str, list[tuple[str, int, str]]]:
    """
    Return per-category list of (matched_string, line_number, line_excerpt).
    """
    results: dict[str, list[tuple[str, int, str]]] = defaultdict(list)
    lines = text.splitlines()
    for category, patterns_list in patterns.items():
        for pat in patterns_list:
            for m in re.finditer(pat, text, re.IGNORECASE | re.MULTILINE):
                # Find line number
                line_no = text[: m.start()].count("\n") + 1
                line_excerpt = lines[line_no - 1].strip() if 0 < line_no <= len(lines) else ""
                if len(line_excerpt) > 120:
                    line_excerpt = line_excerpt[:117] + "..."
                results[category].append((m.group(0), line_no, line_excerpt))
    return results


def severity_label(density: float) -> str:
    if density < 5:
        return "low"
    if density < 15:
        return "medium"
    return "high"


def analyze(text: str, lang: str) -> dict:
    if lang == "auto":
        lang = detect_language(text)

    patterns = PATTERNS_UK if lang == "uk" else PATTERNS_EN

    total_words = len(re.findall(r"\b\w+\b", text))
    matches = find_matches(text, patterns)

    # Style metrics computed separately
    em_dashes, em_dash_rate = count_em_dashes(text, total_words)
    bold_count = count_bold(text)
    emoji_count = count_emoji_in_headings(text)
    wrong_quotes = count_wrong_quotes(text, lang)
    title_case = count_title_case_headings(text)

    # Aggregate counts
    markers_by_category = {cat: len(hits) for cat, hits in matches.items() if hits}

    # Style additions
    if em_dash_rate > 5:
        markers_by_category["em_dash_overuse"] = em_dashes
    if bold_count > 5:
        markers_by_category["bold_overuse"] = bold_count
    if emoji_count > 0:
        markers_by_category["emoji_in_headings"] = emoji_count
    if wrong_quotes > 0:
        markers_by_category["wrong_quotes"] = wrong_quotes
    if title_case > 0:
        markers_by_category["title_case_headings"] = title_case

    total_markers = sum(markers_by_category.values())
    ai_density = (total_markers / max(total_words, 1)) * 1000

    # Top offenders by raw match string
    counter: Counter = Counter()
    examples: dict[str, tuple[int, str]] = {}
    for cat, hits in matches.items():
        for matched, line_no, excerpt in hits:
            key = matched.lower()
            counter[key] += 1
            if key not in examples:
                examples[key] = (line_no, excerpt)

    top_offenders = []
    for marker, count in counter.most_common(15):
        line_no, excerpt = examples[marker]
        top_offenders.append({
            "marker": marker,
            "count": count,
            "first_line": line_no,
            "example": excerpt,
        })

    return {
        "language": lang,
        "total_words": total_words,
        "total_markers": total_markers,
        "ai_density_per_1000_words": round(ai_density, 2),
        "severity": severity_label(ai_density),
        "markers_by_category": dict(sorted(markers_by_category.items(), key=lambda x: -x[1])),
        "style_metrics": {
            "em_dashes": em_dashes,
            "em_dash_rate_per_1000_words": round(em_dash_rate, 2),
            "bold_count": bold_count,
            "emoji_in_headings_or_lists": emoji_count,
            "wrong_or_mixed_quotes": wrong_quotes,
            "title_case_headings": title_case,
        },
        "top_offenders": top_offenders,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Detect AI writing patterns in UK/EN text.")
    parser.add_argument("path", nargs="?", help="Path to text file.")
    parser.add_argument("--stdin", action="store_true", help="Read text from stdin.")
    parser.add_argument(
        "--lang",
        choices=["uk", "en", "auto"],
        default="auto",
        help="Language: uk, en, or auto-detect (default).",
    )
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON.")
    args = parser.parse_args()

    if args.stdin:
        text = sys.stdin.read()
    elif args.path:
        text = Path(args.path).read_text(encoding="utf-8")
    else:
        parser.error("Provide a path or --stdin.")

    result = analyze(text, args.lang)
    indent = 2 if args.pretty else None
    print(json.dumps(result, ensure_ascii=False, indent=indent))
    return 0


if __name__ == "__main__":
    sys.exit(main())
