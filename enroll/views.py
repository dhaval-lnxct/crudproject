from django.shortcuts import render
from .forms import studentregistration
from .models import User
# Create your views here.
def index(request):
    return render(request, 'base.html')
 

def addshow(request):
    if request.method == 'POST':
        fm = studentregistration(request.POST)
        if fm.is_valid():
         fm.save()
         fm = studentregistration()
    else:
        fm = studentregistration()
    stud= User.objects.all()
    return render(request,'addandshow.html',{'form':fm,'stud':stud})

def update(request):
    return render(request,'updatestudent.html')
