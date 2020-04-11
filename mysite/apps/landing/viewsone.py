from django.shortcuts import render
from .forms import LandingForm



def one(request):
	form = LandingForm(request.POST or None)
	if request.method == "POST":
		new_form = form.save()
	return render(request, 'landing/onelist.html',locals ())

 