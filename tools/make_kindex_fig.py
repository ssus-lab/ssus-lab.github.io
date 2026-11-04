"""Two panels of kindex's fig-la (LA components at the 25th percentile and at K's peak) for the lab site.

Usage: python tools/make_kindex_fig.py ~/Dropbox/projects/kindex/paper/figures/la_components.png static/img/fig/kindex-la-components.webp
"""
import sys
from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
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
