from os import listdir
from django.shortcuts import render

from process_csv import process_csv


def index(request):
    context = {'pages': listdir('csv')}
    return render(request, 'reader/index.html', context)


def detail(request, page):
    context = {'timeline_articles': process_csv(page)}
    return render(request, 'reader/detail.html', context)
