from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpResponse

from .models import DivarData
import json

class GetData(DetailView):
    def get(self, request):
        title = request.GET["title"]
        description = request.GET["description"]
        category = request.GET["category"]

        
        if title and category and description:
            try:
                rent = request.GET["rent"]
                deposit = request.GET["deposit"]

                data = DivarData.objects.create(title=title, description=description, category=category, rent=rent, deposit=deposit)
                print(data.title)
            except:
                price = request.GET["price"]
                data = DivarData.objects.create(title=title, description=description, category=category, price=price)
                print(data.title)
                
        else:
            return HttpResponse("None Data")

        return data
    
data = {}
def get_all(request):
    try:
        a = DivarData.objects.all()
        print(a)
        for i in a:
            print(i.title)
            if i.rent != "" and i.deposit != "":
                data[i.pk] = {"title":i.title, "description":i.description, "category":i.category, "deposit":i.deposit, "rent":i.rent}
            else:
                data[i.pk] = {"title":i.title, "description":i.description, "category":i.category, "price":i.price}
        return HttpResponse(data.values())
    except:
        return HttpResponse("invalid")


