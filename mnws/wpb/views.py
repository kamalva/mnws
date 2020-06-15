from django.shortcuts import render

def index(request):
    return render(request,'wpb/index.html')
def politics(request):
    return render(request,'wpb/politics.html')
def cts(request):
    return render(request,'wpb/cts.html')
# Create your views here.
def contactus(request):
    return render(request, 'wpb/contactus.html')
def about(request):
    return render(request, 'wpb/about.html')
def psych(request):
    return render(request,'wpb/psych.html')
def thil(request):
    return render(request,'wpb/thil.html')
import re

from django.db.models import Q
from wpb.models import Entry
from django.views.generic import TemplateView, ListView



class HomePageView(TemplateView):
    template_name = 'wpb/index.html'

class SearchResultsView(ListView):
    model = Entry
    template_name = 'wpb/search.html'


    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Entry.objects.filter(
            Q(title__icontains=query) | Q(link__icontains=query)
        )
        return object_list
