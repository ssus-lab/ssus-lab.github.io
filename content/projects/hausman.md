---
title: "Bayesian Hausman Tests for Spatial Panels"
status: "Current"
venue: "Spatial Economic Analysis, under review"
weight: 42
areas: ["methods"]
summary: "One Bayes factor that chooses among random, correlated random, spatially correlated random, and fixed effects in a spatial panel, and names the assumption that fails."
image: "img/fig/hausman-rho.webp"
image_dark: "img/fig/hausman-rho-dark.webp"
alt: "Dot chart of the posterior mean of rho under four models of the unit effects, random (RE), correlated random (CRE), spatially correlated random (SRE), and fixed (FE), in five simulation designs, with the true value 0.4 marked. When the effects depend on nothing, all four sit at 0.4. When they depend on the covariates' means, RE estimates 0.73 and 0.95; when they follow a spatial field, RE and CRE estimate 0.45 to 0.49. In every design the model the comparison chooses, ringed, sits at 0.4."
caption: "Simulated spatial lag panels on a 20 × 20 rook grid over five periods, 50 datasets per design, true ρ = 0.4. Each dot is one model's posterior mean of ρ, averaged over the datasets; the ring marks the model the comparison chooses, in 48 to 50 of the 50 datasets in every design. Random effects misstate ρ whenever the effects depend on the covariates or on one another, and the Mundlak model (CRE) repairs the first failure but not the second."
---

Whether a spatial panel's unit effects are fixed or random decides which
variation identifies its spatial parameter. The paper gives the analyst one
Bayes factor that chooses among random, correlated random, spatially correlated
random, and fixed effects, and that names the assumption at fault when random
effects fail. The same comparison chooses between the spatial lag and spatial
Durbin models, and with a complementary overidentification statistic it forms a
specification search for spatial panels, beside the Lagrange-multiplier tests of
the spatial process.

The usual arbiter is a Hausman contrast (Mutl and Pfaffermayr 2011; Lee and Yu
2012), whose alternative is effects correlated with the covariates. Spatial data
admit a second departure: the effects of neighboring units can be correlated
with one another, as when an unobserved condition spans several units. Under
such effects random effects misstate the spatial parameter, and so does the
Mundlak model, the alternative those tests take. A likelihood Bayes factor
cannot settle the matter either, because fixed effects are random effects under
a flat prior, and whoever sets the prior on the effects decides between them.

The paper compares the models by their moment conditions instead. Each
random-effects assumption states that a block of moments is zero, and a model
that drops an assumption frees its block, so the four models differ only in the
blocks they free. Their marginal exponentially tilted empirical likelihoods need
no prior on the effects, and under high-level conditions the comparison selects
the most restrictive valid model with probability tending to one. On the county
homicide panel of Baller and colleagues (2001), 3,085 U.S. counties in the
censuses from 1960 to 1990, it chooses the spatial Durbin model with fixed
effects.
