from django.shortcuts import render
from django.core.mail import send_mail

from .models import Reviews


def index(request):

    reviews = Reviews.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        email = request.POST['email']
        message = request.POST['message']

        # send an email
        send_mail(
            'Request from' + name,  # subject
            'Sender:' + name + '\n Tel:' + number + '\n Message:' + message,
            email,  # from email
            ['atengineeringsolutions@gmail.com']  # to email
        )

        context = {
            'reviews': reviews,
            'name': name,
            'number': number,
            'email': email,
            'message': message,
        }
        return render(request, 'home/index.html', context)
    else:
        context = {
            'reviews': reviews,
        }
        return render(request, 'home/index.html', context)
