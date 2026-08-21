import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Olist Retention Analysis", layout="wide")

@st.cache_data
def load_data():
    delivered = pd.read_parquet('data/delivered_orders.parquet')
    return delivered

delivered = load_data()

st.title("Fix the Leak: E-Commerce Retention Analysis")
st.caption("Olist Brazilian E-Commerce Dataset · ~100K orders, 2016-2018")

# --- Headline metrics ---
col1, col2, col3 = st.columns(3)
repeat_rate = delivered.groupby('customer_unique_id')['is_repeat_customer'].first().mean()
late_pct = delivered['is_late'].mean()
avg_review = delivered['review_score'].mean()

col1.metric("Repeat Purchase Rate", f"{repeat_rate*100:.2f}%", help="Industry benchmark: 20-40%+")
col2.metric("% Orders Late", f"{late_pct*100:.2f}%")
col3.metric("Avg Review Score", f"{avg_review:.2f} ★")

st.divider()

# --- Finding 1: Delivery delay vs review score ---
st.subheader("Finding 1: Late delivery devastates review scores")
review_by_late = delivered.groupby('is_late')['review_score'].mean().reset_index()
review_by_late['is_late'] = review_by_late['is_late'].map({True: 'Late', False: 'On-time'})
fig1 = px.bar(review_by_late, x='is_late', y='review_score',
              labels={'is_late': 'Delivery Status', 'review_score': 'Avg Review Score'},
              color='is_late', color_discrete_map={'On-time': '#2ca02c', 'Late': '#d62728'})
fig1.update_layout(showlegend=False)
st.plotly_chart(fig1, use_container_width=True)
st.caption("Mann-Whitney U test: p < 0.001, effect size 0.64 (large)")

st.divider()

# --- Finding 2: The twist ---
st.subheader("Finding 2: But review score doesn't predict repeat purchase")
st.markdown("""
Logistic regression controlling for order value, item count, and region:
- **Review score** → not significant (p = 0.899)
- **Delivery delay** → highly significant (p < 0.001), ~24% lower odds of repeat purchase per 30-day delay
- **Region** → not significant once other factors are controlled
""")

st.divider()

# --- Interactive filter: repeat rate by state ---
st.subheader("Explore: Repeat Purchase Rate by Region")
customer_state_map = delivered.groupby('customer_unique_id').agg(
    customer_state=('customer_state', 'first'),
    is_repeat_customer=('is_repeat_customer', 'first')
).reset_index()

state_repeat = customer_state_map.groupby('customer_state').agg(
    repeat_rate=('is_repeat_customer', 'mean'),
    n_customers=('customer_unique_id', 'count')
).reset_index()
state_repeat = state_repeat[state_repeat['n_customers'] >= 100].sort_values('repeat_rate', ascending=False)

fig2 = px.bar(state_repeat.head(15), x='customer_state', y='repeat_rate',
              labels={'customer_state': 'State', 'repeat_rate': 'Repeat Purchase Rate'})
st.plotly_chart(fig2, use_container_width=True)

st.divider()
st.markdown("**Recommendation:** Invest in delivery reliability over review-score optimization or category-specific retention campaigns. See full report in `/reports`.")