from django.http import HttpResponse, HttpResponseRedirect,HttpResponseNotFound # type: ignore
from django.shortcuts import redirect, render # type: ignore
from django.urls import reverse # type: ignore
from datetime import date,datetime
data ={
    "programming" : "Programming Courses",
    "web" : "Web Courses",
    "mobile" : "Mobil Courses",
    }   

db = { 
    "courses" : [
        {"title" : "Javascript ",
        "description" : "Javascript Course",
        "imageUrl" : "1.jpg",
        "slug" : "Js-Kursu",
        "date" : datetime.now(),
        "isActive" : True,
        "isUpdated" : True, },
        {"title" : "Python ",
        "description" : "Python Course",
        "imageUrl" : "2.jpg",
        "slug" : "Python-Kursu",
        "date" : date(2023,9,13),
        "isActive" : True,
        "isUpdated" : False, },
        {"title" : "Web Development ",
        "description" : "Web Course",
        "imageUrl" : "3.jpg",
        "slug" : "Wev-Kursu",
        "date" : date(2021,7,25),
        "isActive" : True,
        "isUpdated" : True, },
    ],
    "categories" : [
        { 'id' : 1, 'name':"Programming", 'slug' : "programming"},
        { 'id' : 2, 'name':"Web Development", 'slug' : "web-development"},
        { 'id' : 3, 'name':"Mobile Apps", 'slug' : "mobile-apps"},
        ]
}


def index(request):

    courses = [course for course in db["courses"] if course["isActive"] ==True]
    categories = db["categories"]

    return render(request,"courses/index.html",{
        'courses' : courses,
        'categories' : categories
    })

def detail(request, course_name):
    return HttpResponse(f'{course_name} detail page')

def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return render(request,'courses/courselist.html', {
            'category' : category_name,
            'category_text' : category_text,
        })
    except:
        return HttpResponseNotFound("Wrong Category Choosen")
    

def getCoursesByCategoryId(request, category_id):
    return redirect('/course/category/web')