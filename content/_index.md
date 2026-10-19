---
title: "Spatial Science and Urban Systems"
statement: "We study the spatial organization of neighborhoods, cities, and regions."
# Three ways into the work, each with examples rather than a boundary; the
# methods that serve all three sit in one row beneath them.
areas:
  - name: "Structure and Form"
    icon: "structure"
    text: "How land, housing, and jobs are arranged across a region."
    examples: ["Land and housing markets", "Economic geography", "Agglomeration", "Urban form"]
  - name: "Sorting and Change"
    icon: "sorting"
    text: "Who lives where, and how neighborhoods change."
    examples: ["Residential sorting", "Segregation", "Neighborhood change", "Neighborhood effects"]
  - name: "Access and Policy"
    icon: "inequality"
    text: "Who can reach what, and how public decisions change it."
    examples: ["Access to opportunity", "Schools", "Public health", "Transportation", "Fair housing"]
methods:
  label: "How We Work"
  items: ["Spatial econometrics", "Spatial statistics", "Bayesian estimation at scale", "Discrete choice models", "Measurement models", "Areal interpolation", "Regionalization", "Network accessibility", "Open-source software"]
figure:
  image: "img/fig/network-walkshed.webp"
  alt: "A map of San Clemente, California, centered on a marked point: a large translucent red circle covers everything within one mile as the crow flies, while a much smaller blue polygon covers only the streets reachable within a one-mile walk; the polygon is a fraction of the circle across the hilly, cul-de-sac neighborhood."
  title: "A neighborhood is what you can walk to"
  text: "Segregation indices usually draw each neighborhood as a circle. Measured along the street network instead, the neighborhood shrinks to the streets a person can actually reach — and with it the city's measured segregation: across all 380 U.S. metropolitan areas, the network-based measure runs about 20 percent higher, and the gap is widest where streets are winding and sparsely connected."
  link: "https://doi.org/10.1177/23998083231197956"
  linktext: "Read the paper in Environment and Planning B"
book:
  title: "Urban Analysis & Spatial Science"
  subtitle: "Theory, Methods, & Code for Studying Neighborhoods, Cities, & Regions"
  text: "Knaap's textbook introduces the theory and intermediate quantitative methods of urban and regional analysis as a series of executable computational notebooks in Python. Each chapter takes a topic from the social science and policy literature and carries out a real analysis step by step."
  venue: "CRC Press, forthcoming 2027 · draft online, CC BY-NC-ND"
  url: "https://knaaptime.com/urban_analysis"
  figcaption: "Bid rent, from the book's part on urban spatial structure: each land use outbids the others over one band of distance from the market center, so land rent follows the upper envelope of the three bids."
  parts: ["Spatial Data", "Interpolation and Change of Support", "Spatial Analysis", "Accessibility and Interaction", "Urban Spatial Structure", "Segregation", "Urban Factor Models", "Neighborhood Delineation", "Neighborhood Change", "Spatial Econometrics", "Location Models"]
---

SSUS is the research lab of [Elijah Knaap](people/eli-knaap/) at the
University of California, Irvine. We draw on urban economics, sociology, and
geography to explain why activity concentrates where it does, how places
change, and who gains or loses as they do.

People and places are connected and interdependent. Understanding network
structure and relationships embedded in space requires formal geographic
models: we develop spatial econometric and Bayesian models of spillovers,
sorting, and flows, and the sparse numerical tools that make them feasible for
whole metropolitan regions.
