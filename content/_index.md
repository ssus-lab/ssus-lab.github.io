---
title: "Spatial Science and Urban Systems"
statement: "We build open-source methods, models, and software for understanding sociospatial structure."
areas:
  - name: "Urban spatial structure"
    icon: "sorting"
    fields: ["Urban economics", "Residential sorting", "Housing and land markets", "Neighborhood dynamics"]
    methods: ["Discrete choice models", "Land value models", "Agglomeration measurement", "Geodemographic clustering"]
  - name: "Spatial science"
    icon: "methods"
    fields: ["Spatial econometrics", "Spatial statistics", "Spatial data science", "Urban analytics", "Computational social science"]
    methods: ["Spatial autoregressive models", "Bayesian estimation at scale", "Areal interpolation", "Regionalization", "Network accessibility"]
  - name: "Inequality and policy"
    icon: "inequality"
    fields: ["Segregation", "Neighborhood effects", "Access to opportunity", "Housing policy", "Public health"]
    methods: ["Multiscalar segregation profiles", "Opportunity mapping", "Facility location models", "Space-time analysis"]
figure:
  image: "img/fig/multiscalar-profiles.webp"
  alt: "Nine small line charts, one per metropolitan area, each showing a segregation index falling as the distance defining the neighborhood grows, with one line per census year from 1980 to 2010."
  title: "Segregation depends on the scale you measure it at"
  text: "A multiscalar profile recomputes segregation as the neighborhood around each location widens. Here, nine U.S. metropolitan areas from 1980 to 2010: the curves fall with distance, and the shape of the fall differs from one metro to the next."
  link: "software/segregation/"
  linktext: "The segregation package computes these profiles"
---

SSUS is the research lab of [Elijah Knaap](people/eli-knaap/) at the
University of California, Irvine. We study who lives where and why: how
households sort across neighborhoods, how housing and land markets price
location, and how the resulting patterns of segregation and opportunity change
over time.

Outcomes in one place depend on its neighbors, so these questions need spatial
models: we develop spatial econometric and Bayesian models of sorting and
spillovers, and the sparse numerical tools that make them feasible for whole
metropolitan regions.

The questions come from policy. Our models have informed a federal fair-housing
evaluation and a regional plan, and show where harm-reduction services would
reach the most overdose risk. The methods behind them ship as open-source
software, so others can check the analysis and apply it to their own decisions.
