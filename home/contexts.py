def site_contexts(request):
    """ Site contexts variables """

    store_name = 'Swanbourne Village Stores'
    currency = '£'
    facebook = 'https://www.facebook.com/SwanbourneStores'
    instagram = 'https://www.instagram.com/'
    twitter = 'https://www.twitter.com/'

    contexts = {
        'store_name': store_name,
        'currency': currency,
        'facebook': facebook,
        'instagram': instagram,
        'twitter': twitter,
    }

    return contexts
