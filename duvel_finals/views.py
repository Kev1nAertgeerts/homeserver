from django.shortcuts import render
from .models import DuvelCollection

# Create your views here.
def duvel_finals(request):
    template = "duvel/finals.html"

    collection = DuvelCollection.objects.all().values()
    context = {"collection":collection}
    
    return render(request=request, template_name=template, context=context)