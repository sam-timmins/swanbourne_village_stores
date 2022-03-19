def site_contexts(request):
    """ Site contexts variables """

    store_name = 'Swanbourne Village Stores'

    contexts = {
        'store_name': store_name,
    }

    return contexts
