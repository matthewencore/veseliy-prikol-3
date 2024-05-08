from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main (request):
    print(f"INFO | {__name__} {request.user} ")
    return HttpResponse("200")
    