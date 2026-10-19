---
title: "Space Is Not a Control Group: Quasi-Experimental Design in the Presence of Spatial Dependence"
status: "Current"
weight: 20
summary: "Why difference-in-differences cannot recover the effect of a treatment defined by location, and the spatial fixed-effects design that can."
image: "img/fig/rentpanel-simulation-gap.webp"
alt: "Three panels from a Monte Carlo. Left: as unit heterogeneity becomes more spatially structured, the between-group estimate of the spatial parameter climbs from 0.5 to about 0.9 while the within-unit estimate stays on the true 0.5. Center: the between-group treatment effect falls from 10 to about 3 while the within-unit estimate stays on the true 10. Right: with no spatial dependence in the outcome, the within-unit estimate is zero and the between-group estimate is 0.735."
fit: figure
caption: "Monte Carlo, 500 replicates per cell. Left: the estimated spatial parameter against the spatial structure of unit heterogeneity, true ρ = 0.5. Center: the estimated treatment effect, true δ = 10. Right: an outcome with no spatial dependence, where the between-group (DID) design still reports ρ = 0.735. The within-unit (FE) design stays on the truth throughout."
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
