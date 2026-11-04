---
title: "Fast and Unbiased Log-Determinants for Large Spatial Autoregressive Models"
status: "Current"
weight: 30
venue: "Journal of Geographical Systems, under review"
areas: ["methods"]
software: ["neighbayes", "sparsax"]
summary: "Log-determinant methods that make Bayesian spatial autoregressive models fast and unbiased at the scale of every U.S. census tract."
image: "img/fig/logdet-bias.webp"
image_dark: "img/fig/logdet-bias-dark.webp"
alt: "Line chart of bias in the posterior mean of rho, in posterior standard deviations, against true rho from 0.3 to 0.95. Factorize-and-interpolate, stochastic Chebyshev, and Pace–LeSage lie on zero throughout; Barry–Pace lifts off at 0.85 and reaches 1.4 at 0.95; Smirnov–Anselin and grid and spline rise to 0.18 and 0.13 at 0.95."
caption: "Bias in the posterior mean of ρ, in posterior standard deviations, by true ρ, for a spatial autoregressive model of all 85,230 U.S. census tracts. Factorize-and-interpolate, stochastic Chebyshev, and Pace–LeSage lie on zero; Barry–Pace lifts off near the boundary and reaches 1.4 standard deviations at ρ = 0.95, and Smirnov–Anselin and grid and spline follow more modestly. Bands span the probe draws of the two stochastic methods. Positive ρ; the paper also reports the negative range."
---

Fitting a spatial autoregressive model means evaluating the log-determinant of
its Jacobian over and over, thousands of times in a Bayesian sampling run, and
that cost has long limited the sample sizes the models reach. The paper
introduces two methods. The first treats the log-determinant as an analytic
function of the autoregressive parameter and interpolates it with the AAA
algorithm; it suits most spatial weights matrices, directed or undirected. The
second is matrix-free, built on stochastic Chebyshev traces, for weights that
are dense or have hub-and-spoke structure. Both stay unbiased as the
autoregressive parameter approaches the edge of its stability region, where the
most scalable methods in current use do not.

With them, a Bayesian spatial autoregressive model of all 85,230 U.S. census
tracts needs about a second of Jacobian computation per chain of 2,000 draws,
where the next-best unbiased method takes several minutes. The methods ship in
[neighbayes]({{< relref "/software/neighbayes" >}}).
