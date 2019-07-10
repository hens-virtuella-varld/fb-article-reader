from os import listdir
from django.shortcuts import render
from django.views import generic

from process_csv import process_csv
from .models import FanPage


class IndexView(generic.ListView):
    template_name = 'reader/index.html'
    model = FanPage


class DetailView(generic.DetailView):
    pass

# def detail(request, page):
#     context = {'timeline_articles': process_csv(page)}
#     return render(request, 'reader/detail.html', context)
