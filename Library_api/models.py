from django.db import models

class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    published_year=models.IntegerField()
    #vanakkam da mapla viralimalayila irunthu
#this is model