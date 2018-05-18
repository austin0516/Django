from django.shortcuts import render
from django.http import HttpResponse

def homepage(request,):
	return render(request, "index.html", locals())

def leftsidebar(request,):
	return render(request, "left-sidebar.html", locals())

def nosidebar(request,):
	return render(request, "no-sidebar.html", locals())

def rightsidebar(request,):
	return render(request, "right-sidebar.html", locals())


# Create your views here.
