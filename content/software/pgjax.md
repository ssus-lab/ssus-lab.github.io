---
title: "pgjax"
code: true
pypi: true
org: ssus
weight: 2
role: "Lead"
repo: "https://github.com/knaaptime/pgjax"
summary: "Pólya-Gamma sampling on device for JAX, inside compiled, scanned, and parallel programs."
---

[pgjax](https://github.com/knaaptime/pgjax) draws Pólya-Gamma variates as an XLA
custom call, so a Gibbs sampler that needs them stays on the accelerator. It
replaces `jax.pure_callback` around a host-side sampler, which pays a round trip
between device and host on every sweep and serializes under `jax.pmap`.
