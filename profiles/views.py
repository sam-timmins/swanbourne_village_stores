from django.shortcuts import render


def profile(request):
    """
    Profile view
    """
    context = {}

    return render(request, 'profiles/profile.html', context)
