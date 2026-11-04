---
title: "augax"
code: true
pypi: true
org: ssus
weight: 2
role: "Lead"
repo: "https://github.com/knaaptime/augax"
docs: "https://knaaptime.com/augax/"
aliases: ["/software/pgjax/"]
summary: "Data-augmentation draws for JAX that make a model conditionally Gaussian, inside compiled, scanned, and parallel programs."
---

[augax](https://github.com/knaaptime/augax), formerly pgjax, draws the
auxiliary variables of conditionally Gaussian augmentation as XLA custom calls,
so a Gibbs sampler that needs them runs entirely inside compiled JAX code.
`pg_sample` draws Pólya-Gamma variates, for logit and negative binomial models;
`ks_sample` draws the Kolmogorov scale of the logistic distribution's normal
scale mixture, which makes a logistic latent variable conditionally Gaussian.
Both replace `jax.pure_callback` around a host-side sampler, which pays a round
trip between device and host on every sweep and serializes under `jax.pmap`.
The Pólya-Gamma draws are checked against the distribution's closed-form
moments in every sampling regime.
