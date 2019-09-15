from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from listings.choices import price_choices, bedroom_choices, state_choices
from listings.models import Listing
from realtors.models import Realtor
# Create your views here.


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    # get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,

    }
    return render(request, 'pages/about.html', context)

# def index(request):
#  if index:
#     return HttpResponse('<h1>Page was found, I had to do it my way....</h1>')
#  else:
#      return HttpResponseNotFound('<h1>Page not found</h1>')
