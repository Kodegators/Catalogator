from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'administrador/index.html')


def produtos(request):
    return render(request, 'administrador/produtos.html')
