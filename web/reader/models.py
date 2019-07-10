from django.db import models


class FanPage(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    fanpage = models.ForeignKey(FanPage, on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField()
    url = models.URLField(max_length=2000)
    read = models.BooleanField(default=False)
    starred = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.fanpage}, {self.time}'
