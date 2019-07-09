from django.core.management.base import BaseCommand, CommandError

from reader.models import FanPage

import urllib.request
from bs4 import BeautifulSoup
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('csv/fanpage_list.csv') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                soup = BeautifulSoup(urllib.request.urlopen(
                    "https://mbasic.facebook.com/" + row[0]), "lxml")
                fanpage_name = soup.title.text
                FanPage.objects.create(name=fanpage_name)
