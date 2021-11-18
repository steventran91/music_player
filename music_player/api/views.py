from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Write endpoint /hello, /hi 

def main(request):
    return HttpResponse("<h1>hello<h1>")
