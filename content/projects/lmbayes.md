---
title: "A Bayesian Lagrange-Multiplier Framework for Spatial Cross-Section, Panel, and Flow Models"
status: "Current"
venue: "Spatial Economic Analysis, forthcoming"
weight: 40
software: ["neighbayes"]
summary: "Bayesian counterparts of the Lagrange-multiplier tests that spatial econometrics uses to choose a specification."
image: "img/fig/lmbayes-columbus-posteriors.webp"
alt: "Eight histograms, one per Bayesian Lagrange-multiplier statistic on the Columbus crime data, each marked with the 5 percent chi-squared critical value as a dashed line and the posterior mean as a solid red line."
fit: figure
caption: "Posterior distributions of eight Bayesian LM statistics on the Columbus crime data. Each panel marks the 5% χ² critical value (dashed) and the posterior mean (solid); the spread of each posterior carries the uncertainty in the model's parameters into the test."
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
