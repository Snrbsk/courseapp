from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
from . models import Course,Categories, Slider
from courses.forms import CourseForm
from django.contrib.auth.decorators import login_required, user_passes_test


def index(request):

    courses = Course.objects.filter(isActive=1, isHome=True)
    categories = Categories.objects.all()
    sliders = Slider.objects.filter(isActive=True)

    return render(request,"courses/index.html",{
        'courses' : courses,
        'categories' : categories,
        'sliders' : sliders,

    })

def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        courses = Course.objects.filter(isActive = True, title__contains =q).order_by("date")
        categories = Categories.objects.all()
    else:
        return redirect("/course")


    return render(request,'courses/search.html',{
        'courses' : courses,
        'categories' : categories,
    })

def detail(request, slug):

    course = get_object_or_404(Course, slug = slug)
    
    context = {
        'course' : course
    }
    return render(request, "courses/detail.html", context )

def isAdmin(user):
    return user.is_superuser

@user_passes_test(isAdmin)
def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/course")
    else:   
        form = CourseForm()
    return render(request, "courses/createCourse.html", {"form":form})

def getCoursesByCategory(request, slug):

    courses = Course.objects.filter(categories__slug=slug, isActive = True).order_by("date")
    categories = Categories.objects.all()

    paginator = Paginator(courses,3)
    page = request.GET.get('page',1)
    page_obj = paginator.get_page(page) 

    print(page_obj.paginator.count)
    print(page_obj.paginator.num_pages)


    return render(request,'courses/list.html',{
        'page_obj' : page_obj,
        'categories' : categories,
        'seciliKategori' : slug
    })

def course_list(request):
    courses = Course.objects.all()

    return render(request,"courses/listCourse.html",{
            'courses' : courses
        })

@login_required()
def course_edit(request,id):
    if not request.user.is_authenticated:
        return redirect("user_login")
    
    course = get_object_or_404(Course, pk=id)

    if(request.method == "POST"):
        form= CourseForm(request.POST, request.FILES, instance=course)
        form.save()
        return redirect("course-list") 
    else:
        form= CourseForm(instance=course)
    
    return render(request,"courses/editCourse.html",{"form":form})

@login_required()
def course_delete(request,id):
    if not request.user.is_authenticated:
        return redirect("user_login")
    
    course = get_object_or_404(Course, pk=id)

    if(request.method == "POST"):
        course.delete()
        return redirect("course-list") 
    else:
        form= CourseForm(instance=course)
    
    return render(request,"courses/deleteCourse.html",{"course":course})

def upload(request):
    return render(request, "courses/upload.html")