# Brand extraction — separating real brand colors from noise

## The recipe
```bash
cd /tmp && curl -sL "<URL>" -o site.html
wc -c site.html
# colors
grep -oiE '#[0-9a-f]{6}|#[0-9a-f]{3}\b' site.html | tr 'A-Z' 'a-z' | sort | uniq -c | sort -rn | head -25
grep -oiE 'rgba?\([0-9, .]+\)' site.html | sort | uniq -c | sort -rn | head -12
# fonts (Google Fonts query param is the most reliable signal)
grep -oiE 'family=[A-Za-z+]+' site.html | sort -u
grep -oiE 'font-family:[^;{}"]+' site.html | sort | uniq -c | sort -rn | head
# external stylesheets — fetch & re-grep if inline colors are sparse
grep -oiE '<link[^>]+stylesheet[^>]*>' site.html | grep -oiE 'href="[^"]+"' | head
```
If the homepage is a builder (WordPress/Elementor/Webflow), brand colors often live in an
external CSS file. Resolve the top stylesheet href (relative → absolute), `curl` it, and
re-run the color grep on it.

## WordPress / Gutenberg default-palette NOISE (discard these)
These appear on almost every WP site regardless of brand. If a hex is in this list AND
low-frequency, drop it:
```
#0693e3  #00d084  #7bdcb5  #8ed1fc  #0693e3  #9b51e0  #ab1dfe  #fcb900  #ff6900
#cf2e2e  #f78da7  #abb8c3  #eee  #ddd  #313131  #32373c  #7a00df  #dad0ec
#fafae1  #faaca8  #fdd79a  #ffc526
```
Also generic: pure `#ffffff/#fff`, `#000000/#000`, `#f5f5f5`, `#e3e3e3`, `#cccccc`,
`#626262` — keep at most one near-white (paper) and one near-black (ink) as neutrals.

## Classify what's left (frequency-ranked custom hexes)
- **Hero accent** = the most-frequent SATURATED color (high chroma). Usually 1, sometimes a
  warm secondary too. (e.g. a single corporate blue; or a green hero + a warm orange.)
- **Ink / base** = the dominant very-dark color (often near-black, sometimes hue-tinted).
  (e.g. a charcoal `#1C1C1C`; or a near-black green `#02150B`.)
- **Tints** = light versions of the accent (e.g. a mint tint of a green hero).
- **Neutrals** = greys for paper/lines.

Quick saturation gut-check: convert hex→HSL mentally; S>40% & L 30–70% = accent candidate;
L<15% = ink; S<12% = neutral.

## Worked examples (anonymised)
- **Engineering/construction site:** #1C1C1C ×21 (ink, base) + #0054A2 (blue accent) were real;
  every #0693e3/#00d084/#9b51e0/#ff6900 was WP noise. → charcoal + engineering blue.
- **Dev/software site:** #12CF71 ×73 (green hero) + #FFA033 ×80 (orange) + #B2FFD9
  ×50 (mint tint) + #FF4726 ×22 (coral) + #02150B (ink) were real; the rest WP defaults.
  → green-forward, dev character.
