from django.shortcuts import render
from car.models import BrandModel, CarModel
def home(req,brand_slug=None):
    data = CarModel.objects.all()
    
    if brand_slug is not None:
        fil = BrandModel.objects.get(slug=brand_slug)
        data = CarModel.objects.filter(brand = fil)
        
    brand = BrandModel.objects.all()
    return render(req, 'home.html', {'data':data, 'brand':brand})