from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity
from .forms import nameForm
from datetime import datetime
import json 

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello World!")
	
def home(request):
	map_list = Activity.objects.all()
	return render(request,'index.html',{
		'activity_list':activity_list,
	})
	
def activity_detail(request, pk):
    activity = Activity.objects.get(pk=pk)
    return render(request, 'pk.html', {'activity': activity})
import json

#def search(request, keyword):
#    activity_list = Activity.objects.filter(name=keyword)
#    return render(request, 'index.html', {'activity_list':activity_list,})

def addActivity(request):
    activity_list = Activity.objects.all()
    mlist = Activity.objects.all()
    map_list = []
    for m in mlist:
        m.__dict__.pop("_state")
        map_list.append(m.__dict__)		
    if request.method == 'POST': #是否为post请求
        form = nameForm(request.POST)
        if form.is_valid(): #检查输入是否规范
            name = form.cleaned_data['name']
            sdt = form.cleaned_data['sdt']
            edt = form.cleaned_data['edt']
            place = form.cleaned_data['place']
            website = form.cleaned_data['website']
            sdt = sdt.replace('T',' ')
            edt = edt.replace('T',' ')  
            newdata = name+" "+sdt+" "+edt+" "+place+" "+website
            Activity.objects.create(name = name, start_datetime = sdt, end_datetime = edt, place = place, website = website)      
            activity_list = Activity.objects.all()
            return render(request,'index.html',{'activity_list': activity_list,   'map_list': json.dumps(map_list),})
        return render(request,'index.html',{'activity_list': activity_list,   'map_list': json.dumps(map_list),})   
    return render(request,'index.html',{'activity_list': activity_list,  'map_list': json.dumps(map_list),})


def search(request):
    keyword = request.POST.get('search')
    activity_list = Activity.objects.filter(name__contains=keyword)
    mlist = Activity.objects.filter(name__contains=keyword)
    map_list = []
    for m in mlist:
        m.__dict__.pop("_state")
        map_list.append(m.__dict__)
    return render(request, 'index.html', {'activity_list':activity_list,  'map_list': json.dumps(map_list),})
    


    
