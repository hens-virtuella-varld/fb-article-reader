from os import listdir
import pandas as pd


def process_csv():
    for csvfile in listdir('csv'):
        df = pd.read_csv('csv/'+csvfile)
        saved_column = df[['date', 'text', 'url', 'source']]
        timeline_articles = saved_column.sort_values('date').to_dict('records')
        return timeline_articles
