from django.shortcuts import render, redirect
from .models import DuvelCollection

# Create your views here.
def duvel_finals(request):
    template = "duvel/finals.html"

    collection = DuvelCollection.objects.all().values()
    context = {"collection":collection}

    if request.method == "POST" and request.POST.get("name")!=None:
        name = request.POST.get("name")
        year = request.POST.get("year")
        foto = request.POST.get("foto")
        waarde = request.POST.get("waarde")
        new_final = DuvelCollection(name=name, year=year, photo=foto, price=waarde)
        new_final.save()
        return redirect("duvel_finals:duvel_finals")

    
    
    return render(request=request, template_name=template, context=context)