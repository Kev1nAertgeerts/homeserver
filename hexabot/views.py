from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def hexabot(request):
    template = "hexabot/hexabot_home.html"
    context = {}
    return render(template_name=template, request=request, context=context)