from django.http import HttpResponse, HttpResponseRedirect,HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse

data ={
    "programming" : "Programming Courses",
    "web" : "Web Courses",
    "mobile" : "Mobil Courses",
    }

def list(request):
    return HttpResponse("List Page")

def detail(request, course_name):
    return HttpResponse(f'{course_name} detail page')

def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name];
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("Wrong Category Choosen")
    

def getCoursesByCategoryId(request, category_id):
    return redirect('/course/category/web')