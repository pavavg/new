# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)
