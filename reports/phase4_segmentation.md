# Phase 4: Segmentation by Product Category

## Question
Is the low overall repeat purchase rate (3.12%) mostly explained by product
mix — i.e., Olist is dominated by one-off, considered purchases (furniture,
electronics) that people simply don't rebuy soon — or is it a more
universal experience problem that cuts across categories?

## Method
Grouped each customer's first order by `product_category_name` (mapped via
the order_items → products join), filtered to categories with at least 200
orders to avoid noise from tiny categories, and compared repeat purchase
rate across categories.

## Finding: category explains very little
- Highest repeat-rate category: **eletrodomesticos** (home appliances) at
  just **9.23%** — still low by normal e-commerce standards
- Lowest: **livros_tecnicos** (technical books) at **0.80%**
- Full range across ~30 real categories: **0.80% to 9.23%**
- Standard deviation across categories: **1.48 percentage points**

This is a narrow, tightly clustered spread. If the low repeat rate were
mainly structural — driven by product type — we'd expect to see some
categories (e.g. beauty, household consumables) sitting far higher than
others (e.g. furniture, big electronics). Instead, essentially every
category, regardless of what it is, clusters in the same low single-digit
band.

## Why this matters
This rules out the "it's just what people are buying" explanation as the
primary driver. Combined with Phase 3's finding that delivery delay (not
review score) predicts repeat purchase, the evidence points toward a
platform-wide, category-agnostic experience factor — most likely delivery
performance — rather than a product-mix problem that would call for
category-specific retention marketing.

## Implication for the recommendation
This supports prioritizing logistics/delivery-speed investment over
category-targeted retention campaigns: the retention problem looks uniform
across what customers buy, not concentrated in any one segment.