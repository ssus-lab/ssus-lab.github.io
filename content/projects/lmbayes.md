---
title: "A Bayesian Lagrange-Multiplier Framework for Spatial Cross-Section, Panel, and Flow Models"
status: "Current"
venue: "Spatial Economic Analysis, forthcoming"
weight: 40
areas: ["methods"]
software: ["neighbayes"]
summary: "Bayesian counterparts of the Lagrange-multiplier tests that spatial econometrics uses to choose a specification."
image: "img/fig/lmbayes-columbus.webp"
image_dark: "img/fig/lmbayes-columbus-dark.webp"
alt: "Dot-and-interval chart, on a log scale, of six Bayesian Lagrange-multiplier statistics, each with its posterior mean, 95 percent posterior interval, and 5 percent chi-squared critical value. The robust LM-Error interval lies wholly below its critical value and the robust LM-Lag interval straddles it; the other four have posterior means above their critical values and intervals that reach below them."
caption: "The six Bayesian LM statistics for the OLS fit to the Columbus crime data: each one's posterior mean (dot) and 95% posterior interval (bar), against its 5% χ² critical value (tick), on a log scale. Each test carries the uncertainty in the model's parameters into its own posterior."
---

Lagrange-multiplier tests are the standard misspecification diagnostics of
spatial econometrics, but models fit by Markov chain Monte Carlo have had no
equivalent: analysts either refit a frequentist model at the posterior mean or
compare marginal likelihoods, which is expensive. The paper builds the Bayesian
counterpart. One template, a score evaluated on each posterior draw of the
restricted model, reproduces the classical diagnostics for cross-sectional
models and extends without structural change to the spatial Durbin family,
static spatial panels, and origin–destination flow models. Each statistic
carries a full posterior distribution, so the test reports its own uncertainty.

The tests ship in [neighbayes]({{< relref "/software/neighbayes" >}}).
