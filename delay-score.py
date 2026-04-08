''' 
Objective: First, I want to determine if my hypothesis that a delivery delay could 
significantly impact the situation is valid before considering other factors.

Logic: Get both sheets using the key "order_id":
- olist_order_reviews_dataset.csv
    - Get "review_score"
- olist_orders_dataset.csv
    - Get "order_delivered_customer_date","order_estimated_delivery_date"

Then, I calculate the difference between the dates and discover how it impacts the score
-> Without delay: average percentual and probability of getting 1 star
-> With delay: average percentual and probability of getting 1 star
Analyse the difference
'''

import pandas as pd


df_score = pd.read_csv(r'C:\Projetos\Students-Performance-in-Exams---Kaggle\files\olist_order_reviews_dataset.csv') # r before 'address' help me with python changing my address and take me an error
score_filtered = df_score[['order_id', 'review_score']]

df_date = pd.read_csv(r'C:\Projetos\Students-Performance-in-Exams---Kaggle\files\olist_orders_dataset.csv')
date_filtered = df_date[['order_id','order_delivered_customer_date','order_estimated_delivery_date']]

df_final = pd.merge(score_filtered, date_filtered, on='order_id')
# print(df_score.head()) - debug to show if everything was ok 


# convert to dateTime objects - input types like dataframes can't tolerer operations like sum
df_final['real_date'] = pd.to_datetime(df_final['order_delivered_customer_date'])
df_final['estimated_date'] = pd.to_datetime(df_final['order_estimated_delivery_date'])

df_final['difference_days'] = (df_final['real_date']-df_final['estimated_date']).dt.days # to remove the hour (real_date has the hour of the delivery) we use tje dt.days
df_final['Had delay'] = df_final['difference_days'] > 0 # receives false or true

relationship_ScoreAverage_Delay = df_final.groupby('Had delay')['review_score'].mean()



print("Average score:")
print(relationship_ScoreAverage_Delay)



