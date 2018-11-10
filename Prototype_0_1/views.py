from django.shortcuts import render


def index(request):
    return render(request, 'Website_0_1/Unauthenticated/index.html')
