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
  - name: "Sorting and change"
    icon: "sorting"
    text: "Who lives where, and how neighborhoods change."
    examples: ["Residential sorting", "Segregation", "Neighborhood change", "Neighborhood effects"]
  - name: "Access and policy"
    icon: "inequality"
    text: "Who can reach what, and how public decisions change it."
    examples: ["Access to opportunity", "Schools", "Public health", "Transportation", "Fair housing"]
methods:
  label: "How we work"
  items: ["Spatial econometrics", "Spatial statistics", "Bayesian estimation at scale", "Discrete choice models", "Measurement models", "Areal interpolation", "Regionalization", "Network accessibility", "Open-source software"]
figure:
  image: "img/fig/multiscalar-profiles.webp"
  alt: "Nine small line charts, one per metropolitan area, each showing a segregation index falling as the distance defining the neighborhood grows, with one line per census year from 1980 to 2010."
  title: "Segregation depends on the scale you measure it at"
  text: "A multiscalar profile recomputes segregation as the neighborhood around each location widens. Here, nine U.S. metropolitan areas from 1980 to 2010: the curves fall with distance, and the shape of the fall differs from one metro to the next."
  link: "software/segregation/"
  linktext: "The segregation package computes these profiles"
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
