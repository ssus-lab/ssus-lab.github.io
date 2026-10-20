---
title: "Zoning and Segregation in Principal Cities and Suburbs: Another Look at the Examples of Houston and Dallas, Texas"
status: "Current"
venue: "Annals of Regional Science, under review"
weight: 45
software: ["segregation"]
summary: "Houston's lack of zoning is the standing natural experiment in land-use scholarship; re-run the comparison inside each metropolis, principal city against suburbs, and the answer changes."
---

Houston has no zoning, and that fact has made it the standing natural
experiment in land-use scholarship: compare Houston with a zoned peer, and
whatever differs is attributed to zoning. Christopher Berry's widely cited
comparison of Houston and Dallas (2001) found no significant difference in
Black–White segregation and concluded zoning was unlikely to be a major driver
of it.

The comparison is pitched at the wrong scale. Zoning is a municipal
instrument, and its effect operates through competition among jurisdictions
*within* a metropolis, the sorting the Tiebout mechanism describes, not
through differences *between* metropolises, which average the mechanism away.
Re-partitioning each region into principal city versus suburbs and testing
within each also reveals the two cities as poor partners for the comparison:
Houston's principal city holds two-thirds of its region's population, Dallas's
under a quarter.

Measured with the spatial information theory index, chosen because an additive
decomposition across the city–suburb partition is built into it, and inferred
by comparative spatial inference with 10,000 permutations per comparison, the
analysis re-runs the original on 1990 census and 2021 ACS tracts, Black–White
throughout. Between metropolises, the original's null result holds in both
years. Inside each region, the city–suburb test separates them: in 1990 both
principal cities were significantly more segregated than their suburbs; by
2021 the city of Dallas remains so, and the city of Houston no longer is.
Three decades of the same macroeconomic forces, two land-use regimes. The
analysis runs in the lab's [segregation
package]({{< relref "/software/segregation" >}}).