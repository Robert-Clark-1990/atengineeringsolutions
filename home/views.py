from django.shortcuts import render

from .models import Reviews
from .forms import ReviewsForm


def index(request):

    reviews = Reviews.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'home/index.html', context)
