"""Project figures for the lab site, in the SSUS figure style, light and dark.

Each figure is one panel at the cards' 16:10, drawn from the raw results its
paper's repository keeps, so it can be redrawn when they change:

    python tools/make_figs.py rentpanel ~/Dropbox/projects/rentpanel
    python tools/make_figs.py logdet    ~/Dropbox/projects/logdet
    python tools/make_figs.py lmbayes   ~/Dropbox/projects/lmbayes
    python tools/make_figs.py texas

texas downloads 2017-2021 ACS tracts through geosnap and TIGER 2021 places on
its first run, into tools/.cache/, so run it where geosnap imports (the geosnap
env). Writes static/img/fig/<name>.webp and <name>-dark.webp. The style comes
from ssus-lab-brand/matplotlib; set SSUS_BRAND if the brand folder is elsewhere.
"""
import io
import os
import sys
from pathlib import Path

import matplotlib
import matplotlib.ticker
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

BRAND = Path(os.environ.get("SSUS_BRAND", "~/Dropbox/projects/ssus-lab-brand")).expanduser()
sys.path.insert(0, str(BRAND / "matplotlib"))
import ssus_style  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "static" / "img" / "fig"
SIZE = (6.4, 4.0)   # inches, 16:10 like the cards; saved 1600 px wide
WIDTH = 1600
# Lines the figure does not foreground: Graticule on white, Slate on night.
MUTED = {"light": ssus_style.BRAND["graticule"], "dark": ssus_style.BRAND["slate"]}
INK = {"light": ssus_style.BRAND["survey-ink"], "dark": "#E6EBEA"}  # the styles' text colors


def save(fig, name, mode):
    """Save at 1600 px wide as WebP, the site's figure format."""
    buf = io.BytesIO()
    with plt.rc_context({"savefig.bbox": "standard"}):  # the styles crop tight; keep 16:10
        fig.savefig(buf, format="png", dpi=WIDTH / fig.get_figwidth())
    plt.close(fig)
    im = Image.open(buf).convert("RGB")
    path = OUT / f"{name}{'-dark' if mode == 'dark' else ''}.webp"
    im.save(path, "WEBP", quality=88, method=6)
    print(path, im.size)


def rentpanel(src, mode):
    """The treatment effect each design recovers as heterogeneity grows spatial (true rho 0.5)."""
    d = pd.read_csv(Path(src) / "data" / "simulation_results.csv")
    g = (d[d.rho_y == 0.5].groupby("rho_mu")
         .agg(fe=("delta_fe", "mean"), fe_sd=("delta_fe", "std"),
              did=("delta_did", "mean"), did_sd=("delta_did", "std")).reset_index())
    print(g.round(3).to_string(index=False))
    s = ssus_style.SERIES[mode]
    fig, ax = plt.subplots(figsize=SIZE, layout="constrained")
    ax.axhline(10, color=MUTED[mode], lw=1, ls=(0, (3, 3)), zorder=1)
    for col, sd, c, dx in (("fe", "fe_sd", s[0], -0.006), ("did", "did_sd", s[1], 0.006)):
        ax.errorbar(g.rho_mu + dx, g[col], yerr=g[sd], color=c, lw=2, marker="o",
                    ms=6, elinewidth=1.2, capsize=0, zorder=3)
    last = g.iloc[-1]
    ax.annotate("Within-unit (fixed effects)", (last.rho_mu, last.fe), xytext=(0, 14),
                textcoords="offset points", ha="right", color=s[0], fontweight=600)
    ax.annotate("Between-group (difference-in-differences)", (last.rho_mu, last.did),
                xytext=(0, -22), textcoords="offset points", ha="right", color=s[1], fontweight=600)
    ax.set_xlim(-0.04, 0.84)
    ax.set_ylim(0, 12.5)
    ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8])
    ax.set_xlabel("Spatial structure of unit heterogeneity, $\\rho_\\mu$")
    ax.set_ylabel("Estimated treatment effect")
    save(fig, "rentpanel-effect", mode)


def logdet(src, mode):
    """Bias in the posterior mean of rho by true rho, all U.S. tracts (queen): the paper's positive panel."""
    res = Path(src) / "replication" / "results"
    sources = (("bias_map.csv", lambda m: m not in ("barry_pace", "sa_m30_trunc")),
               ("bias_map_positive.csv", lambda m: m == "barry_pace"),
               ("bias_map_negative.csv", lambda m: m != "sa_m30_trunc"))
    rows = []
    for fname, keep in sources:
        d = pd.read_csv(res / fname)
        rows.append(d[(d.family == "queen_tracts") & d.method.map(keep)])
    d = pd.concat(rows)
    s = ssus_style.SERIES[mode]
    # Factorize-and-interpolate is drawn wide beneath stochastic Chebyshev: both lie on zero.
    look = {"aaa": ("Factorize and interpolate", s[0], 4.0),
            "stoch_cheb": ("Stochastic Chebyshev", s[2], 1.6),
            "barry_pace": ("Barry–Pace", s[1], 2.2)}
    others = ("lesage_pace", "sa_m30", "grid_spline")
    fig, ax = plt.subplots(figsize=SIZE, layout="constrained")
    ax.axhline(0, color=MUTED[mode], lw=0.8, zorder=1)
    for m in (*others, "aaa", "stoch_cheb", "barry_pace"):
        label, c, lw = look.get(m, ("Pace–LeSage, Smirnov–Anselin, grid and spline", MUTED[mode], 1.4))
        st = (d[(d.method == m) & (d.rho_true > 0)].groupby("rho_true").bias_in_sd
              .agg(["mean", "min", "max", "size"]).reset_index())
        ax.plot(st.rho_true, st["mean"], color=c, lw=lw, zorder=3 if m in look else 2,
                label=label if m in ("aaa", "stoch_cheb", "barry_pace", "sa_m30") else None)
        if st["size"].max() > 1:
            ax.fill_between(st.rho_true, st["min"], st["max"], color=c, alpha=0.18, lw=0, zorder=2)
        print(m, st.set_index("rho_true")["mean"].loc[[0.85, 0.9, 0.95]].round(2).tolist())
    h, l = ax.get_legend_handles_labels()
    order = [l.index(x) for x in ("Factorize and interpolate", "Stochastic Chebyshev", "Barry–Pace",
                                  "Pace–LeSage, Smirnov–Anselin, grid and spline")]
    ax.legend([h[i] for i in order], [l[i] for i in order], loc="upper left")
    ax.set_xlim(0.28, 0.97)
    ax.set_xlabel("True $\\rho$")
    ax.set_ylabel("Bias in posterior mean of $\\rho$\n(posterior standard deviations)")
    save(fig, "logdet-bias", mode)


def lmbayes(src, mode):
    """The OLS-launch Bayesian LM statistics on Columbus: posterior mean, 95% interval, 5% critical value."""
    from scipy.stats import chi2
    d = pd.read_csv(Path(src) / "paper" / "tables" / "columbus_lm_diagnostics.csv")
    d = d[d.launch_null == "OLS"].iloc[::-1].reset_index(drop=True)
    print(d[["test", "statistic", "ci_lower", "ci_upper", "df"]].round(3).to_string(index=False))
    names = {"LM-Lag": "LM-Lag", "LM-Error": "LM-Error", "LM-SDM-Joint": "LM-SDM, joint",
             "LM-SLX-Error-Joint": "LM-SLX-Error, joint", "Robust-LM-Lag": "Robust LM-Lag",
             "Robust-LM-Error": "Robust LM-Error"}
    s = ssus_style.SERIES[mode]
    fig, ax = plt.subplots(figsize=SIZE, layout="constrained")
    y = np.arange(len(d))
    ax.hlines(y, d.ci_lower, d.ci_upper, color=s[0], lw=3, alpha=0.45 if mode == "light" else 0.6,
              label="95% posterior interval")
    ax.plot(d.statistic, y, "o", color=s[0], ms=8, label="Posterior mean")
    crit = chi2.ppf(0.95, d.df)
    ax.plot(crit, y, "|", color=INK[mode], ms=20, mew=2, label="5% critical value, $\\chi^2$")
    ax.set_xscale("log")
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}"))
    ax.set_yticks(y, [names[t] for t in d.test])
    ax.tick_params(axis="y", labelcolor=INK[mode], labelsize=9)
    ax.grid(axis="x", which="major")
    ax.grid(axis="y", visible=False)
    ax.set_ylim(-0.6, len(d) - 0.4)
    ax.set_xlabel("Bayesian LM statistic (log scale)")
    fig.legend(loc="outside upper center", ncol=3, markerscale=0.6)
    save(fig, "lmbayes-columbus", mode)


METROS = (("Dallas–Fort Worth", "19100", "4819000"), ("Houston", "26420", "4835000"))


def texas_data():
    """Tracts (ACS 2017-2021) for both metros and the two principal cities, cached."""
    import geopandas as gpd
    cache = Path(__file__).resolve().parent / ".cache"
    cache.mkdir(exist_ok=True)
    tracts = []
    for _, msa, _ in METROS:
        f = cache / f"acs2021_tracts_{msa}.parquet"
        if not f.exists():
            from geosnap import DataStore, io as gio
            g = gio.get_acs(DataStore(), msa_fips=msa, years=[2021], level="tract")
            g[["geoid", "n_total_pop", "n_nonhisp_black_persons", "geometry"]].to_parquet(f)
        tracts.append(gpd.read_parquet(f))
    f = cache / "tiger2021_places_48.parquet"
    if not f.exists():
        p = gpd.read_file("https://www2.census.gov/geo/tiger/TIGER2021/PLACE/tl_2021_48_place.zip")
        p[p.GEOID.isin([m[2] for m in METROS])].to_parquet(f)
    return tracts, gpd.read_parquet(f)


def texas(mode):
    """Black share by tract in each metro, its principal city outlined in the accent."""
    tracts, places = texas_data()
    fig, axes = plt.subplots(1, 2, figsize=SIZE, layout="constrained")
    cmap = "ssus_seq" if mode == "light" else "ssus_seq_dark"
    for ax, g, (name, _, city) in zip(axes, tracts, METROS):
        g = g[g.n_total_pop > 0].to_crs(g.estimate_utm_crs())   # water tracts have no residents
        g["share"] = g.n_nonhisp_black_persons / g.n_total_pop
        c = places[places.GEOID == city].to_crs(g.crs)
        inside = g.representative_point().within(c.geometry.iloc[0])
        pshare = g.loc[inside, "n_total_pop"].sum() / g.n_total_pop.sum()
        g.plot("share", ax=ax, cmap=cmap, vmin=0, vmax=0.8, lw=0)
        c.boundary.plot(ax=ax, color=ssus_style.flag(mode), lw=1.1)
        ax.set_aspect("equal", adjustable="datalim")   # same box for both, so the titles align
        city_name = c.NAME.iloc[0]
        ax.set_title(f"{name}: city of {city_name} holds {pshare:.0%}", loc="left")
        ax.set_axis_off()
        print(name, f"city share {pshare:.3f}", len(g), "tracts")
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(0, 0.8))
    cb = fig.colorbar(sm, ax=axes, orientation="horizontal", shrink=0.45, aspect=30, pad=0.02)
    cb.set_label("Share of residents who are non-Hispanic Black")
    cb.ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1, decimals=0))
    cb.outline.set_visible(False)
    save(fig, "texas-cities", mode)


def main():
    name, *args = sys.argv[1:]
    for mode in ("light", "dark"):
        ssus_style.use(mode)
        globals()[name](*args, mode=mode)


if __name__ == "__main__":
    main()
