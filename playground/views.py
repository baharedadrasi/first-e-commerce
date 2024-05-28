from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action

def say_hello(request):
    # return HttpResponse('Hello, Django!')
    return render(request, 'hello.html', {'name': 'Bahare'})

def say_hello_new(request):
    return HttpResponse('Hello World!')
