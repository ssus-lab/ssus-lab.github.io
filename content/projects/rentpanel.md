---
title: "Space Is Not a Control Group: Quasi-Experimental Design in the Presence of Spatial Dependence"
status: "Current"
weight: 20
venue: "Journal of Regional Science, under review"
areas: ["structure", "methods"]
summary: "Why difference-in-differences cannot recover the effect of a treatment defined by location, and the spatial fixed-effects design that can."
image: "img/fig/rentpanel-effect.webp"
image_dark: "img/fig/rentpanel-effect-dark.webp"
alt: "Line chart of the estimated treatment effect against the spatial structure of unit heterogeneity, from 0 to 0.8. The within-unit estimate stays at 10, the true effect, throughout; the between-group estimate falls steadily from 10.2 to 3.2."
caption: "Monte Carlo, 500 replicates per cell, with a true treatment effect of 10 (dashed) and a true spatial parameter of 0.5. As unit heterogeneity becomes more spatially structured, the between-group (difference-in-differences) estimate falls from 10.2 to 3.2, while the within-unit (fixed-effects) estimate stays on the truth. Bars are one standard deviation across replicates."
---

Applied work estimates the effect of a place-based treatment, such as a new
transit line or a regulatory boundary, with difference-in-differences or fixed
effects, and treats the choice between them as immaterial. The two designs are
numerically identical for an unstaggered treatment in a balanced two-period
panel, but only in the aspatial case. When the outcome is spatially dependent,
the spatial multiplier is itself a function of location, so a period shock that
varies across space produces a differential trend correlated with treatment by
construction. The conditions under which parallel trends survive cannot be
tested with two periods, and an explicit spatial model is required.

Adding one does not rescue difference-in-differences. The spatial parameter is
identified from the residual variation that separates unit-level from
group-level conditioning, and the treatment effect depends on it. In
simulation, the between-group design understates the effect by up to 68 percent
and reports a spatial parameter of 0.735 where the outcome has none. On
Montgomery County rents around the announcement of the Purple Line, a
light-rail line in suburban Maryland, it returns the larger spatial parameter
in all 124 comparisons. The announcement moved rents little, and only the
spatial fixed-effects design recovers that estimate.
