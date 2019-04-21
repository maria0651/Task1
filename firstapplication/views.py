from django.shortcuts import render
from django.http import HttpResponse
from . import forms


# Create your views here.
def index(request):
    return HttpResponse("Hello, I just created my first application.")

def template_demo(request):
    dict_var= {'random_var' : "I am written in views.py"}
    return render(request,'firstapplication/index.html', context= dict_var)

def form_view(request):
    form = forms.FormName()
    if request.method == "POST":
        if form.is_valid():
            form = forms.FormName(request.POST)
            form.save()

    return render(request,'firstapplication/basic_form.html',{form1:form})
