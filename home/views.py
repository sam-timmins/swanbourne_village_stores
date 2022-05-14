from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages


def index(request):
    """ A view to return the index page
    and send an email when  the contact form is submitted
    """

    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_message = request.POST['message']

        name = message_name.strip()
        message = message_message.strip()

        if not message:
            saved_name = name
            saved_email = message_email

            messages.error(
                request,
                'Please include a message so we can help.'
                )
            return render(request, 'home/index.html', {
                'saved_name': saved_name,
                'saved_email': saved_email,
            })

        elif not name:
            saved_email = message_email
            saved_message = message

            messages.error(
                request,
                'Please include your name.'
                )
            return render(request, 'home/index.html', {
                'saved_message': saved_message,
                'saved_email': saved_email,
            })

        else:
            send_mail(
                f'Message from {name}',
                message_message,
                message_email,
                ['sam.timmins1@gmail.com', ],
                )

        return render(request, 'home/index.html', {
            'name': name,
        })

    else:
        return render(request, 'home/index.html')


def privacy_policy(request):
    """ A view to return the privacy policy """

    return render(request, 'home/privacy-policy.html')
