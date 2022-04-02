from django.shortcuts import render


def products(request):
    """ products view """

    return render(request, 'products/products.html')
