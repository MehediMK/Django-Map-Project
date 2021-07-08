from django.shortcuts import render,redirect
from .models import MyMap

# Create your views here.
def index(request):
    if request.method == 'POST':
        location = request.POST['address']
        MyMap(address=location).save()
        return redirect('home')
    else:
        address = MyMap.objects.all()
        mapbox_token = 'pk.eyJ1IjoibWFwYm94MTQ1MyIsImEiOiJja3F1dnBka2QwOGllMnBvODA5dGN2ejJmIn0.M5C9oRSB9tzmD5VrIhYp6g'
        context = {
            'map_address':address,
            'map_token':mapbox_token,
        }
    return render(request,'index.html',context)