---
title: "neighbayes"
code: true
pypi: true
org: ssus
weight: 1
role: "Lead"
status: "Pre-release"
repo: "https://github.com/knaaptime/neighbayes"
docs: "https://knaaptime.com/neighbayes/dev/"
summary: "Bayesian estimation of spatial econometric models in Python: cross-sections, discrete outcomes, panels, and flows."
---

[neighbayes](https://github.com/knaaptime/neighbayes) fits spatial econometric
models by Bayesian estimation, some fifty model classes behind one formula
interface: the cross-sectional family (SAR, SEM, SDM, SDEM, and SLX); spatial
logit, probit, tobit, negative binomial, and zero-inflated models; fixed-,
random-, and dynamic-effects panels; and origin–destination flows. Fitted models
report direct, indirect, and total effects with their posterior intervals, and
carry the [Bayesian Lagrange-multiplier diagnostics]({{< relref "/projects/lmbayes" >}}).
The [log-determinant methods]({{< relref "/projects/logdet" >}}) keep the
Jacobian cheap enough for a model of every U.S. census tract. It builds on PyMC,
and an optional JAX backend runs its Gibbs samplers on the sparse solvers of
[sparsax]({{< relref "/software/sparsax" >}}) and the augmentation draws of
[augax]({{< relref "/software/augax" >}}).
