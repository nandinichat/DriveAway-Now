from collections import OrderedDict
from django.http import HttpResponse
from django.shortcuts import render
from car.models import Booking, Form, Registration
# Create your views here.
# views.py

def login(request):

    
        return  render(request, 'login.html')  #  successful 


def home(request):
  #  return HttpResponse("This is CAR module")
    return render(request, 'main.html') 

def details(request):
    return render(request, 'details.html')

def confirmed(request):
    return render(request, 'confirmed.html')
  # Assuming you have an Order model defined

def booking(request):
    if request.method == 'POST':
        pickup_location = request.POST.get('pickup_location')
        dropoff_location = request.POST.get('dropoff_location')
        pickup_date = request.POST.get('pickup_date')
        dropoff_date = request.POST.get('dropoff_date')

        # Create and save the Order object
        order = OrderedDict.objects.create(
            pickup_location=pickup_location,
            dropoff_location=dropoff_location,
            pickup_date=pickup_date,
            dropoff_date=dropoff_date
        )

        # Pass the order object to the template
        context = {'order': order}

        # Render the confirmed.html template with the order data
        return render(request, 'confirmed.html', context)
    else:
        return render(request, 'booking.html')





def registered(request):
    first_name= request.POST['fn']
    last_name= request.POST['ln']
    email= request.POST['email']
    password= request.POST['password']

    person= Registration( first_name=first_name, last_name= last_name, email=email, password=password)
    person.save()
    return render(request, 'registered.html', {'fn': first_name})
