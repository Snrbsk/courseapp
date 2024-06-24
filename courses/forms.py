from django import forms
from django.forms import TextInput,Textarea,CheckboxInput,SelectMultiple
from courses.models import Course

# class CourseForm(forms.Form):
#     title = forms.CharField(
#         label="Name",
#         error_messages={"required" : "Name is required"},
#         widget=forms.TextInput(attrs={"class" : "form-control"}),)
#     description = forms.CharField(x
#         widget=forms.Textarea(attrs={"class" : "form-control"}))
#     imageUrl = forms.CharField(
#         widget=forms.TextInput(
#             attrs={"class" : "form-control"}),)
#     slug = forms.SlugField(
#         required=False,
#         widget=forms.TextInput(
#             attrs={"class" : "form-control"}),)

class CourseForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = '__all__'
        labels = {
            "title" : "Course Name",
            "imageUrl" : "Image Url",
        }
        widgets = {
            "title" : TextInput(attrs={"class":"form-control"}),
            "description" : Textarea(attrs={"class":"form-control"}),
            "imageUrl" : TextInput(attrs={"class":"form-control"}),
            "slug" : TextInput(attrs={"class":"form-control"}),
            "categories" : SelectMultiple(attrs={"class":"form-control"}),
        }
    