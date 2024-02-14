from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Sec
from .bitvavo import MyBitvavo
from .plotly import Plot

# Create your views here.
@login_required
def bitvavo(request):
    model_keys = Sec.objects.all()
    bitv = MyBitvavo(model_keys)
    plot = Plot()

    
    pricelist = bitv.get_prices(["BTC-EUR", "ETH-EUR", "PEPE-EUR", "ADA-EUR", "SOL-EUR"])
    balance = bitv.get_portefeuille()
    tickerprice = bitv.engine.tickerPrice({})
    for i in balance:  
        for j in tickerprice:
            if j["market"]==i["symbol"]+"-EUR" and i["symbol"]!="EUR":
                i["value"] = str(float(i["available"])*float(j["price"]))
            elif i["symbol"] == "EUR":
                i["value"] = i["available"]
    print(balance)
    pie_available = plot.pie_chart_available(balance)
    pie_inorder = plot.pie_chart_inorder(balance)
        

    template = "bitvavo/bitvavo.html"
    context = {"pricelist": pricelist, "plot_available":pie_available, "plot_inorder":pie_inorder}
    return render(template_name=template, request=request, context=context)