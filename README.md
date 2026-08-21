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

## Key findings
- **Repeat purchase rate: 3.12%** — well below typical e-commerce benchmarks
  (20-40%+), the core problem this analysis investigates
- **Late delivery strongly hurts satisfaction**: review scores drop from
  4.29★ (on-time) to 2.27★ (late), p < 0.001, large effect size (0.64)
- **But review score does NOT predict repeat purchase** (p = 0.899) — the
  counter-intuitive twist this project is built around
- **Delivery delay itself does predict repeat purchase** (p < 0.001): each
  extra day of delay costs ~0.9% in odds, compounding to ~24% lower odds
  for a 30-day-later delivery
- **Product category explains very little of the low repeat rate**
  (0.80%–9.23% range across ~30 categories, tightly clustered) — this is
  not a "wrong product mix" problem, it's broad-based
- **Modeled impact**: a realistic 5-day delivery improvement projects to
  ~R$21,700 incremental revenue on this cohort — a real, defensible signal,
  though modest relative to the scale of the retention gap

## Recommendation
Invest in delivery reliability over review-score optimization or
category-specific retention campaigns — the data shows delivery delay
(not customer sentiment or product type) is the strongest available lever
on repeat purchase.

## Project structure
- `src/` — data cleaning and preparation scripts
- `notebooks/` — exploratory analysis and statistical testing
- `reports/` — phase-by-phase written findings (data audit, EDA & stats,
  segmentation, synthesis & recommendation)
- `dashboard/` — interactive Streamlit app (`streamlit run dashboard/app.py`)