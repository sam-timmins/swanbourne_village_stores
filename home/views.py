from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    """ A view to return the index page
    and send an email when  the contact form is submitted
    """

    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            f'Message from {message_name}',
            message,
            message_email,
            ['sam.timmins1@gmail.com', ],
            )

        return render(request, 'home/index.html', {
            'message_name': message_name,
        })

    else:
        return render(request, 'home/index.html')
