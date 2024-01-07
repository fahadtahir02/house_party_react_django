#Here is where all endpoints go

from django.shortcuts import render
#import https response
from django.http import HttpResponse



#Here is where all endpoints go


def main(request):
    return HttpResponse("Hello")
