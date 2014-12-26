__author__ = 'Abhilash'

from django.http import HttpResponse
from django.shortcuts import render_to_response

import datetime
def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    if(html):
        return HttpResponse(html)
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

