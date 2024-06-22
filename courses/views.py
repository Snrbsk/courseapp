from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from . models import Course,Categories

def index(request):

    courses = Course.objects.filter(isActive=1)
    categories = Categories.objects.all()

    return render(request,"courses/index.html",{
        'courses' : courses,
        'categories' : categories
    })

def detail(request, slug):

    course = get_object_or_404(Course, slug = slug)
    
    context = {
        'course' : course
    }
    return render(request, "courses/detail.html", context )

def getCoursesByCategory(request, slug):

    courses = Course.objects.filter(categories__slug=slug, isActive = True).order_by("date")
    categories = Categories.objects.all()

    paginator = Paginator(courses,2)
    page = request.GET.get('page',1)
    page_obj = paginator.get_page(page) 

    print(page_obj.paginator.count)
    print(page_obj.paginator.num_pages)


    return render(request,'courses/index.html',{
        'page_obj' : page_obj,
        'categories' : categories,
        'seciliKategori' : slug
    })