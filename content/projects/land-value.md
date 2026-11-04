---
title: "Proof-of-Concept Land Value Models: A Spatial Econometric Approach"
funder: "Robert Schalkenbach Foundation"
years: "2023–2024"
status: "Completed"
role: "Co-PI (PI: Chester Harvey)"
weight: 100
short: "Land value models"
areas: ["structure"]
software: ["neighbayes"]
summary: "A spatial Durbin approach to estimating land value from property sales, with a proof of concept in Baltimore City."
---

Land value is rarely observed directly, since vacant land seldom sells, so most
land values are modeled as a residual: a property's total value minus the value
of its structure. As a regression, that residual requires a perfectly specified
model, because any misspecification is indistinguishable from land or housing
value. Land prices are also spatially dependent, directly through spillovers
from neighboring parcels and latently through price speculation.

The project's approach, developed by Knaap, fits a spatial Durbin hedonic model
to property sales and specifies it as fully as possible, then sums the land
components (the intercept and the land terms, with their direct and indirect
spatial effects) and leaves the value of the structure aside. The proof of
concept built the hedonic specification on property sales in Baltimore City,
where every test for spatial dependence rejected the non-spatial model. The
method is set out in the chapter *The Hedonic Housing Price Model* of Knaap's
[*Urban Analysis & Spatial Science*](https://knaaptime.com/urban_analysis), and
its prediction step is implemented in
[neighbayes]({{< relref "/software/neighbayes" >}}).
