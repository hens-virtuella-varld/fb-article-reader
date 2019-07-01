import csv
import pandas as pd


df = pd.read_csv('.csv')

saved_column = df[['date', 'text', 'post_id']]
timeline_articles = saved_column.sort_values('date')
