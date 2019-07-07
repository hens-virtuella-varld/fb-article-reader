from django.shortcuts import render

from process_csv import process_csv


def index(request):
    context = {'timeline_articles': process_csv()}
    return render(request, 'reader/index.html', context)
