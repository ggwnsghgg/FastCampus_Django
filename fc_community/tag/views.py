from django.shortcuts import render

# Create your views here.
class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='태그명')