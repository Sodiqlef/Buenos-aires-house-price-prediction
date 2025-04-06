from django.shortcuts import render
from .forms import PricePredictionForm
from .models import PricePrediction
from .houseprediction import test_model

def index(request):
    predicted_price = None
    if request.method == "POST":
        form = PricePredictionForm(request.POST)
        if form.is_valid():
            surface_covered_in_m2 = form.cleaned_data["surface_area"]
            lat = form.cleaned_data["latitude"]
            lon = form.cleaned_data["longitude"]
            neighbourhood = form.cleaned_data["neighborhood"]
            
            # Get the predicted price
            predicted_price = test_model(surface_covered_in_m2, lat, lon, neighbourhood)
            
            # Save the prediction to the database
            PricePrediction.objects.create(
                surface_area=surface_covered_in_m2,
                latitude=lat,
                longitude=lon,
                neighborhood=neighbourhood,
                predicted_price= predicted_price
            )

    else:
        form = PricePredictionForm()
    
    if predicted_price != None:
        predicted_price = "{:,}".format(int(predicted_price))

    return render(request, "index.html", {
        "form": form,
        "predicted_price": predicted_price
    })
