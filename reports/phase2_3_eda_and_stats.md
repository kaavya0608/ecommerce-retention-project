# Phase 2 & 3: EDA and Statistical Testing

## EDA headline numbers
- Median delivery time: 10 days (mean 12.1, right-skewed — some orders take 100+ days)
- 6.77% of orders arrive later than the estimate given at checkout
- Review scores: 59% are 5-star, but 13% are 1-2 star — bimodal, not a
  smooth distribution. Late orders look very different (see below).

## H1: Late delivery tanks satisfaction — confirmed, large effect
- On-time orders: mean review score **4.29**
- Late orders: mean review score **2.27**
- Mann-Whitney U test: p < 0.001 (effectively 0), rank-biserial effect
  size = 0.64 (large)
- Bootstrap 95% CI on the mean difference: [-2.06, -1.98] stars

**This is not subtle.** Late delivery is one of the strongest satisfaction
drivers in the dataset.

## H2: Does review score predict repeat purchase? — Not once you look closely
Bivariate logistic regression (review_score -> repeat purchase):
coefficient not significant (p = 0.71). Even in the full controlled model
(p = 0.90). The star rating a customer leaves has **no measurable
relationship** with whether they come back.

## H3: What actually predicts repeat purchase (controlled model)
Logistic regression on first order -> becomes repeat customer, controlling
for region (state), order value, and item count (n = 92,746):

| Variable | Odds ratio | p-value | Interpretation |
|---|---|---|---|
| review_score | 0.998 | 0.90 | No effect |
| delivery_delay_days | 0.991/day | <0.001 | Each extra day late reduces repeat odds ~0.9% |
| log(payment value) | 0.880 | <0.001 | Bigger one-off orders are *less* likely to repeat |
| n_items | 1.241 | <0.001 | More items per order → more likely to repeat |
| state (region) | — | not significant | No regional effect once value/delay controlled |

**Plain-English translation:** a customer whose delivery arrived 30 days
later than another customer's has about **24% lower odds** of becoming a
repeat buyer, holding order value and region constant.

## Why this matters for the business recommendation
The naive story would be: "reviews are bad because of late delivery, bad
reviews drive churn, fix delivery to fix reviews to fix churn." The data
doesn't support the middle link. Review score is a satisfaction signal, not
a retention lever. The retention lever is the raw delivery delay itself,
and separately, the type of purchase (high-value one-off items vs
multi-item baskets).

## Caveats
- This is observational data — not a randomized experiment.
- Review score may still matter for other outcomes not tested here.
- Next (Phase 4): segment by product category.
