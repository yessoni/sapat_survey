from multiprocessing import context
from django.shortcuts import redirect, render

from survey_form.serializers import CategorySerializer
from rest_framework import generics,viewsets
from .models import *

# Create your views here.
from django.db.models import Count


def home(request):
    if request.method == "POST":
        if request.POST.getlist("choices") and request.POST.get('area') and request.POST.get('check'):
            for data in request.POST.getlist("choices"):
                if ServayEntry.objects.filter(show_id=int(data), sessionId=request.COOKIES['csrftoken'], area_id=int(request.POST.get('area')), gender=request.POST.get('check'), name=request.POST.get('username')).exists():
                    print("inside if")
                    pass
                else:
                    print("inside else")
                    ServayEntry.objects.create(show_id=int(data), sessionId=request.COOKIES['csrftoken'], area_id=int(
                        request.POST.get('area')), gender=request.POST.get('check'), name=request.POST.get('username'))
            return render(request, 'diwali_offer/thank-you.html')

    # shows = Shows.objects.all()
    channel = Channel.objects.all()
    cat = Category.objects.all()
    area = Area.objects.all()

    shows = Shows.objects.prefetch_related(
        'show_survey').annotate(Count("show_survey")).all()

    context = {
        "channel": channel,
        "cat": cat,
        "shows": shows,
        "area": area,
    }
    return render(request, 'diwali_offer/home.html', context)
    # return render(request, 'diwali_offer/thank-you.html')


def dashboard(request):
    channel = Channel.objects.all()
    cat = Category.objects.all()
    area = Area.objects.all()

    shows = Shows.objects.prefetch_related(
        'show_survey').annotate(Count("show_survey")).all()

    data_dict = {}
    for s in Shows.objects.all():
        final_dict = {}
        for a in area:
            scount = ServayEntry.objects.filter(
                area_id=a.id, show_id=s.id).all().count()
            final_dict[a.id] = scount
        data_dict[s.id] = final_dict

    context = {
        "channel": channel,
        "cat": cat,
        "shows": shows,
        "area": area,
        "data_dict": data_dict,
    }
    return render(request, 'diwali_offer/visitor-count.html', context)


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
