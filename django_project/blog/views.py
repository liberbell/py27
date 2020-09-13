from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("""
                           <!doctype html>
                           <html>
                           <head>
                               <title></title>
                           </head>
                           <body>
                           Welcome to Liber Park
                           </body>
                           </html>
                        """)