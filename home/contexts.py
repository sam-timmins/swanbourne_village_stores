def site_contexts(request):
    """ Site contexts variables """

    store_name = 'Swanbourne Village Stores'
    currency = '£'

    contexts = {
        'store_name': store_name,
        'currency': currency,
    }

    return contexts
