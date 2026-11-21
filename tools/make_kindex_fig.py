"""kindex's fig-la (LA components) for the lab site: two panels for the project page, one map for its card.

Usage: python tools/make_kindex_fig.py ~/Dropbox/projects/kindex/paper/figures/la_components.png static/img/fig/kindex-la-components.webp [static/img/fig/kindex-la-card.webp]

The page figure joins the panels at the 25th percentile and at K's peak, headers
through bar labels. The card, which is too small for either panel's text, takes
the peak's map alone.
"""
import sys
from PIL import Image

src, dst, *card = sys.argv[1:]
im = Image.open(src).convert("RGB")
TOP, BOTTOM = 0, 1395                      # panel headers through the bar labels; legend dropped
p1 = im.crop((0, TOP, 1115, BOTTOM))       # cut at $40,000, the 25th percentile
p3 = im.crop((2427, TOP, 3541, BOTTOM))    # cut at $150,000, the 76th percentile, where K peaks
gap = 98                                   # ink-to-ink spacing 134 px, as in the paper
out = Image.new("RGB", (p1.width + gap + p3.width, BOTTOM - TOP), "white")
out.paste(p1, (0, 0))
out.paste(p3, (p1.width + gap, 0))
w = 1600
out = out.resize((w, round(out.height * w / out.width)), Image.LANCZOS)
out.save(dst, "WEBP", quality=88, method=6)
print(dst, out.size)

if card:
    m = im.crop((2427, 120, 3541, 1243))   # the peak's map, below its header and above its bar
    m = m.resize((800, round(m.height * 800 / m.width)), Image.LANCZOS)
    m.save(card[0], "WEBP", quality=88, method=6)
    print(card[0], m.size)
