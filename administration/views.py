from django.shortcuts import render


def administration(request):
    """ A view to return the privacy policy """

    return render(request, 'administration/administration.html')
