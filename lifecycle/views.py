from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from lifecycle.models import LifeCycleCurve as lc

# Create your views here.
def index(request):
	date_number = lc.objects.all()
	context = {'date_number': date_number}
	return render(request, "lifecycle/index.html", context)
