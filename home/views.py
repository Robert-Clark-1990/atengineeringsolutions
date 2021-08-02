from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .models import Reviews
from .forms import ContactForm


def index(request):

    reviews = Reviews.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            subject = "Job Inquiry from " + name
            body = {
                'name': form.cleaned_data['name'],
                'number': form.cleaned_data['number'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = '''
            From: {}
            Tel: {}
            Email: {}

            Message: {}
            '''.format(body['name'], body['number'],
                       body['email'], body['message'])
            send_mail(subject, message, 'atengineeringsolutions@gmail.com',
                      ['atengineeringsolutions@gmail.com'],
                      auth_user=None, auth_password=None)
            context = {
                'name': name,
            }
            return redirect('home', context)

    form = ContactForm()
    context = {
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'home/index.html', context)
