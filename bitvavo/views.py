from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def bitvavo(request):
    template = "bitvavo/bitvavo.html"
    context = {}
    return render(template_name=template, request=request, context=context)