from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app.forms import *

from django.views.generic import View
#for class based views ,in generic module we are using a class named as view
from django.views.generic import TemplateView
#for dealing with templates we are using a class named as TemplateView

#returning string as response by using func based views

def fbv_string(request):
    return HttpResponse('this is a string from function based view')

#returning string as a response by using class based views
class cbvstring(View):
    def get(self,request):
        return HttpResponse('this string belongs to class based views')
        #in a class obj is mandatory to display objects we are using def get(self,request)
        #for class based views it will not work so to work the class views,
        #we need to give cbvstring.as_view() in urls
        #path('suffix/',functionaddress.as_view(),name='name of url')



#rendering html by func based views
def fbvhtml(request):
    return render(request,'fbvhtml.html')   

#rendering html page by class based views
class cbvhtml(View):
    def get(self,request):
        return render(request,'cbvhtml.html')  

#insert data by fbv through model forms  
def insert_school_by_fbv(request):
    sfo=SchoolForm()
    d={'SFO':sfo}       

    if request.method=='POST':
        SFDO=SchoolForm(request.POST)  
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert data by fbv is done')  
    return render(request,'insert_school_by_fbv.html',d)  

#insert data by using class based views
class InsertSchoolByCbv(View):
    def get(self,request):
        ESFO=SchoolForm()
        d={'ESFO':ESFO} 
        return render(request,'InsertSchoolByCbv.html',d)  
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Insert school by cbv is done')  

#by using class based views we are using code reusability
class Cbv_Template(TemplateView):
    template_name='Cbv_Template.html'                      
