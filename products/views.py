from django.shortcuts import render


def products(request):
    """ products view """

    context = {

    }

    return render(
        request,
        'products/products.html',
        context,
        )
