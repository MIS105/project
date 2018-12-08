from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity
# Create your views here.

def hello_world(request):
    return HttpResponse("Hello World!")
def home(request):
	activity_list = Activity.objects.all()
	return render(request,'index.html',{
		'activity_list':activity_list,
	})
	
def activity_detail(request, pk):
    activity = Activity.objects.get(pk=pk)
    return render(request, 'index.html', {'activity': activity})
