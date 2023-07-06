from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'base.html')


def about(reqeust):
    pass


def contact(reqeust):
    pass
