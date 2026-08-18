import pandas as pd

RAW = 'data/'
OUT = 'data/'

orders = pd.read_csv(f'{RAW}olist_orders_dataset.csv', parse_dates=[
    'order_purchase_timestamp', 'order_approved_at',
    'order_delivered_carrier_date', 'order_delivered_customer_date',
    'order_estimated_delivery_date'])
items = pd.read_csv(f'{RAW}olist_order_items_dataset.csv')
payments = pd.read_csv(f'{RAW}olist_order_payments_dataset.csv')
reviews = pd.read_csv(f'{RAW}olist_order_reviews_dataset.csv')
customers = pd.read_csv(f'{RAW}olist_customers_dataset.csv')

items_agg = items.groupby('order_id').agg(
    n_items=('order_item_id', 'count'),
    total_price=('price', 'sum'),
    total_freight=('freight_value', 'sum'),
    n_sellers=('seller_id', 'nunique'),
).reset_index()

pay_agg = payments.groupby('order_id').agg(
    total_payment_value=('payment_value', 'sum'),
    n_payment_installments=('payment_installments', 'max'),
).reset_index()
pay_type = payments.sort_values('payment_sequential').groupby('order_id')['payment_type'].first().reset_index()
pay_agg = pay_agg.merge(pay_type, on='order_id')

reviews_slim = (reviews.sort_values('review_creation_date')
                 .groupby('order_id').first().reset_index()
                 [['order_id', 'review_score', 'review_creation_date']])

cust_slim = customers[['customer_id', 'customer_unique_id', 'customer_state', 'customer_city']]

master = orders.merge(cust_slim, on='customer_id', how='left')
master = master.merge(items_agg, on='order_id', how='left')
master = master.merge(pay_agg, on='order_id', how='left')
master = master.merge(reviews_slim, on='order_id', how='left')

master['delivery_days'] = (master['order_delivered_customer_date'] - master['order_purchase_timestamp']).dt.days
master['estimated_delivery_days'] = (master['order_estimated_delivery_date'] - master['order_purchase_timestamp']).dt.days
master['delivery_delay_days'] = (master['order_delivered_customer_date'] - master['order_estimated_delivery_date']).dt.days
master['is_late'] = master['delivery_delay_days'] > 0

order_counts = master.groupby('customer_unique_id')['order_id'].transform('nunique')
master['customer_total_orders'] = order_counts
master['is_repeat_customer'] = order_counts >= 2

delivered = master[master['order_status'] == 'delivered'].copy()

master.to_parquet(f'{OUT}master_orders.parquet', index=False)
delivered.to_parquet(f'{OUT}delivered_orders.parquet', index=False)

print(f"master_orders: {master.shape}")
print(f"delivered_orders: {delivered.shape}")
print(f"Repeat purchase rate: {(master.groupby('customer_unique_id')['is_repeat_customer'].first().mean())*100:.2f}%")