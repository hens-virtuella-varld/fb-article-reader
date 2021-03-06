'''
make_data loads fan-page and article data into database.
'''
import csv
import urllib.request
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from process_csv import process_csv
from reader.models import FanPage, Article


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('csv/fanpage_list.csv') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                soup = BeautifulSoup(urllib.request.urlopen(
                    "https://mbasic.facebook.com/" + row[0]), "lxml")
                fanpage_name = soup.title.text
                fanpage = FanPage.objects.create(name=fanpage_name)

                timeline_articles = process_csv(row[0]+'.csv')
                Article.objects.bulk_create([
                    Article(
                        fanpage=fanpage,
                        time=article['date'],
                        url=article['url'],
                        text=article['text']
                    ) for article in timeline_articles
                ])
