# Phase 5: Synthesis & Recommendation

## The question
Should Olist invest its next dollar in logistics (faster delivery) or
retention marketing, to improve repeat purchase rate?

## What the evidence shows
1. **Late delivery devastates review scores** (4.29★ → 2.27★, large
   effect) — but review score does not predict repeat purchase (p=0.899).
2. **Delivery delay itself does predict repeat purchase** (p<0.001): each
   extra day of delay reduces the odds of a repeat purchase by ~0.9%,
   compounding to a ~24% odds reduction for a 30-day-later delivery.
3. **Product category explains very little of the low repeat rate**
   (0.80%–9.23% range, tight clustering) — this is not a "wrong product
   mix" problem, it's broad-based.

## Quantifying the delivery lever
Modeling a realistic 5-day reduction in average delivery delay against the
logistic regression:
- Baseline repeat rate: 3.20%
- Projected repeat rate: 3.35% (+0.15 percentage points)
- On this cohort (~93K customers, avg order value R$160): ~136 incremental
  repeat customers, ~R$21,700 incremental revenue

## Honest assessment: the effect is real but modest
Delivery delay is statistically significant and directionally correct —
faster delivery does help retention, and it's the strongest lever found in
this analysis. But the magnitude is small relative to the scale of the
problem: a 5-day improvement moves the needle by 0.15 percentage points,
not enough on its own to close the gap to typical e-commerce repeat rates
(20-40%+). This suggests delivery speed is a real, defensible investment,
but not a silver bullet — most of the "why don't people come back" question
remains open and likely involves factors not captured in this dataset
(pricing, product fit, marketplace trust, competition).

## Recommendation
1. **Invest in delivery reliability, not review-score optimization.**
   Chasing better reviews as a retention lever is not supported by the
   data — review score and repeat purchase are statistically unrelated.
   Any operational fix should be justified by delay itself, not by its
   effect on ratings.
2. **Don't over-index on category-specific retention campaigns.** The
   problem is broad-based, not concentrated in a handful of product types.
3. **Treat the R$21,700/cohort estimate as a lower bound on the logistics
   case, not a full ROI model.** It should be annualized against real order
   volume and weighed against the actual cost of a 5-day logistics
   improvement — data this analysis doesn't have.
4. **Flag as future work:** since delivery delay only explains part of the
   picture, the next highest-value analysis would investigate other
   candidate drivers (pricing sensitivity, first-purchase product category,
   marketing channel) to find the rest of the retention story.

## Limitations (stated plainly)
- This is observational data; regression controls reduce but do not
  eliminate confounding — this is not a randomized experiment.
- The revenue projection assumes the historical delay/retention
  relationship holds if delivery is actually improved, which is an
  assumption, not a guarantee.
- No cost data for logistics improvements was available, so this is a
  benefit-only estimate, not a full cost-benefit analysis.