from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Diepvries
from .decorators import change_template

# Create your views here.
def home_page(request):
    template = "main/home.html"
    context = {}
    return render(request=request, context=context, template_name=template)

@login_required
#@change_template("main\digitale_meter.html")
def digi_meter_page(request):
    template = "main/digitale_meter.html"
    context = {}
    return render(request=request, context=context, template_name=template)

@login_required
def tegenw_tijd_page(request):
    template = "main/tegenw_tijd.html"
    context = {}
    return render(request=request, context=context, template_name=template)

def diepvries_page(request):
    template = "main/diepvries.html"
    inhoud = Diepvries.objects.all().order_by("datum").values()

    if request.method == "POST" and request.POST["potnummer"] != "":
        try:
            x=Diepvries.objects.get(pot_nummer=request.POST["potnummer"])
            x.omschrijving = request.POST["omschrijving"]
            x.personen = request.POST["personen"]
        except:
            x=Diepvries(pot_nummer=request.POST["pot"], omschrijving = request.POST["omschrijving"], personen = request.POST["personen"])
        x.save()
        redirect("main:diepvries")
        
    context = {"inhoud":inhoud}
    return render(request=request, context=context, template_name=template)