from django.shortcuts import render
from .forms import LandingForm
from .models import landing

def index(request):
	all_objects = landing.objects.all()

	return render(request, 'landing/list.html', {'all_objects': all_objects})

