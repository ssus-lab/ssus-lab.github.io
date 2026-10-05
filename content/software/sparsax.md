---
title: "sparsax"
code: true
pypi: true
org: ssus
weight: 1
role: "Lead"
repo: "https://github.com/knaaptime/sparsax"
summary: "Sparse direct solvers for JAX, backed by SuiteSparse: factorizations, solves, and log-determinants that run natively inside compiled code."
---

[sparsax](https://github.com/knaaptime/sparsax) exposes SuiteSparse's CHOLMOD
(Cholesky, for symmetric positive definite matrices) and KLU (LU, for general
matrices) to JAX as XLA custom calls. A sparse factorization therefore runs at
native speed inside `jax.jit`, `lax.scan`, and `lax.fori_loop`, with no Python
callback and no round trip between device and host on each iteration.
