# Phase 1: Data Audit Findings

## Dataset overview
- 99,441 orders spanning **2016-09-04 to 2018-10-17** (~2 years)
- 9 relational tables, joined to a single order-level table (`master_orders`)
- 96,478 orders (97%) have status `delivered`; the rest are canceled,
  unavailable, shipped-but-not-delivered, or still in process — these are
  excluded from delivery/review analysis (Phase 2+) since they lack
  delivery dates or reviews.

## Critical schema gotcha
`customer_id` is **generated per order** — the same real person gets a new
`customer_id` on every order. The actual person is identified by
`customer_unique_id`. Any repeat-purchase analysis using `customer_id`
directly would incorrectly show 0% repeat customers. This is fixed in the
join by aggregating on `customer_unique_id`.

## Headline finding
**Repeat purchase rate is 3.12%** — only ~3,000 of 96,000 unique customers
placed a second order in this ~2-year window. This is unusually low for
e-commerce (industry benchmarks are typically 20-40%+) and is the core
problem this analysis investigates.

Two honest possible explanations to keep in view (not yet resolved):
1. Genuine retention failure — something about the experience discourages
   repeat purchase (delivery, product quality, price).
2. Structural: Olist is a marketplace largely used for one-off, considered
   purchases (furniture, electronics) rather than repeat-consumption goods
   — some of this data-not-behavior. Phase 4 (segmentation by category)
   should check whether repeat rate varies a lot by product category, which
   would support this alternative explanation partially.

## Data quality notes
- `order_delivered_customer_date` missing for 2,965 orders (undelivered/
  canceled orders — expected)
- `review_score` missing for 768 orders (~0.8%) — buyer never reviewed
- `product_category_name` missing for 610 products (~1.9%) — will need
  "unknown" bucket if used in segmentation
- Payments table has multiple rows per order (installments/split payments)
  — aggregated to total value per order

## Output
- `data/master_orders.parquet` — all orders, all columns joined
- `data/delivered_orders.parquet` — filtered to delivered orders only,
  used for delivery/review/repeat-purchase analysis going forward