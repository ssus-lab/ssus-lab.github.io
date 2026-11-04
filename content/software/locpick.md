---
title: "locpick"
code: true
pypi: true
org: ssus
weight: 2
role: "Lead"
status: "Pre-release"
repo: "https://github.com/knaaptime/locpick"
summary: "Discrete choice models of location decisions: households, individuals, or firms choosing among places."
---

[locpick](https://github.com/knaaptime/locpick) models location and destination
choice, where individuals, households, or firms choose among spatially defined
alternatives such as neighborhoods, jobs, housing units, or transit stops. One
estimator composes the multinomial, nested, and mixed logit, and attaches space
to any of them in two ways: as correlation among nearby alternatives, the
spatially correlated logit, which keeps closed-form choice probabilities and
reduces to the multinomial logit when its spatial parameter is one; or as an
autoregressive structure in the systematic utility of the alternatives. Sampled
alternative sets are built for problems of 100,000 choosers and thousands of
alternatives. It is written in JAX.
