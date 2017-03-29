from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("app1.home")


def app1_handle_args(args):
    pass


def app1_info(request):
    pass