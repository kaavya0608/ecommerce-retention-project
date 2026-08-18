# Fix the Leak: Retention & Logistics Analysis (Olist E-Commerce)

## Business Question
Olist's repeat purchase rate is low. Where should the company invest its next
marketing/ops dollar to improve customer lifetime value — logistics
(faster/more reliable delivery) or retention marketing (post-purchase
engagement)? Which lever moves the needle more, for which customer segments?

## Why this matters (the pitch, for the report)
Marketplaces live and die on repeat purchase rate. Acquiring a new customer
costs far more than retaining one. If late delivery is driving churn, the
fix is operational (carrier SLAs, warehouse placement). If churn is driven
by something else (product mismatch, price sensitivity, one-time gift
buyers), operational fixes won't move the number — retention marketing will.
This analysis quantifies which lever matters more, and for whom.

## Dataset
Olist Brazilian E-Commerce Public Dataset (Kaggle), ~100k orders 2016-2018.
Tables: orders, order_items, order_payments, order_reviews, customers,
sellers, products, product_category_translation, geolocation.

## Analysis Plan

### Phase 1 — Data audit & cleaning
- Load all tables, document schema and row counts
- Identify nulls, duplicates, date range issues, currency/units
- Build a single analysis-ready "order-level" table via joins

### Phase 2 — Exploratory analysis (question-driven, not generic)
- Distribution of delivery time (estimated vs actual)
- Distribution of review scores
- Repeat purchase rate overall and by segment (region, category, price tier)
- First look: does late delivery correlate with lower review score?

### Phase 3 — Statistical testing
- H1: Late delivery is associated with lower review scores
- H2: Review score is associated with repeat purchase likelihood
- H3: Delivery delay's effect on repeat purchase, controlling for confounders

### Phase 4 — Segmentation
- RFM (Recency, Frequency, Monetary) segmentation of customers
- Identify which segments are most sensitive to delivery delay vs price vs
  product category

### Phase 5 — Synthesis & recommendation
- Quantify the retention lift from fixing delivery delay vs a retention
  marketing push, with stated assumptions and limitations

### Phase 6 — Deliverables
- `reports/` — written analysis
- `dashboard/` — interactive Streamlit app
- `notebooks/` — exploratory notebooks

## Key findings so far
- Repeat purchase rate: **3.12%** — well below typical e-commerce benchmarks
- Late delivery strongly hurts review scores (4.29★ on-time vs 2.27★ late,
  p < 0.001, large effect size)
- But review score does NOT significantly predict repeat purchase (p = 0.90)
- What does predict repeat purchase: raw delivery delay length (each extra
  day costs ~0.9% in odds) and order value/type