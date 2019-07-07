from os import listdir
import pandas as pd


for csvfile in listdir('csv'):
    df = pd.read_csv('csv/'+csvfile)
    saved_column = df[['date', 'text', 'url', 'source']]
    timeline_articles = saved_column.sort_values('date')
    return timeline_articles
