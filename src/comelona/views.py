from django.shortcuts import render
from .models import platillo
# Create your views here.
def index(request):
    platos=platillo.objects.all()
    return render(request,'index.html',{'platos':platos})